class Node:
    def __init__(self):
        """
        Function description:
        Initialize a node for the trie. The link is an array of 5 elements, because the DNA sequence
        can only contain the characters A, B, C, D, and $. The end_indices are used to store the 
        indices of the DNA sequence that are traversed. 

        Input:
            None

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only initializes the node.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only initializes the node.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input space complexity is constant because it does not take any input.
        """
        self.link = [None] * 5
        self.end_indices = []

    def __str__(self):
        """
        Function description:
        Return the string representation of the node.

        Input:
            None

        Return:
            str: The string representation of the node.

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only returns the string representation of 
                      the node.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it stores the string representation of the 
                      node.

        Input space complexity: 
            Complexity: O(1)
            Analysis: The input space complexity is constant because it does not take any input.
        """
        return f"End indices: {self.end_indices}, Link: {self.link}"


# This code is partially based on the lecture video from FIT2004, Lecture 11 Trie, and the methods
# are modified to suit the requirements of the assignment.
# Link: https://www.youtube.com/watch?v=-6CfJUKueL0&list=PLd4dQRGEL270jV6Y_7LB-ISs9UaI2E5-O&index=45
class OrfFinder:
    def __init__(self, dna):
        """
        Function description:
        Initialize the OrfFinder class. The class takes the DNA sequence as input and initializes the 
        forward and reverse trie roots. The reversed trie is used to look for the indices of the end 
        sequence in the reverse order. In here, the DNA sequence is iterated over, and each concatenated 
        sequence is inserted into the forward trie and reversed trie.

        Input:
            dna: The DNA sequence represented as a string.

        Return:
            None

        Time complexity:
            Complexity: O(n^2), where n is the length of the DNA sequence.
            Analysis: The time complexity is quadratic because it iterates through the DNA sequence, then 
                      the insert function iterates through the DNA sequence again to insert the characters 
                      into the trie. The insert function has a time complexity of O(n), and it is called n 
                      times, resulting in a time complexity of O(n^2).

        Space complexity:
            Complexity: O(n), where n is the length of the DNA sequence.
            Analysis: The space complexity is linear because it only stores the reversed DNA sequence here.

        Input space complexity:
            Complexity: O(n), where n is the length of the DNA sequence.
            Analysis: The input space complexity is linear because it takes the DNA sequence as input.
        """

        # Store the DNA sequence, forward and reverse trie roots
        self.dna = dna
        self.forward_trie_root = Node()
        self.reverse_trie_root = Node()

        # Space complexity: O(n), because a new string is created, containing the characters of dna in reverse
        # Time complexity: O(n), where n is the length of the DNA sequence
        # Reverse the DNA sequence to be used for the reverse trie
        reversed_dna = ''.join(reversed(dna))

        # Time complexity: O(n^2), where n is the length of the DNA sequence
        # Insert all possible DNA sequences and its reverse into the trie 
        for i in range(len(dna)):
            self.insert(self.forward_trie_root, dna, i)
            self.insert(self.reverse_trie_root, reversed_dna, i)

    def char_to_index(self, char):
        """
        Function description:
        Helper function to convert the character to an index. The & terminal node is represented by 0,
        while the characters are converted to an index by subtracting the ASCII value of 'A' from the
        ASCII value of the character, then adding 1. This is done so that we can store the characters
        A-D starting from index 1. 

        Input:
            char: The character to be converted to an index.

        Return:
            The index of the character.

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only performs a simple operation to 
                      convert the character to an index.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the index of the character.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input space complexity is constant because it only takes a single character as 
                      input.
        """

        # If the character is '$', return 0. This is used to represent the end or terminal node.
        if char == "$":
            return 0
        
        # Convert the character to an index by subtracting the ASCII value of 'A' from the ASCII
        return ord(char) - ord('A') + 1

    def insert(self, root, dna, start_index):
        """
        Function description:
        Insert the DNA sequence into the trie using an index. The function iterates through the DNA
        sequence starting from the start index, and inserts the characters into the trie. A new node 
        is created if the link at the index is None. The start and end indices of the DNA sequence are 
        appended to the current node at every iteration.

        Input:
            root: The root node of the trie, can be the forward or reverse trie.
            dna: The DNA sequence represented as a string.
            start_index: The starting index of the DNA sequence to be inserted.

        Return:
            None

        Time complexity:
            Complexity: O(n), where n is the length of the DNA sequence.
            Analysis: The time complexity is linear because it iterates through the DNA sequence
                      to insert the characters into the trie.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores indices of each
                      of the node traversed, and it gets overwritten at each iteration.

        Input space complexity:
            Complexity: O(n), where n is the length of the DNA sequence.
            Analysis: The input space complexity is linear because it takes the entire DNA sequence
                      as input.
        """

        # Start from the root node
        current_node = root

        # Time complexity: O(n), where n is the length of the DNA sequence
        # Iterate through the DNA sequence starting only from the start index
        for i in range(start_index, len(dna)):

            # Convert the character to an index using the helper function created
            index = self.char_to_index(dna[i])

            # If the link at the index is None, create a new node
            if current_node.link[index] is None:
                current_node.link[index] = Node()

            # Move to the next node
            current_node = current_node.link[index]
            
            # Append the end indice of the DNA sequence to the current node
            current_node.end_indices.append(i)

        # Insert the terminal node at the end of the DNA sequence
        terminal_index = self.char_to_index("$")

        # If the link at the terminal index does not exist yet, create a new node
        if current_node.link[terminal_index] is None:
            current_node.link[terminal_index] = Node()

        # Move to the terminal node and append the end indice of the DNA sequence
        terminal_node = current_node.link[terminal_index]
        terminal_node.end_indices.append(i)

    def search(self, root, sequence):
        """
        Function description:
        Search for a DNA sequence in the trie, and return the node if it exists.

        Input:
            root: The root node of the trie, can be the forward or reverse trie.
            sequence: The DNA sequence to be searched from the trie.

        Return:
            The last node of the found DNA sequence found, otherwise return None.

        Time complexity:
            Complexity: O(n), where n is the length of the DNA sequence to be searched.
            Analysis: The time complexity is linear because it iterates through the DNA sequence to 
                      search for the DNA sequence in the trie, starting from the root node.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the node as it traverses
                      through the trie.

        Input space complexity:
            Complexity: O(n), where n is the length of the DNA sequence.
            Analysis: The input space complexity is linear because it takes sequence of the DNA to be
                      searched as input.
        """

        # Start from the root node
        current_node = root

        # Time complexity: O(n), where n is the length of the DNA sequence
        # Iterate through the DNA sequence to search for the sequence in the trie
        for char in sequence:

            # Convert the character to an index using the helper function created
            index = self.char_to_index(char)

            # If the link at the index is None, the sequence does not exist in the trie, return None
            if current_node.link[index] is None:
                return None
            
            # Move to the next node
            current_node = current_node.link[index]

        # Return the last node of the found DNA sequence
        return current_node
    
    def find(self, start, end):
        """
        Function description:
        This function finds all substrings of the DNA that contain the start and end prefixes. With 
        the Node, and OrfFinder classes ready, and initialized, this function simply calls the search
        method to find the start and end prefixes in the forward and reverse tries. Then, it constructs
        the substrings based on the indices of the start and end prefixes found in the tries.

        Approach description (if main function): 
        For this question, I used 2 tries, one for the forward sequence and one for the reverse sequence.
        The forward trie is used to search for the index of the last character of the start sequence, while
        the reverse trie is used to search for the index of the first character of the end sequence. A 
        reversed trie is used because by reversing the DNA sequence and the end sequence, the search method
        can then be used to find the index of the end sequence in the reverse trie. Then only, the index is 
        subtracted from the length of the DNA sequence to get the start index of the end sequence. 

        With these indices, they can be used to check overlap, by comparing the indices of the start and end
        sequences. If there is no overlap, the substring is then constructed by iterating through the DNA 
        sequence with the stored index. The substrings are then appended to the result list, and returned at
        the end.

        Additional checks are being done inside the main iterations, where in the inner loop, after the 
        construction of the substring is done, a check is done to see if the next end index is less than or
        equal to the current start index. If it is, the loop is broken, this is done because there is no need
        to continue the loop when the next iteration will be an overlap. When this overlap already happens, the 
        rest of the substrings in that inner loop will also be overlapping, so it is not necessary to continue
        the loop. The same is done for the outer loop, where if the next start index is greater than or equal
        to the first end index, the loop is broken. This is done to optimize the time complexity, and to avoid
        unnecessary iterations. This is done to make sure that the time complexity does not exceed the capacity
        of the total number of characters in all the substrings to output, because unnecessary iterations will
        be avoided.

        Early terminations are also done where firstly, if the start or end sequence does not exist in the trie,
        an empty list is returned. Secondly, if the start and end indices immediately overlap, an empty list is
        returned. This is done to make sure that the time complexity is optimized, and the function does not
        run uneccessary loops when the start and end sequences do not exist, or when they overlap.

        Input:
            start: The start prefix of the genome
            end: The end prefix of the genome

        Return:
            result: A list of all substrings of the DNA that contain the start and end prefixes.

        Time complexity:
            Complexity: O(T + U + V), where T is the length of the start sequence, U is the 
                        length of the end sequence, and V is the number of characters to be output.
            Analysis: The complexity of T is achieved by searching for the start sequence in the forward trie, 
                      U is achieved by searching for the end sequence in the reverse trie. Constructing each 
                      substring is dependent on the distance between the indices of the start and end points 
                      found in the tries. Thus, the V is achieved by iterating through the start and end indices, 
                      and constructing the substrings based on the indices. So, V can be considered as the number 
                      of characters to be output. This can be O(1) when the start or end indice does not exist, 
                      or when they overlap. However, in the worst case, V can be O(n^2) when the start and end 
                      indices are from the beginning to the end of the DNA sequence. The construction of the 
                      substring will take O(n^2) time complexity.

        Space complexity:
            Complexity: O(V), where V is the number of characters to be output.
            Analysis: The space complexity is linearly V because it only stores the substrings that are being
                      constructed. The primary variable that dynamically scales in space is result, which 
                      stores all the substrings found. Each substring can potentially be as long as the 
                      difference between the start index and the end index, contributing a variable length 
                      of characters. The temporary initializations of substring that is used to construct
                      the substrings are not considered in the space complexity because, at any given point, 
                      it would be proportional to the length of the longest substring being processed, but 
                      since these substrings are immediately converted to strings and not stored simultaneously, 
                      they do not add cumulatively to the space complexity.

        Input space complexity:
            Complexity: O(T + U), where T is the length of the start sequence, and U is the length of the end 
                        sequence.
            Analysis: The input space complexity is linear because it only takes the start and end sequences 
                      as input.
        """

        # Space complexity: O(1), because this only stores a node for the start sequence
        # Time complexity: O(T), where T is the length of the start sequence
        # Using the search method to search for the start sequence in the forward trie
        start_node = self.search(self.forward_trie_root, start)

        # Space complexity: O(1), because this only stores a node for the end sequence
        # Time complexity: O(U), where U is the length of the end sequence
        # Reverse the sequence of the DNA to be used for searching in the reverse trie
        # Using the search method to search for the end sequence in the reverse trie
        reversed_end = ''.join(reversed(end))
        end_node = self.search(self.reverse_trie_root, reversed_end)

        # Space complexity: O(V), where V is the number of characters to be output
        # Initialize the result list
        result = []

        # Early termination: if the start or end sequence does not exist in the trie, return empty list
        if start_node is None or end_node is None:
            return result

        # Space complexity: O(1), because this only stores the indices that is referenced from the node
        # Get the start and end indices of the start and end sequences from the trie payloads
        start_end_indices = start_node.end_indices
        end_end_indices = end_node.end_indices

        # Time complexity: O(U), where U is the length of the end sequence
        # Get the start indices of the end sequence by subtracting the end indices from the length of the DNA
        end_start_indices = []
        for end_end_index in end_end_indices:
            end_start_index = len(self.dna) - end_end_index - 1
            end_start_indices.append(end_start_index)

        # Early termination: if the start and end indices immediately overlap, return empty list
        if start_end_indices[0] >= end_start_indices[0]:
            return result

        # Time complexity: O(V), where V is the number of characters to be output
        # Iterate through the start and end indices to find the substrings
        for each_start in range(len(start_end_indices)):
            for each_end in range(len(end_start_indices)):
                
                start_end_index = start_end_indices[each_start]
                end_start_index = end_start_indices[each_end]

                # If overlap, break immediately, otherwise, construct the substring
                if start_end_index < end_start_index:
                    substring = []

                    # Interation to get the substring through the indices and pointers
                    for i in range(start_end_index - len(start) + 1, end_start_index + len(end)):
                        substring.append(self.dna[i])

                    # When the substring is formed, join and append it to the result list
                    result.append(''.join(substring))

                    # Break the loop if the next end index is greater than the or equal to the current start index
                    if each_end + 1 < len(end_start_indices):
                        if end_start_indices[each_end + 1] <= start_end_index:
                            break

            # Break the loop if the next starting index is greater than the or equal to the first end index
            if each_start + 1 < len(start_end_indices):
                if start_end_indices[each_start + 1] >= end_start_indices[0]:
                    break

        return result