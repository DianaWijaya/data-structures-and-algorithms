import sys


ASCII_MIN = 8
ASCII_MAX = 126
ASCII_RANGE = ASCII_MAX - ASCII_MIN + 1  # 119


class Node:
    """
    This class represents a node in the suffix tree.
    """
    def __init__(self, is_leaf, id=None):
        """
        Initializer for the node in the suffix tree.
        """
        self.id = id
        self.children = [None] * ASCII_RANGE
        # self.children = {}
        self.is_leaf = is_leaf
        self.suffix_link = None
        self.file_ids = []
        self.suffix_start_index = None

    def get_edge(self, char):
        """
        Retrieves the outgoing edge corresponding to the given character.

        Args:
            char (str): A single character representing the edge to retrieve.

        Returns:
            Edge or None: The edge associated with the character, or None if it does not exist.
        """
        return self.children[ord(char) - ASCII_MIN]
        # return self.children.get(char, None)

    def add_edge(self, char, edge):
        """
        Adds an outgoing edge for the given character.

        Args:
            char (str): A single character representing the label of the edge.
            edge (Edge): The edge object to be added.
        """
        self.children[ord(char) - ASCII_MIN] = edge
        # self.children[char] = edge


class GlobalEnd:
    """
    This class represents the global pointer, where leaf edges share the same end index, which grows as new characters 
    are added to the text.
    """
    def __init__(self):
        """
        Initializer for the global pointer
        """
        self.index = 0


class Edge:
    """
    This class represents the edge from a node to another node, or to itself in the suffix tree
    """
    def __init__(self, start, end, node_from, destination):
        """
        Initializes an Edge with specified start and end positions, and connecting nodes.

        Args:
            start (int): Start index of the edge label in the text.
            end (int or GlobalEnd): End index or a GlobalEnd object for dynamic updates.
            node_from (Node): Source node of the edge.
            destination (Node): Destination node of the edge.
        """
        self.start = start
        self.end = end
        self.node_from = node_from
        self.destination = destination

    def get_edge_length(self):
        """
        Calculates and returns the current length of the edge.

        Returns:
            int: The length of the substring represented by this edge.
        """
        if isinstance(self.end, GlobalEnd):
            return self.end.index - self.start + 1
        return self.end - self.start + 1

    def get_endpoint(self):
        """
        Retrieves the current end index of the edge.

        Returns:
            int: The current endpoint value, resolving GlobalEnd if necessary.
        """
        return self.end.index if isinstance(self.end, GlobalEnd) else self.end


class Remainder:
    """
    This class represents the remainder of the current suffix being processed during Ukkonen's algorithm.
    """
    def __init__(self, start=None, end=None):
        """
        Initializes a Remainder instance with optional start and end indices.

        Args:
            start (int, optional): Initial start index.
            end (int, optional): Initial end index.
        """
        self.start = start
        self.end = end

    def exists(self):
        """
        Checks if the remainder currently represents a valid substring.

        Returns:
            bool: True if both start and end are set; False otherwise.
        """
        return (self.start is not None) and (self.end is not None)

    def length(self):
        """
        Returns the length of the current remainder substring.

        Returns:
            int: Length of the remainder if it exists; 0 otherwise.
        """
        return self.end - self.start + 1 if self.exists() else 0

    def advance(self, steps):
        """
        Advances the start index of the remainder by the specified number of steps.

        If advancing causes start to exceed end, the remainder is reset.

        Args:
            steps (int): Number of positions to advance.
        """
        self.start += steps
        if self.start > self.end:
            self.reset()

    def reset(self):
        """
        Resets the remainder, clearing both start and end indices.
        """
        self.start = None
        self.end = None

    def set(self, start, end):
        """
        Sets the start and end indices of the remainder.

        Args:
            start (int): New start index.
            end (int): New end index.
        """
        self.start = start
        self.end = end

    def get_char(self, text):
        """
        Retrieves the current character pointed to by the remainder's start index.

        Args:
            text (str): The full text being processed.

        Returns:
            str or None: The character at position `start` if the remainder exists; None otherwise.
        """
        if self.exists():
            return text[self.start]
        return None


class SuffixTree:
    """
    This class represents a Suffix Tree data structure.
    """
    def __init__(self):
        """
        Initializes the suffix tree without anything initially
        """
        self.root = Node(is_leaf=False, id=0)
        self.root.suffix_link = self.root
        self.nodes = [self.root]
        self.node_count = 1
        self.text_count = 0
        self.text = ""
        self.text_offsets = []
        
    def insert_string(self, text, file_id):
        """
        Inserts a string into the suffix tree and updates its structure using Ukkonen's algorithm.

        Args:
            text (str): The string to be inserted into the suffix tree.
            file_id (int): Identifier for the inserted string, used for tracking suffix origins.
        """
        start_index = len(self.text)
        self.text += text
        self.text_offsets.append(start_index)

        # Check if this is the first string being inserted
        is_first = (self.text_count == 0)
        self.ukkonen_extend(start_index, len(text), file_id, is_first)
        self.text_count += 1
        
    def create_node(self, is_leaf, file_id=None):
        """
        Creates a new node in the suffix tree.

        Args:
            is_leaf (bool): Indicates whether the new node is a leaf.
            file_id (int): If provided and the node is a leaf, associates the node with this file ID.

        Returns:
            Node: The newly created node.
        """
        node = Node(is_leaf=is_leaf, id=self.node_count)
        self.node_count += 1
        self.nodes.append(node)
        
        # If this is a leaf node, record the file ID it belongs to
        if is_leaf and file_id is not None:
            if file_id not in node.file_ids:
                node.file_ids.append(file_id)
        
        return node

    def ukkonen_extend(self, start_index, length, file_id, is_first=False):
        """
        Extends the suffix tree with new characters from the inserted string using Ukkonen's algorithm.

        Args:
            start_index (int): The starting index of the new text in the concatenated text buffer.
            length (int): The length of the new text to be processed.
            file_id (int): Identifier for the inserted text, used to tag leaf nodes.
            is_first (bool, optional): Indicates if this is the first string being inserted. Defaults to False.
        """
        txt = self.text
        global_end = GlobalEnd()
        global_end.index = start_index

        active_node = self.root
        remainder = Remainder()

        # Determine where the extension loop should start
        if is_first:
            last_j = start_index
        else:
            last_j = start_index - 1

        # Create initial leaf and edge to start Ukkonen’s algorithm for the first string insertion
        if is_first:
            first_leaf = self.create_node(is_leaf=True, file_id=file_id)
            first_leaf.suffix_start_index = start_index - self.text_offsets[file_id]
            first_edge = Edge(start_index, global_end, self.root, first_leaf)
            self.root.add_edge(txt[start_index], first_edge)
            global_end.index = start_index 

        # Determine if we should skip the first character if it is the first string being inserted
        if is_first:
            start_increment = 1
        else:
            start_increment = 0

        # Main phase loop, one iteration for each character in the string
        for i in range(start_index + start_increment, start_index + length):
            global_end.index = i            # Move global end forward to include the current character
            j = last_j + 1                  # Start of the current extension
            previous_internal_node = None   # Tracks last created internal node for suffix links

            # Extension loop to process all pending suffixes
            while j <= i:
                current_node = active_node
                active_length = remainder.length()

                # Determine which character to match next
                if remainder.exists():
                    current_char = remainder.get_char(txt)
                else:
                    current_char = txt[i]

                edge = current_node.get_edge(current_char)

               # Trick 2: Walk down if remainder length covers the entire edge
                while remainder.exists() and edge and active_length >= edge.get_edge_length():
                    step = edge.get_edge_length()
                    remainder.advance(step)
                    active_length -= step
                    current_node = edge.destination
                    active_node = current_node
                    if not remainder.exists():
                        break
                    edge = current_node.get_edge(txt[remainder.start])

                # Case 1: Remainder exists, need to check character match or split edge
                if remainder.exists():
                    edge = current_node.get_edge(txt[remainder.start])
                    edge_pos = edge.start + active_length
                    next_char = txt[i]

                    # Mismatch found, split the edge and insert a new internal node with case 2
                    if txt[edge_pos] != next_char:
                        internal = self.create_node(is_leaf=False)

                        # Create new split edge for the remaining part of the old edge
                        split_edge = Edge(edge_pos, edge.end, internal, edge.destination)
                        internal.add_edge(txt[edge_pos], split_edge)

                        # Update old edge to end before the split point
                        edge.end = edge_pos - 1
                        edge.destination = internal

                        # Create a new leaf edge for the current character
                        leaf = self.create_node(is_leaf=True, file_id=file_id)
                        new_edge = Edge(i, global_end, internal, leaf)
                        internal.add_edge(next_char, new_edge)
                        leaf.suffix_start_index = i - self.text_offsets[file_id]

                        # Update suffix links if needed
                        if previous_internal_node:
                            previous_internal_node.suffix_link = internal
                        previous_internal_node = internal

                        # Update active point using Rule 1 or Rule 3
                        if active_node == self.root:
                            remainder.advance(1)
                        else:
                            active_node = active_node.suffix_link

                        if not remainder.exists():
                            remainder.reset()

                        # Move to the next extension
                        last_j = j
                        j = last_j + 1
                        continue

                    else:
                        # Characters match, so continue to next phase without splitting
                        offset = edge_pos - edge.start

                        # Update remainder with new start position
                        remainder.set(i - offset, i)

                        # Update suffix links if needed
                        if previous_internal_node and not current_node.is_leaf:
                            previous_internal_node.suffix_link = current_node

                        # Add file ID to the leaf if not already present
                        if edge.destination.is_leaf:
                            if file_id not in edge.destination.file_ids:
                                edge.destination.file_ids.append(file_id)

                        # No need to extend further for this phase, so jist break
                        break

                # Case 2: No matching edge, so create a new leaf edge
                else:
                    edge = current_node.get_edge(txt[i])
                    if edge is None:

                        # Create a new leaf node representing the current suffix
                        leaf = self.create_node(is_leaf=True, file_id=file_id)
                        new_edge = Edge(i, global_end, current_node, leaf)
                        current_node.add_edge(txt[i], new_edge)
                        leaf.suffix_start_index = i - self.text_offsets[file_id]

                        # If an internal node was created in the previous extension, update its suffix link to the current node
                        if previous_internal_node and not current_node.is_leaf:
                            previous_internal_node.suffix_link = current_node
                            previous_internal_node = None

                        # Update the active point
                        if active_node == self.root and remainder.exists():
                            remainder.advance(1)
                        else:
                            active_node = active_node.suffix_link

                        # If remainder is now empty, reset it for the next phase
                        if not remainder.exists():
                            remainder.reset()

                        # Move to the next extension
                        last_j = j
                        j = last_j + 1
                        continue

                    # Case 3: Show Stopper, matching edge already exists, stop extension early
                    else:
                        
                        # Set the remainder to start from the current position
                        remainder.set(i, i)

                        # If an internal node was created previously, link it to the current node
                        if previous_internal_node and not current_node.is_leaf:
                            previous_internal_node.suffix_link = current_node

                        # No further extension needed for this phase
                        break

    def print_tree(self):
        """
        Prints a readable representation of the suffix tree structure.
        """
        def recurse(node, depth):
            for ascii_code in range(ASCII_MIN, ASCII_MAX + 1):
                edge = node.children[ascii_code - ASCII_MIN]
                if edge is not None:
                    label = self.text[edge.start:edge.get_endpoint() + 1]
                    print(" " * depth + f"├─ {label}")
                    recurse(edge.destination, depth + 4)

        print("Suffix Tree Structure:")
        recurse(self.root, 0)

    def print_suffix_links(self):
        """
        Prints all suffix links between nodes in the suffix tree.
        """
        print("Suffix Links:")
        for node in self.nodes:
            if node.suffix_link:
                print(f"Node {node.id} → Node {node.suffix_link.id}")

    def print_all_nodes(self):
        """
        Prints detailed information for all nodes in the suffix tree.
        """
        print("Suffix Tree Nodes:")
        for node in self.nodes:
            suffix_info = f" (Suffix Start Index: {node.suffix_start_index})" if node.suffix_start_index is not None else ""
            node_type = "Leaf" if node.is_leaf else "Internal"
            print(f"Node {node.id}: [{node_type}]{suffix_info}")

            if node.suffix_link:
                print(f"    Suffix Link: Node {node.suffix_link.id}")
            else:
                print(f"    Suffix Link: None")


    def suffix_array(self):
        """
        Constructs and returns the suffix array from the suffix tree.

        Returns:
            list[int]: The suffix array containing starting indices of all suffixes in sorted order.
        """
        result = []

        def dfs(node):
            if node.is_leaf and node.suffix_start_index is not None:
                result.append(node.suffix_start_index)
            else:
                for ascii_code in range(ASCII_MIN, ASCII_MAX + 1):
                    edge = node.children[ascii_code - ASCII_MIN]
                    if edge is not None:
                        dfs(edge.destination)

        def suffix_key(index):
            """Returns the suffix starting at the given index in the text."""
            return self.text[index:]

        dfs(self.root)
        return sorted(result, key=suffix_key)


    def get_longest_common_prefix(self, text_start_index, pattern):
        """
        Computes the length of the longest common prefix between a substring of the text and the given pattern using the 
        suffix tree.

        Args:
            text_start_index (int): The starting index in the text to compare from.
            pattern (str): The pattern to compare against.

        Returns:
            int: Length of the longest common prefix found.
        """
        current_node = self.root
        pattern_pos = 0
        text = self.text
        text_pos = text_start_index

        while pattern_pos < len(pattern) and text_pos < len(text):

            # Try to find an outgoing edge for the current character in the text
            edge = current_node.get_edge(text[text_pos])

            # No matching edge, so just return current LCP length
            if not edge:
                return pattern_pos

            edge_length = edge.get_edge_length()
            edge_start_index = edge.start
            edge_char_offset = 0

            # Walk along the characters of the current edge
            while (edge_char_offset < edge_length 
                and pattern_pos < len(pattern) 
                and text_pos < len(text)):

                # Mismatch found, return current LCP length
                if pattern[pattern_pos] != text[edge_start_index + edge_char_offset]:
                    return pattern_pos

                # Characters match, move both pointers forward
                pattern_pos += 1
                text_pos += 1
                edge_char_offset += 1

            # Move to the next node in the tree after finishing the current edge
            current_node = edge.destination

        # Return the total length matched if loop completes without mismatch
        return pattern_pos


class GeneralizedSuffixTree:
    """
    Represents a Generalized Suffix Tree (GST) for efficiently handling multiple strings.

    Attributes:
        tree (SuffixTree): The underlying suffix tree structure.
    """
    def __init__(self, strings):
        """
        Initializes the GST with a collection of strings.

        Args:
            strings (list[str]): List of input strings to be inserted into the GST.
        """
        self.tree = SuffixTree()
        for file_id, s in enumerate(strings):
            self.tree.insert_string(s + '$', file_id)


def try_out(text, pattern):
    tree = SuffixTree()
    tree.insert_string(text + '$', 0)
    
    matches = near_exact_pattern_matching(text, pattern)
    
    # Only return the position and DL-distance as tuples
    result = [(pos, dl) for pos, dl in matches]
    return result

    
def near_exact_pattern_matching(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)

    # Constants to represent the type of match
    EXACT_MATCH = 0
    NEAR_EXACT_MATCH = 1
    
    if m == 0 or n == 0 or m > n + 1:
        return matches

    # Insert the text into a forward suffix tree
    tree = SuffixTree()
    tree.insert_string(text, 0)

    # Insert the reversed text into the reversed suffix tree
    rev_tree = SuffixTree()
    rev_tree.insert_string(text[::-1], 0)

    # Reverse the pattern
    reversed_pattern = pattern[::-1]

    for i in range(n):

        # Skip if not enough characters left for a match with ≤1 edit
        if n - i < m - 1:
            continue

        forward = tree.get_longest_common_prefix(i, pattern)

        # Compute backwards with shifted indices
        rev_start_exact = n - i - m
        rev_start_insert = n - i - (m - 1)
        rev_start_delete = n - i - (m + 1)

        # Compute backward matching lengths for different edit scenarios
        backward_exact = 0
        backward_insert = 0
        backward_delete = 0

        # Backward matching for exact match scenario
        if 0 <= rev_start_exact < n:
            backward_exact = rev_tree.get_longest_common_prefix(rev_start_exact, reversed_pattern)

        # Backward matching for insert scenario (skip one character in pattern)
        if 0 <= rev_start_insert < n:
            backward_insert = rev_tree.get_longest_common_prefix(rev_start_insert, reversed_pattern[:-1])

        # Backward matching for delete scenario (pattern remains the same, deletion handled by offset)
        if 0 <= rev_start_delete < n:
            backward_delete = rev_tree.get_longest_common_prefix(rev_start_delete, reversed_pattern)

        # CASE 1: Exact match
        if forward == m:
            matches.append((i + 1, EXACT_MATCH))

        # CASE 2: Insert (text has 1 extra character)
        elif m > 1 and forward + backward_insert >= m - 1 and i + forward < n:
            matches.append((i + 1 ,NEAR_EXACT_MATCH))

        # CASE 3: Replace (1 char mismatch)
        elif forward + backward_exact == m - 1:
            matches.append((i + 1 ,NEAR_EXACT_MATCH))

        # CASE 4: Swap (adjacent transposition)
        elif (
            m > 1 and
            forward + backward_exact == m - 2 and
            i + forward + 1 < n and
            forward + 1 < m and
            text[i + forward] == pattern[forward + 1] and
            text[i + forward + 1] == pattern[forward]
        ):
            matches.append((i + 1 ,NEAR_EXACT_MATCH))

        # CASE 5: Delete (delete 1 character)
        elif m > 1 and forward + backward_delete >= m:
            matches.append((i + 1 ,NEAR_EXACT_MATCH))

    return matches


def combining_patterns_and_texts(patterns, texts, pattern_numbers, text_numbers):
    """
    Finds approximate matches (DL-distance ≤ 1) for each pattern against each text and records the results 
    with corresponding pattern and text identifiers.

    Args:
        patterns (list[str]): List of patterns to search for.
        texts (list[str]): List of texts to search within.
        pattern_numbers (list[int]): Identifiers corresponding to each pattern.
        text_numbers (list[int]): Identifiers corresponding to each text.

    Returns:
        list[tuple]: List of matches in the form (pattern_number, text_number, match_position, edits).
    """
    matches = []
    for pattern_idx, pattern in enumerate(patterns):

        # Find matches of the current pattern in the current text
        for text_idx, text in enumerate(texts):
            match_results = near_exact_pattern_matching(text, pattern)

            # Record match with associated pattern and text identifiers
            for match_pos, edits in match_results:
                matches.append((pattern_numbers[pattern_idx], text_numbers[text_idx], match_pos, edits))

    return matches


def read_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python a2.py <run-configuration-filename>")
        sys.exit(1)

    config_filename = sys.argv[1]
    config_lines = read_file(config_filename)

    N, M = map(int, config_lines[0].strip().split())

    # Parse text files and their assigned numbers
    text_info = [line.strip().split() for line in config_lines[1:N+1]]
    text_numbers = [int(info[0]) for info in text_info]
    text_files = [info[1] for info in text_info]

    # Parse pattern files and their assigned numbers
    pattern_info = [line.strip().split() for line in config_lines[N+1:N+1+M]]
    pattern_numbers = [int(info[0]) for info in pattern_info]
    pattern_files = [info[1] for info in pattern_info]

    # Read file contents and flatten them into strings
    texts = [''.join(read_file(f)).replace('\n', '') for f in text_files]
    patterns = [''.join(read_file(f)).replace('\n', '') for f in pattern_files]

    # Perform pattern matching using correct numbering
    matches = combining_patterns_and_texts(patterns, texts, pattern_numbers, text_numbers)

    # Write results to output a2.txt using the required output format
    with open("output output a2.txt", "w") as out_file:
        for pattern_num, text_num, pos, edits in matches:
            out_file.write(f"{pattern_num} {text_num} {pos} {edits}\n")

    print("Results written to output output a2.txt")