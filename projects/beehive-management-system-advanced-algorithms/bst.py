""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""


from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from node import TreeNode
import sys


# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: K) -> bool:
        """
            Checks to see if the key is in the BST
            :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
            :complexity best: O(CompK) finds the item in the root of the tree
            :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item, subtree_size=0)
            self.length += 1
            current.subtree_size += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
            current.subtree_size += 1
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item) 
            current.subtree_size += 1
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def __delitem__(self, key: K) -> None:
        """
            Deletes an item from the tree
        """
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
        """

        if current is None:  # key not found 
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key) #O(n)
            current.subtree_size -= 1
        elif key > current.key:
            current.right = self.delete_aux(current.right, key) #O(n)
            current.subtree_size -= 1
        else:  # we found our key => do actual deletion
            current.subtree_size -= 1
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
            Get successor of the current node.
            It should be a child node having the smallest key among all the
            larger keys.

            Args:
            - current (TreeNode): the node in the bst to find the successor from

            Returns:
            - successor (TreeNode): the succesor of current, the node containing the smallest value that is larger than current

            Raises:
            - None

            Complexity:
            - WCS: O(N) where N is the number of left child in the subtree of the right child of current node, which 
              occurs when traversal is done N times until the leftmost child of the right child of current is reached.
            - BCS: O(1), which occurs when the current node has no right child, so no traversing needed.
        """
        if current is None or current.right is None: # O(1)
            return None # O(1)
        return self.get_minimal(current.right) #O(n)

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
            Get a node having the smallest key in the current sub-tree.

            Args:
            - current (TreeNode): The node to find the minimal value from

            Returns:
            - minimal (TreeNode): The node containing the minimal vlaue in the subtree of current

            Raises:
            - None

            :complexity:
            - WCS: O(N) where N is the number of left child in the subtree of current node. which occurs when traversal
              is done N times until the leftmost node is reached. 
            - BCS: O(1) when the current node is the minimal value, and has no left child, so no traversing needed.
        """
        if current.left: # O(1)
            return self.get_minimal(current.left) # O(n)
        return current # O(1)
        

    def is_leaf(self, current: TreeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)

    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
            Finds the kth smallest value by key in the subtree rooted at current.

            Args:
            - k (int): the number k smallest value in the subtree of current
            - current (TreeNode): the node to find the kth smallest element in subtree of current

            Returns:
            - k_smallest_node (TreeNode): the kth smallest node in the subtree of current

            Raises:
            - None

            Complexity:
            - WCS: O(D), where D is the maximum depth of the subtree of current.
            - BCS: O(1), where the current node is the kth smallest node.
        """
            
        return self.kth_smallest_aux(k, current, 1, current.subtree_size) # O(D)
    
    def kth_smallest_aux(self, k: int, current: TreeNode, start: int, end: int) -> TreeNode:
        """
            The auxillary function of kth_smallest

            Args:
            - k (int): the number k smallest value in the subtree of current
            - current (TreeNode): the node to find the kth smallest element in subtree of current
            - start (int): the starting position value
            - end (int): the end position value

            Returns:
            - k_smallest_node (TreeNode): the kth smallest node in the subtree of current

            Raises:
            - None

            Complexity: 
            - WCS: O(D), where D is the maximum depth of the subtree of current.
            - BCS: O(1), where the current node is the kth smallest node.
        """
        if current is None : # O(1)
            return # O(1)
        
        if current.left is None : # O(1)
            position = start # (1)
        else : # O(1)
            position = current.left.subtree_size + start # O(1)

        if k == position : # O(1)
            return current # O(1)
        elif k > position : # O(1)
            return self.kth_smallest_aux(k, current.right, (position + 1), end) # O(depth)
        elif k < position : # O(1)
            return self.kth_smallest_aux(k, current.left, start, (position - 1)) # O(depth)

if __name__ == "__main__" :
    pass
