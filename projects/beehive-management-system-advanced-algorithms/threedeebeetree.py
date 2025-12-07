from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    oct1: BeeNode|None = None
    oct2: BeeNode|None = None
    oct3: BeeNode|None = None
    oct4: BeeNode|None = None
    oct5: BeeNode|None = None
    oct6: BeeNode|None = None
    oct7: BeeNode|None = None
    oct8: BeeNode|None = None

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
        Returns the child node depending on the key and the octant it resides in.

        Args:
        - point (Point): the coordinate of the node to find the child node

        Returns:
        - child_node (BeeNode | Node): the would be child node for point, is None if the there is no child node for point

        Raises:
        - None

        Complexity:
        WCS: O(1), where the function returns the child node of the point.
        BCS: O(1), same with WCS.
        """
        if point[0] >= self.key[0] and point[1] >= self.key[1] and point[2] >= self.key[2]: # O(1)
            return self.oct1 # O(1)
        elif point[0] < self.key[0] and point[1] >= self.key[1] and point[2] >= self.key[2]: # O(1)
            return self.oct2 # O(1)
        elif point[0] < self.key[0] and point[1] < self.key[1] and point[2] >= self.key[2]: # O(1)
            return self.oct3 # O(1)
        elif point[0] >= self.key[0] and point[1] < self.key[1] and point[2] >= self.key[2]: # O(1)
            return self.oct4 # O(1)
        elif point[0] >= self.key[0] and point[1] >= self.key[1] and point[2] < self.key[2]: # O(1)
            return self.oct5 # O(1)
        elif point[0] < self.key[0] and point[1] >= self.key[1] and point[2] < self.key[2]: # O(1)
            return self.oct6 # O(1)
        elif point[0] < self.key[0] and point[1] < self.key[1] and point[2] < self.key[2]: # O(1)
            return self.oct7 # O(1)
        elif point[0] >= self.key[0] and point[1] < self.key[1] and point[2] < self.key[2]: # O(1)
            return self.oct8 # O(1)
            
class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None 
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
            Attempts to find the node in the threedeebeetree using the key.

            Args:
            - key (Point): the coordinates of the node to find in the tree

            Returns:
            - node (BeeNode): the node in the tree containing the key given 

            Raises:
            - KeyError : when the node is not found in the tree

            Complexity:
            - WCS: O(n)*Comp, where n is the depth of the octant, so traversal is done n times to find the node
                   that is at the leaf of the octant. Comp is the complexity of the comparison operator.
            - BCS: O(1)*Comp, which occurs when the element to be looked is the root node. Comp is the complexity 
                   of the comparison operator.
        """
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode :
        """
            Attempts to find the node in the threedeebeetree using the key.

            Args:
            - current: the current node the function is comparing the key to
            - key (Point): the coordinates of the node to find in the tree

            Returns:
            - node (BeeNode): the node in the tree containing the key given 

            Raises:
            - KeyError : when the node is not found in the tree

            Complexity:
            - WCS: O(n)*Comp, where n is the depth of the octant, so traversal is done n times to find the node
                   that is at the leaf of the octant. Comp is the complexity of the comparison operator.
            - BCS: O(1)*Comp, which occurs when the element to be looked is the root node. Comp is the complexity 
                   of the comparison operator.
        """
        if current is None :
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key :
            return current
        elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct1, key) # O(n)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct2, key) # O(n)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct3, key) # O(n)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct4, key) # O(n)
        elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct5, key) # O(n)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct6, key) # O(n)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct7, key) # O(n)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]: # O(1)
            return self.get_tree_node_by_key_aux(current.oct8, key) # O(1)

    def __setitem__(self, key: Point, item: I) -> None:
        """
            Attempts to insert an item into the tree, it uses the Key to locate the location to insert

            Args:
            - current (BeeNode): the current node the function is comparing the key to 
            - key (Point): The key or coordinate of the item to be insterted
            - item (item): the item to be inserted into the tree

            Returns: 
            - current (BeeNode): the parent node the new node should be linked to

            Raises:
            - ValueError: error is raised when the key already exists in the tree

            Complexity:
            - WCS: O(n)*Comp, where n is the depth of the octant, which occurs when item is inserted at the leaf of 
                   the octant, so traversal is done all the way from the root to the leaf, and comp is the complexity 
                   of the comparison operators. 
            - BCS: O(n)*Comp, same as WCS
        """
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to locate the location to insert

            Args:
            - current (BeeNode): the current node the function is comparing the key to 
            - key (Point): The key or coordinate of the item to be insterted
            - item (item): the item to be inserted into the tree

            Returns: 
            - current (BeeNode): the parent node the new node should be linked to

            Raises:
            - ValueError: error is raised when the key already exists in the tree

            Complexity:
            - WCS: O(n)*Comp, where n is the depth of the octant, which occurs when item is inserted at the leaf of 
                   the octant, so traversal is done all the way from the root to the leaf, and comp is the complexity 
                   of the comparison operators. 
            - BCS: O(n)*Comp, same as WCS
        """
        if current is None : # O(1)
            current = BeeNode(key, item=item, subtree_size=0) # O(1)
            self.length += 1 # O(1)
            current.subtree_size += 1 # O(1)
        elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]: # O(1)
            current.oct1 = self.insert_aux(current.oct1, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]: # O(1)
            current.oct2 = self.insert_aux(current.oct2, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]: # O(1)
            current.oct3 = self.insert_aux(current.oct3, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]: # O(1)
            current.oct4 = self.insert_aux(current.oct4, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]: # O(1)
            current.oct5 = self.insert_aux(current.oct5, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]: # O(1)
            current.oct6 = self.insert_aux(current.oct6, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]: # O(1)
            current.oct7 = self.insert_aux(current.oct7, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]: # O(1)
            current.oct8 = self.insert_aux(current.oct8, key, item) # O(n)
            current.subtree_size += 1 # O(1)
        else : # O(1)
            raise ValueError('Inserting duplicate item') # O(1)
            
        return current # O(1)
    

    def is_leaf(self, current: BeeNode) -> bool:
        """ 
            Simple check whether or not the node is a leaf. 
        
            Args:
            - current: the node to be checked

            Returns:
            - bool: the function returns true when the node is a leaf node, and false if the node is not a leaf node

            Raises:
            - None

            Complexity:
            - WCS: O(Comp), where the function checks if all the octants of the current node is none. Comp is the
                   complexity of the comparison operators.
            - BCS: O(Comp), same with WCS
        """
        return ((current.oct1 == None) and 
                (current.oct2 == None) and 
                (current.oct3 == None) and 
                (current.oct4 == None) and 
                (current.oct5 == None) and 
                (current.oct6 == None) and 
                (current.oct7 == None) and 
                (current.oct8 == None))
            

if __name__ == "__main__":
    pass
