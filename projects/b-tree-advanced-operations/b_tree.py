import random
import sys

class Node:
    """
    This class represents a node in a B-tree.
    """
    def __init__(self, t, is_leaf):
        """
        Initializes a node with the given the minimum degree T and the leaf boolean.
        """
        self.t = t
        self.children = []
        self.node_keys = []
        self.is_leaf = is_leaf
        self.subtree_size = []
        self.min_key = []
        self.max_key = []

    def is_lower_bound(self):
        """
        This function is used to check if the number of elements in this node is t - 1.
        """
        return len(self.node_keys) == (self.t - 1)

    def is_upper_bound(self):
        """
        This function is used to check if the number of elements in this node is 2t - 1.
        """
        return len(self.node_keys) == ((2 * self.t) - 1)

    def count_node_keys(self):
        """
        This function returns the number of keys in this node.
        """
        return len(self.node_keys)

    def count_children(self):
        """
        This function returns the number of children in this node.
        """
        return len(self.children)


class BTree:
    """
    This class represents a B-tree of a minimum degree of T, with the insert, delete, search operations.
    It also contains methods for inorder traversal, select, rank, keysInRange, and primesInRange
    for this assignment purposes.
    """
    def __init__(self, t):
        """
        Initializes a B-tree with the given T value for the minimum degree
        """
        self.root = Node(t, True)
        self.t = t

    def search(self, node, k):
        """
        Searches for the key k in the subtree rooted at node

        Args:
            node (Node): The node from which to start the search
            k (int): The key to search for

        Returns:
            tuple: (node, index) if found, where node is the Node object and index is the key's position
            None: if the key is not found
        """
        i, _ = self.binary_search(node, k)

        # If the key is found in the current node, return the node and index
        if i < len(node.node_keys) and node.node_keys[i] == k:
            return (node, i)

        # If the key is not found and this is a leaf node, return None
        if node.is_leaf:
            return None

        # Recursively search down the child
        return self.search(node.children[i], k)

    def binary_search(self, node, search_value):
        """
        Helper method to perform binary search for search_value in the node's keys

        Args:
            node (Node): The node whose keys to search
            search_value (int): The key to locate

        Returns:
            tuple: (index, found) where index is the position where the key is or should be inserted and
                   found is a boolean that indicates True if the key is found, False otherwise
        """
        start = 0
        end = len(node.node_keys) - 1

        # Perform binary search
        while start <= end:
            mid = (start + end) // 2

            if node.node_keys[mid] == search_value:
                return mid, True
            elif node.node_keys[mid] < search_value:
                start = mid + 1
            else:
                end = mid - 1

        return start, False

    def _get_subtree_min(self, node):
        """
        Gets the minimum key in the subtree rooted at the given node

        Args:
            node (Node): The root of the subtree for which to find the minimum key

        Returns:
            int / float: The minimum key value in the subtree
        """

        # If the node is a leaf, return the first key
        if node.is_leaf:
            return node.node_keys[0]

        # For internal nodes, use min_key if available for the leftmost child
        if node.min_key and len(node.min_key) > 0:
            leftmost_child_min = node.min_key[0]
            if node.node_keys:
                return min(leftmost_child_min, node.node_keys[0])
            return leftmost_child_min

        # Return the first key if it exists
        return node.node_keys[0]

    def _get_subtree_max(self, node):
        """
        Gets the maximum key in the subtree rooted at the given node

        Args:
            node (Node): The root of the subtree for which to find the maximum key

        Returns:
            int / float: The maximum key value in the subtree
        """

        # If the node is a leaf, return the last key
        if node.is_leaf:
            return node.node_keys[-1]

        # For internal nodes, use max_key if available for the rightmost child
        if node.max_key and len(node.max_key) > 0:
            rightmost_child_max = node.max_key[-1]
            if node.node_keys:
                return max(rightmost_child_max, node.node_keys[-1])
            return rightmost_child_max

        # Return the last key if it exists
        return node.node_keys[-1]

    def insert(self, insert_value):
        """
        Inserts a new key into the B-tree, maintaining the B-tree properties
        If the key already exists in the tree, the operation does nothing

        Args:
            insert_value (int): The key to insert into the B-tree
        """

        # If the value already exists, do not insert
        if self.search(self.root, insert_value) is not None:
            return

        root = self.root

        # If the root is full, split it and create a new root
        if root.is_upper_bound():

            # Split median and make this the parent of the two new nodes
            median_index = self.root.count_node_keys() // 2
            median_value = self.root.node_keys[median_index]

            # Create a new root and split the old root into left and right children
            split_root = Node(self.t, False)
            split_root.node_keys.append(median_value)

            # Left splitted node
            left_node = Node(self.t, root.is_leaf)
            left_node.node_keys = root.node_keys[0:median_index]

            # Right splitted node
            right_node = Node(self.t, root.is_leaf)
            right_node.node_keys = root.node_keys[median_index + 1:]

            # Reassign children if the root is not a leaf
            if root.is_leaf == False:
                median_child_index = self.root.count_children() // 2
                left_node.children = root.children[0:median_child_index]
                right_node.children = root.children[median_child_index:]

                # Copy the subtree sizes, min_key, and max_key
                left_node.subtree_size = root.subtree_size[0:median_child_index]
                right_node.subtree_size = root.subtree_size[median_child_index:]
                left_node.min_key = root.min_key[0:median_child_index]
                right_node.min_key = root.min_key[median_child_index:]
                left_node.max_key = root.max_key[0:median_child_index]
                right_node.max_key = root.max_key[median_child_index:]

            # Calculate the total keys in each child subtree
            left_total = len(left_node.node_keys) + sum(left_node.subtree_size)
            right_total = len(right_node.node_keys) + sum(right_node.subtree_size)

            # Calculate min and max for each child subtree
            left_min = self._get_subtree_min(left_node)
            left_max = self._get_subtree_max(left_node)
            right_min = self._get_subtree_min(right_node)
            right_max = self._get_subtree_max(right_node)

            # Set the children and subtree sizes, min_key, and max_key for the new root
            split_root.children = [left_node, right_node]
            split_root.subtree_size = [left_total, right_total]
            split_root.min_key = [left_min, right_min]
            split_root.max_key = [left_max, right_max]
            self.root = split_root

            # Continue insertion into the newly created root
            current = split_root

        else:
            current = root

        # Recursively insert the value into the appropriate child
        self.insert_helper(current, insert_value)

    def insert_helper(self, node, insert_value):
        """
        Helper function for insert. Recursively inserts a key into the correct node,
        handle node splits when necessary, and updates the parent node

        Args:
            node (Node): The current node to insert into
            insert_value (int): The key to insert
        """

        # If this is a leaf, just insert the value into the correct position
        if node.is_leaf:
            insert_pos, _ = self.binary_search(node, insert_value)
            node.node_keys.insert(insert_pos, insert_value)
            return

        # Find the child to recurse into
        value_index, _ = self.binary_search(node, insert_value)
        traversed_child = node.children[value_index]

        # If the child is full, split it
        if traversed_child.is_upper_bound():

            # Split median and make this the parent of the two new nodes
            median_index = traversed_child.count_node_keys() // 2
            median_value = traversed_child.node_keys[median_index]

            # Left splitted node
            left_node = Node(self.t, traversed_child.is_leaf)
            left_node.node_keys = traversed_child.node_keys[0:median_index]

            # Right splitted node
            right_node = Node(self.t, traversed_child.is_leaf)
            right_node.node_keys = traversed_child.node_keys[median_index + 1:]

            # Reassign children if the root is not a leaf
            if traversed_child.is_leaf == False:
                median_child_index = traversed_child.count_children() // 2
                left_node.children = traversed_child.children[0:median_child_index]
                right_node.children = traversed_child.children[median_child_index:]

                # Copy the subtree sizes, min_key, and max_key
                left_node.subtree_size = traversed_child.subtree_size[0:median_child_index]
                right_node.subtree_size = traversed_child.subtree_size[median_child_index:]
                left_node.min_key = traversed_child.min_key[0:median_child_index]
                right_node.min_key = traversed_child.min_key[median_child_index:]
                left_node.max_key = traversed_child.max_key[0:median_child_index]
                right_node.max_key = traversed_child.max_key[median_child_index:]

             # Calculate the total keys in each child subtree
            left_total = len(left_node.node_keys) + sum(left_node.subtree_size)
            right_total = len(right_node.node_keys) + sum(right_node.subtree_size)

            # Calculate min and max for each child subtree
            left_min = self._get_subtree_min(left_node)
            left_max = self._get_subtree_max(left_node)
            right_min = self._get_subtree_min(right_node)
            right_max = self._get_subtree_max(right_node)

            # Insert median into parent and update children
            node.node_keys.insert(value_index, median_value)
            node.children[value_index] = left_node
            node.children.insert(value_index + 1, right_node)

            # Update subtree sizes, min_key, and max_key for the parent node
            node.subtree_size[value_index] = left_total
            node.subtree_size.insert(value_index + 1, right_total)
            node.min_key[value_index] = left_min
            node.min_key.insert(value_index + 1, right_min)
            node.max_key[value_index] = left_max
            node.max_key.insert(value_index + 1, right_max)

            # Determine which child to continue with
            if insert_value > median_value:
                traversed_child = right_node
                value_index += 1
            else:
                traversed_child = left_node

        # Recursively insert into the appropriate child
        self.insert_helper(traversed_child, insert_value)

        # Update subtree size for the parent node
        node.subtree_size[value_index] += 1

        # Update min_key and max_key for the children
        child_min = self._get_subtree_min(node.children[value_index])
        child_max = self._get_subtree_max(node.children[value_index])
        node.min_key[value_index] = child_min
        node.max_key[value_index] = child_max

    def delete(self, delete_value):
        """
        Removes a key from the B-tree if it exists with the 3 main cases:
        Case 1: If the key is found in a leaf node, simply remove it.
        Case 2: If the key is found in an internal node:
            (a) If the left child has at least t keys, replace the key with its predecessor and recursively
                delete the predecessor.
            (b) If the right child has at least t keys, replace the key with its successor and recursively
                delete the successor.
            (c) If both children have t-1 keys, merge the key and both children, then recursively delete in the
                merged node.
        Case 3: If the key is not found in the current node, descend to the appropriate child and ensure that
                child has at least t keys by borrowing from a sibling or merging siblings if necessary.

        Args:
            delete_value (int): The key to be deleted from the tree
        """

        # If key is not found, do nothing
        if self.search(self.root, delete_value) is None:
            return

        # Recursively delete the key starting from the root
        self.delete_helper(self.root, delete_value)

    def delete_helper(self, node, delete_value):
        """
        Helper function to recursively delete a key from the tree

        Args:
            node (Node): The current node being examined
            delete_value (int): The key to be deleted
        """
        t = self.t
        value_index, found = self.binary_search(node, delete_value)

        # Case 1: Key is in a leaf node
        if node.is_leaf:

            # Simply remove the key if found if it's a leaf node
            if found:
                node.node_keys.pop(value_index)
            return

        # Case 2: Key in this (internal) node
        if found:
            left_child = node.children[value_index]
            right_child = node.children[value_index + 1]

            # Case 2a: If the left child has at least t elements, replace by predecessor
            if len(left_child.node_keys) >= t:

                # Find the predecessor (rightmost of left child)
                pred_value = self.get_rightmost(left_child)
                node.node_keys[value_index] = pred_value

                # Recursively delete the predecessor from the left child
                self.delete_helper(left_child, pred_value)

                # Decrement the subtree size for the left child
                node.subtree_size[value_index] -= 1

                # Update minimim and maximum for the left child
                child_min = self._get_subtree_min(left_child)
                child_max = self._get_subtree_max(left_child)
                node.min_key[value_index] = child_min
                node.max_key[value_index] = child_max

            # Case 2b: If the right child has at least t elements, replace by successor
            elif len(right_child.node_keys) >= t:

                # Find the successor (leftmost of right child)
                succ_value = self.get_leftmost(right_child)
                node.node_keys[value_index] = succ_value

                # Recursively delete the successor from the right child
                self.delete_helper(right_child, succ_value)

                # Decrement the subtree size for the right child
                node.subtree_size[value_index + 1] -= 1

                # Update minimim and maximum for the right child
                child_min = self._get_subtree_min(right_child)
                child_max = self._get_subtree_max(right_child)
                node.min_key[value_index + 1] = child_min
                node.max_key[value_index + 1] = child_max

            # Case 2c: If both children have t-1 elements, merge them and recursively delete it
            else:

                # Copy keys from left and right children, and include the parent separator key
                left_keys = left_child.node_keys[:]
                parent_key = node.node_keys[value_index]
                right_keys = right_child.node_keys[:]
                merged_keys = left_keys + [parent_key] + right_keys

                # Calculate merged children, subtree sizes, min_keys, and max_keys
                if left_child.is_leaf:
                    merged_children = []
                    merged_subtree_sizes = []
                    merged_min_keys = []
                    merged_max_keys = []
                else:
                    merged_children = left_child.children + right_child.children
                    merged_subtree_sizes = left_child.subtree_size + right_child.subtree_size
                    merged_min_keys = left_child.min_key + right_child.min_key
                    merged_max_keys = left_child.max_key + right_child.max_key

                # Create the merged node
                merged_node = Node(t, left_child.is_leaf)
                merged_node.node_keys = merged_keys

                # If the merged node is not a leaf, set its children and subtree sizes
                if merged_children:
                    merged_node.children = merged_children
                    merged_node.subtree_size = merged_subtree_sizes
                    merged_node.min_key = merged_min_keys
                    merged_node.max_key = merged_max_keys

                # Calculate the new subtree size for the merged node
                if merged_node.is_leaf:
                    new_subtree_size = len(merged_keys)
                else:
                    new_subtree_size = sum(merged_subtree_sizes) + len(merged_keys)

               # Update min and max keys for the merged node
                merged_min = self._get_subtree_min(merged_node)
                merged_max = self._get_subtree_max(merged_node)

                # Replace left_child with merged_node in parent, remove parent key and right_child
                node.children[value_index] = merged_node
                node.node_keys.pop(value_index)
                node.children.pop(value_index + 1)
                node.subtree_size[value_index] = new_subtree_size
                node.subtree_size.pop(value_index + 1)
                node.min_key[value_index] = merged_min
                node.min_key.pop(value_index + 1)
                node.max_key[value_index] = merged_max
                node.max_key.pop(value_index + 1)

                # Recursively continue deletion in the merged node
                self.delete_helper(merged_node, delete_value)
                node.subtree_size[value_index] -= 1

                # Update minimum and maximum after deletion
                updated_min = self._get_subtree_min(merged_node)
                updated_max = self._get_subtree_max(merged_node)
                node.min_key[value_index] = updated_min
                node.max_key[value_index] = updated_max

            return

        # Case 3: If the traversal is stopped because the subtree has t-1 keys
        target_child = node.children[value_index]
        if len(target_child.node_keys) == t - 1:

            # Determine the left sibling, if it exists
            if value_index > 0:
                left_sibling = node.children[value_index - 1]
            else:
                left_sibling = None

            # Determine the right sibling, if it exists
            if value_index < len(node.children) - 1:
                right_sibling = node.children[value_index + 1]
            else:
                right_sibling = None

            # Case 3a: Immediate LEFT sibling has at least t keys, rotate
            if left_sibling != None and len(left_sibling.node_keys) >= t:

                # Borrow the rightmost key from the left sibling
                borrowed_value = left_sibling.node_keys[-1]
                updated_keys = [node.node_keys[value_index - 1]] + target_child.node_keys
                node.node_keys[value_index - 1] = borrowed_value
                left_sibling_values = left_sibling.node_keys[:-1]

                # If nodes are internal, transfer rightmost child from left sibling to target child
                if left_sibling.is_leaf == False:
                    new_children = [left_sibling.children[-1]] + target_child.children
                    left_sibling_children = left_sibling.children[:-1]

                    # Move subtree size from left sibling to target child
                    borrowed_subtree_size = left_sibling.subtree_size[-1]
                    target_child.subtree_size = [borrowed_subtree_size] + target_child.subtree_size
                    left_sibling.subtree_size = left_sibling.subtree_size[:-1]

                    # Move minimum and maximum keys from left sibling to target child
                    borrowed_min = left_sibling.min_key[-1]
                    borrowed_max = left_sibling.max_key[-1]
                    target_child.min_key = [borrowed_min] + target_child.min_key
                    target_child.max_key = [borrowed_max] + target_child.max_key
                    left_sibling.min_key = left_sibling.min_key[:-1]
                    left_sibling.max_key = left_sibling.max_key[:-1]

                    # Update parent's subtree sizes
                    node.subtree_size[value_index - 1] -= (borrowed_subtree_size + 1)
                    node.subtree_size[value_index] += (borrowed_subtree_size + 1)

                # If nodes are leaves, just update the keys and children
                else:
                    new_children = target_child.children
                    left_sibling_children = []
                    node.subtree_size[value_index - 1] -= 1
                    node.subtree_size[value_index] += 1

                # Apply the changes to both siblings
                left_sibling.node_keys = left_sibling_values
                left_sibling.children = left_sibling_children
                target_child.node_keys = updated_keys
                target_child.children = new_children

                # Update minimum and maximum values for both siblings in parent
                left_min = self._get_subtree_min(left_sibling)
                left_max = self._get_subtree_max(left_sibling)
                target_min = self._get_subtree_min(target_child)
                target_max = self._get_subtree_max(target_child)
                node.min_key[value_index - 1] = left_min
                node.max_key[value_index - 1] = left_max
                node.min_key[value_index] = target_min
                node.max_key[value_index] = target_max

            # Case 3a: Immediate RIGHT sibling has at least t keys, rotate
            elif right_sibling != None and len(right_sibling.node_keys) >= t:

                # Borrow the leftmost key from the right sibling
                borrowed_value = right_sibling.node_keys[0]
                updated_keys = target_child.node_keys + [node.node_keys[value_index]]
                node.node_keys[value_index] = borrowed_value
                right_sibling_values = right_sibling.node_keys[1:]

                # If nodes are internal, transfer leftmost child from right sibling to target child
                if right_sibling.is_leaf == False:
                    new_children = target_child.children + [right_sibling.children[0]]
                    right_sibling_children = right_sibling.children[1:]

                    # Move subtree size from right sibling to target child
                    borrowed_subtree_size = right_sibling.subtree_size[0]
                    target_child.subtree_size = target_child.subtree_size + [borrowed_subtree_size]
                    right_sibling.subtree_size = right_sibling.subtree_size[1:]

                    # Move minimum and maximum keys from right sibling to target child
                    borrowed_min = right_sibling.min_key[0]
                    borrowed_max = right_sibling.max_key[0]
                    target_child.min_key = target_child.min_key + [borrowed_min]
                    target_child.max_key = target_child.max_key + [borrowed_max]
                    right_sibling.min_key = right_sibling.min_key[1:]
                    right_sibling.max_key = right_sibling.max_key[1:]

                    # Update parent's subtree sizes
                    node.subtree_size[value_index] += (borrowed_subtree_size + 1)
                    node.subtree_size[value_index + 1] -= (borrowed_subtree_size + 1)

                # If nodes are leaves, just update the keys and children
                else:
                    new_children = target_child.children
                    right_sibling_children = []
                    node.subtree_size[value_index] += 1
                    node.subtree_size[value_index + 1] -= 1

                # Apply the changes to both siblings
                target_child.node_keys = updated_keys
                target_child.children = new_children
                right_sibling.node_keys = right_sibling_values
                right_sibling.children = right_sibling_children

                # Update minimum and maximum values for both siblings in parent
                target_min = self._get_subtree_min(target_child)
                target_max = self._get_subtree_max(target_child)
                right_min = self._get_subtree_min(right_sibling)
                right_max = self._get_subtree_max(right_sibling)
                node.min_key[value_index] = target_min
                node.max_key[value_index] = target_max
                node.min_key[value_index + 1] = right_min
                node.max_key[value_index + 1] = right_max

            # Case 3b: Immediate sibling has exactly t - 1 keys, merge with sibling
            else:

                # Case 3b: Merge with left sibling
                if left_sibling != None and left_sibling.is_lower_bound():

                    # Combine left sibling's keys, parent's separator key, and target_child's keys
                    merged_keys = left_sibling.node_keys + [node.node_keys[value_index - 1]] + target_child.node_keys

                    # If the target child is a leaf, we do not need children
                    if left_sibling.is_leaf:
                        merged_children = []
                        merged_subtree_sizes = []
                        merged_min_keys = []
                        merged_max_keys = []

                    # For internal nodes, merge children
                    else:
                        merged_children = left_sibling.children + target_child.children
                        merged_subtree_sizes = left_sibling.subtree_size + target_child.subtree_size
                        merged_min_keys = left_sibling.min_key + target_child.min_key
                        merged_max_keys = left_sibling.max_key + target_child.max_key

                    # Create a new merged node
                    merged_node = Node(t, left_sibling.is_leaf)
                    merged_node.node_keys = merged_keys

                    # If the merged node is not a leaf, set its children and subtree sizes
                    if merged_children:
                        merged_node.children = merged_children
                        merged_node.subtree_size = merged_subtree_sizes
                        merged_node.min_key = merged_min_keys
                        merged_node.max_key = merged_max_keys

                    # Recalculate the total subtree size for the merged node
                    if merged_node.is_leaf:
                        new_subtree_size = len(merged_keys)
                    else:
                        new_subtree_size = sum(merged_subtree_sizes) + len(merged_keys)

                    # Update min and max keys for the merged node
                    merged_min = self._get_subtree_min(merged_node)
                    merged_max = self._get_subtree_max(merged_node)

                    # Replace the left sibling with merged node, remove the parent separator and target_child
                    node.children[value_index - 1] = merged_node
                    node.node_keys.pop(value_index - 1)
                    node.children.pop(value_index)
                    node.subtree_size[value_index - 1] = new_subtree_size
                    node.subtree_size.pop(value_index)
                    node.min_key[value_index - 1] = merged_min
                    node.min_key.pop(value_index)
                    node.max_key[value_index - 1] = merged_max
                    node.max_key.pop(value_index)

                    # After merge, continue deletion in the merged node
                    target_child = merged_node
                    value_index = value_index - 1

                # Case 3b: Merge with right sibling
                elif right_sibling != None and right_sibling.is_lower_bound():

                    # Combine right sibling's keys, parent's separator key, and target_child's keys
                    merged_keys = target_child.node_keys + [node.node_keys[value_index]] + right_sibling.node_keys

                    # For leaves, there are no children to combine
                    if target_child.is_leaf:
                        merged_children = []
                        merged_subtree_sizes = []
                        merged_min_keys = []
                        merged_max_keys = []

                    # For internal nodes, merge children
                    else:
                        merged_children = target_child.children + right_sibling.children
                        merged_subtree_sizes = target_child.subtree_size + right_sibling.subtree_size
                        merged_min_keys = target_child.min_key + right_sibling.min_key
                        merged_max_keys = target_child.max_key + right_sibling.max_key

                    # Create a new merged node
                    merged_node = Node(t, target_child.is_leaf)
                    merged_node.node_keys = merged_keys

                    # If the merged node is not a leaf, set its children and subtree sizes
                    if merged_children:
                        merged_node.children = merged_children
                        merged_node.subtree_size = merged_subtree_sizes
                        merged_node.min_key = merged_min_keys
                        merged_node.max_key = merged_max_keys

                    # Recalculate the total subtree size for the merged node
                    if merged_node.is_leaf:
                        new_subtree_size = len(merged_keys)
                    else:
                        new_subtree_size = sum(merged_subtree_sizes) + len(merged_keys)

                    # Calculate min and max for the merged subtree
                    merged_min = self._get_subtree_min(merged_node)
                    merged_max = self._get_subtree_max(merged_node)

                    # Replace the right sibling with merged node, remove the parent separator and target_child
                    node.children[value_index] = merged_node
                    node.node_keys.pop(value_index)
                    node.children.pop(value_index + 1)
                    node.subtree_size[value_index] = new_subtree_size
                    node.subtree_size.pop(value_index + 1)
                    node.min_key[value_index] = merged_min
                    node.min_key.pop(value_index + 1)
                    node.max_key[value_index] = merged_max
                    node.max_key.pop(value_index + 1)
                    target_child = merged_node

        self.delete_helper(target_child, delete_value)

        # After merge and possible recursion, continue deleting the key from the merged node with recursion
        node.subtree_size[value_index] -= 1

        # Update min_key and max_key for the affected child
        child_min = self._get_subtree_min(node.children[value_index])
        child_max = self._get_subtree_max(node.children[value_index])
        node.min_key[value_index] = child_min
        node.max_key[value_index] = child_max

    def get_rightmost(self, node):
        """
        Recursively finds and returns the rightmost key in the subtree rooted at node

        Args:
            node (Node): The node from which to find the rightmost key

        Returns:
            int: The rightmost (largest) key in the subtree
        """
        if node.is_leaf:

            # Return the last key if the node is not empty
            return node.node_keys[-1]

        # Continue traversing to the rightmost child
        return self.get_rightmost(node.children[-1])

    def get_leftmost(self, node):
        """
        Recursively finds and returns the leftmost key in the subtree rooted at node

        Args:
            node (Node): The node from which to find the leftmost key

        Returns:
            int: The leftmost (smallest) key in the subtree
        """
        if node.is_leaf:

            # Return the first key if the node is not empty
            return node.node_keys[0]

        # Continue traversing to the leftmost child
        return self.get_leftmost(node.children[0])

    def select(self, k):
        """
        Returns the k-th smallest key in the current state of the B-tree (1-based index)
        If k is out of range, returns -1

        Args:
            k (int): The 1-based position of the key to find

        Returns:
            int: The k-th smallest key, or -1 if k is out of bounds
        """

        # Calculate the total number of keys in the B-tree
        if self.root.subtree_size:
            total = sum(self.root.subtree_size) + len(self.root.node_keys)
        else:
            total = len(self.root.node_keys)

        # If k is out of bounds, return -1
        if k < 1 or k > total:
            return -1

        # Recursively find the k-th smallest key
        return self.select_helper(self.root, k)

    def select_helper(self, node, k):
        """
        Recursively finds the k-th smallest key in the subtree rooted at node

        Args:
            node (Node): The current node being inspected
            k (int): The rank (1-based) of the key to find in this subtree

        Returns:
            int: The k-th smallest key, or -1 if k is out of range
        """
        for i in range(len(node.node_keys)):

            # Determine the size of the left subtree for the current key
            if node.subtree_size:
                left_size = node.subtree_size[i]
            else:
                left_size = 0

            # The k-th key is in the left subtree
            if k <= left_size:
                return self.select_helper(node.children[i], k)

            # The current key is the k-th smallest
            elif k == left_size + 1:
                return node.node_keys[i]

            # Skip left subtree and current key, decrement k accordingly
            else:
                k = k - (left_size + 1)

        # After looping through all keys, must check the rightmost child if it is present
        if node.subtree_size and len(node.children) > 0:
            return self.select_helper(node.children[-1], k)
        return -1

    def rank(self, x):
        """
        Returns the 1-based rank (sorted order) of key x in the B-tree
        If x does not exist in the tree, returns -1

        Args:
            x (int): The key whose rank is to be determined

        Returns:
            int: The rank of x, or -1 if x does not exist in the tree
        """
        return self.rank_helper(self.root, x, 0)

    def rank_helper(self, node, x, count_so_far):
        """
        Recursively computes the rank (number of keys <= x) in the subtree rooted at node
        Returns -1 if x is not found in the subtree

        Args:
            node (Node): The current node being searched
            x (int): The key whose rank is to be computed
            count_so_far (int): Accumulator for the number of keys less than x encountered so far

        Returns:
            int: The rank of x in the tree, or -1 if not found
        """
        i = 0

        # Count all keys and left subtrees with keys < x
        while i < len(node.node_keys) and x > node.node_keys[i]:
            if node.subtree_size:
                count_so_far += node.subtree_size[i] + 1
            else:
                count_so_far += 1
            i += 1

        # If current key matches x, add all left and self, then return
        if i < len(node.node_keys) and node.node_keys[i] == x:
            if node.subtree_size:
                count_so_far += node.subtree_size[i] + 1
            else:
                count_so_far += 1
            return count_so_far

        # If we reach a leaf and didn't find x, return -1
        if node.is_leaf:
            return -1

        # Continue recursively in the proper child
        return self.rank_helper(node.children[i], x, count_so_far)

    def keysInRange(self, x, y):
        """
        Returns a list of keys in the B-tree that are within the range [x, y]
        If no such keys exist, returns -1

        Args:
            x (int): The lower bound of the range
            y (int): The upper bound of the range

        Returns:
            list[int] or int: A list of keys within [x, y], or -1 if none are found
        """
        result = []

        # Start the recursive search for keys in the range
        self.keysInRange_helper(self.root, x, y, result)

        # If no keys found in the range, return -1
        if len(result) == 0:
            return -1
        return result

    def keysInRange_helper(self, node, x, y, result):
        """
        Recursively traverses the subtree rooted at 'node', adding all keys in [x, y] to result
        Uses min_key and max_key to efficiently skip subtrees outside the range

        Args:
            node (Node): The current node being examined
            x (int): The lower bound of the range
            y (int): The upper bound of the range
            result (list): The accumulator list for valid keys
        """
        i = 0
        while i < len(node.node_keys):

            # Traverse the i-th child if it's not a leaf, and only if its subtree overlaps [x, y]
            if not node.is_leaf and node.children:
                child = node.children[i]

                # If the entire subtree is less than x, skip it
                if node.max_key[i] is not None and node.max_key[i] < x:
                    pass

                # If the entire subtree is greater than y, skip it
                elif node.min_key[i] is not None and node.min_key[i] > y:
                    pass

                # If the subtree overlaps with [x, y], continue searching in it
                else:
                    self.keysInRange_helper(child, x, y, result)

            # Check the current key itself
            key = node.node_keys[i]
            if x <= key <= y:
                result.append(key)
            i += 1

        # Check the rightmost child if present for the final remaining child
        if not node.is_leaf and node.children:
            right_idx = len(node.children) - 1
            right_child = node.children[right_idx]

            # All keys too small, skip
            if node.max_key[right_idx] is not None and node.max_key[right_idx] < x:
                pass

            # All keys too large, skip
            elif node.min_key[right_idx] is not None and node.min_key[right_idx] > y:
                pass

            # If the right child overlaps with [x, y], continue searching in it
            else:
                self.keysInRange_helper(right_child, x, y, result)

    def primesInRange(self, x, y):
        """
        Returns a list of keys in the B-tree that are both within the range [x, y] (inclusive)
        and prime. If no such keys exist, returns -1

        Args:
            x (int): The lower bound of the range
            y (int): The upper bound of the range

        Returns:
            list[int] or int: A list of prime keys within [x, y], or -1 if none are found
        """

        # Get all keys in the range [x, y]
        keys_in_range = self.keysInRange(x, y)
        if keys_in_range == -1:
            return -1

        primes = []

        # Check each key in the range for primality
        for key in keys_in_range:
            if millerRabinRandomisedPrimality(key, 10):
                primes.append(key)

        # If no primes found, return -1
        if len(primes) == 0:
            return -1

        return primes

    def print_tree(self, node=None, level=0):
        """
        Recursively prints the structure of the B-tree starting from the specified node

        Args:
            node (Node, optional): The starting node for printing. Defaults to the root
            level (int, optional): The current depth level (used for indentation). Defaults to 0

        Returns:
            None
        """
        if node is None:
            node = self.root

        print("  " * level + f"Keys: {node.node_keys}")
        if not node.is_leaf:
            print("  " * level + f"Subtree sizes: {node.subtree_size}")
            print("  " * level + f"Min keys: {node.min_key}")
            print("  " * level + f"Max keys: {node.max_key}")

        for i, child in enumerate(node.children):
            print("  " * level + f"Child {i}:")
            self.print_tree(child, level + 1)

def modular_exponentiation(base, exponent, modulus):
    """
    Computes modulus using exponentiation by squaring

    Args:
        base (int): The base integer
        exponent (int): The exponent (non-negative integer)
        modulus (int): The modulus

    Returns:
        int: The result of (base ** exponent) % modulus
    """
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2

    return result

def millerRabinRandomisedPrimality(n, k):
    """
    Performs the Miller-Rabin probabilistic primality test on n, with k rounds

    Args:
        n (int): The integer to test for primality
        k (int): The number of random rounds to increase confidence

    Returns:
        bool: True if n is probably prime, False if n is composite
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    s = 0
    t = n - 1

    # Express n-1 as 2^s * t with t odd
    while t % 2 == 0:
        s = s + 1
        t = t // 2

    # Run k random tests
    for i in range(1, k):
        a = random.randrange(2, n - 1)

        x_s = modular_exponentiation(a, n - 1, n)

        if x_s != 1:
            return False

        # Run the sequence test
        for j in range(1, s + 1):
            x_j = modular_exponentiation(a, (2 ** j) * t, n)
            x_j_minus_1 = modular_exponentiation(a, (2 ** (j - 1)) * t, n)
            if x_j == 1 and (x_j_minus_1 != 1 and x_j_minus_1 != n - 1):
                return False

    # n has passed all tests so probably prime
    return True

def read_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python a3.py <t> <keystoinsert.txt> <keystodelete.txt> <commands.txt>")
        sys.exit(1)

    t = int(sys.argv[1])
    insert_file = sys.argv[2]
    delete_file = sys.argv[3]
    commands_file = sys.argv[4]
    output_file = "output_a3.txt"

    btree = BTree(t)

    # Insert keys
    for line in read_file(insert_file):
        line = line.strip()
        key = int(line)
        btree.insert(key)

    # Delete keys
    for line in read_file(delete_file):
        line = line.strip()
        key = int(line)
        btree.delete(key)

    # Process commands and write to output file
    commands = read_file(commands_file)
    with open(output_file, 'w') as out:
        for line in commands:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            command = parts[0]

            # Process select
            if command == "select":
                k = int(parts[1])
                result = btree.select(k)
                out.write(str(result) + "\n")

            # Process rank
            elif command == "rank":
                x = int(parts[1])
                result = btree.rank(x)
                out.write(str(result) + "\n")

            # Process keysInRange
            elif command == "keysInRange":
                x = int(parts[1])
                y = int(parts[2])
                keys = btree.keysInRange(x, y)
                if keys == -1:
                    out.write("-1\n")
                else:
                    out.write(" ".join([str(key) for key in keys]) + "\n")

            # Process primesInRange
            elif command == "primesInRange":
                x = int(parts[1])
                y = int(parts[2])
                keys = btree.primesInRange(x, y)
                if keys == -1:
                    out.write("-1\n")
                else:
                    out.write(" ".join([str(key) for key in keys]) + "\n")
