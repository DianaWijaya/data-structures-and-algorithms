from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil, floor
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
            Initiates an empty binary search tree

            Arg:
            - None

            Returns:
            - None

            Raises:
            - None

            Complexity:
            - WCS: O(1), for the initialization of a Binary Search Tree
            - BCS: O(1), same as WCS
        """
        self.binary_search_tree = BinarySearchTree() # O(1)
    
    def add_point(self, item: T) -> None:
        """
            Adds a point into the bst

            Arg:
            - item: The item to be added into the BST

            Returns:
            - None

            Raises:
            - None

            Complexity:
            WCS: O(log N)*comp, where log n is the depth of the bst, occurs when item to be added is at a leaf node,
                 so traversal is done all the way from the root to the leaf node, and comp is the complexity of the
                 comparison operator.
            BCS: O(log N)*comp, same as WCS.
        """
        self.binary_search_tree[item] = item # O(log n)
    
    def remove_point(self, item: T) -> None:
        """
            removes a node from the bst

            Arg:
            - item: The item to be deleted into the BST

            Returns:
            - None

            Raises:
            - None

            Complexity:
            WCS: O(log N)*comp, where log n is the depth of the bst, occurs when item to be deleted is at a leaf node,
                 or the node does not exist. Traversal is done all the way from the root to the leaf node, and comp is
                 the complexity of the comparison operator.
            BCS: O(1)*comp, occurs when item to be deleted is at the root, and comp is the complexity of the comparison 
                 operator.
        """
        del self.binary_search_tree[item] # O(log n)

    def ratio(self, x, y) -> list[T]:
        """
            Computes a list of all items fitting the larger than/smaller than criteria

            Arg:
            - x: values have to be larger than  this % of the elements in the list
            - y: values have to be smaller than this % of the elements in the list

            Returns:
            - None

            Raises:
            - None

            Complexity:
            WCS: O(log N + O), where log N is the depth of the bst, and O is the number of elements in the ratio_list. occurs when 
                 the function traverses through the bst, returning a list of elements that are larger than x% of all the elements 
                 and smaller than y% of all the elements.
            BCS: O(log N + O), same as WCS
        """
        num_of_elements = len(self.binary_search_tree) # O(1)
        x_percentile = ceil(num_of_elements * x / 100) # O(1)
        y_percentile = floor(num_of_elements * (100 - y) / 100) # O(1)

        ratio_list = [] # O(1)
        ratio_list.append(self.binary_search_tree.kth_smallest(x_percentile+1, self.binary_search_tree.root).key) # O(log N)

        if x_percentile <= y_percentile: # O(1)
            self.ratio_aux(self.binary_search_tree.root, 0, x_percentile, y_percentile, ratio_list)

        return ratio_list # O(1)

    def ratio_aux(self, current: TreeNode, start: int, x_percentile: int, y_percentile: int, ratio_list: list) -> None:
        """
            auxillary function for ratio

            Arg:
            - current: the node to start 
            - start: the index of the current value 
            - x_percentile: the index of the value has to be higher than this index
            - y_percentile: the index of the value has to be lower than this index
            - ratio_list: the list containing values between the x_percentile and y_percentile of all the elements

            Returns:
            - None

            Raises:
            - None

            Complexity:
            WCS: O(O), where O is the total number of elements in the ratio_list 
            BCS: O(O), same as WCS
        """
        if current is None: # O(1)
            return # O(1)

        if current.left is None : # O(1)
            position = start # O(1)
        else : # O(1)
            position = current.left.subtree_size + start # O(1)

        self.ratio_aux(current.left, start, x_percentile, y_percentile, ratio_list) # O(n)

        if (x_percentile < position) and (y_percentile > position): # O(1)
            ratio_list.append(current.key) # O(1)
        if y_percentile >= position : # O(1)
            self.ratio_aux(current.right, (position + 1), x_percentile, y_percentile, ratio_list) # O(n)


if __name__ == "__main__":
    pass
