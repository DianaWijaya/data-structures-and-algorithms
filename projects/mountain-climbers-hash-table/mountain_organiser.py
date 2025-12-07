from __future__ import annotations

from mountain import Mountain

from algorithms.mergesort import mergesort
from algorithms.binary_search import binary_search

class MountainOrganiser:
    def __init__(self) -> None:
        """
        Initialises an empty list for MountainOrganiser that stores the organized list of mountains.

        Args:
        - None

        Returns: 
        - None

        Complexity:
        - Worst case: O(1), which is the initialization of an empty list for organized_mountains.
        - Best case: O(1), which is the initialization of an empty list for organized_mountains.
        """

        # Initialize a list to store the organized mountains
        self.organized_mountains = [] # O(1)

    def add_mountains(self, mountains: list[Mountain]) -> None:
        """
        Adds a list of mountains to the organiser and organises the list according to the difficulty of each mountain.

        Args:
        - mountains: list of all the mountains to be added and sorted

        Returns:
        - None

        Complexity:
        - Worst case: O(NlogN + M), where n is the number of elements in the array, M is the number of mountains in the mountains list
          and comp(T) is the complexity of the comparison, in this case is considered O(1), because it is unrelated to the input size 
          of the mountain list. 
          This occurs when the mergesort function is called. 
        - Best case: O(NlogN + M), where n is the number of elements in the array, M is the number of mountains in the mountains list
          and comp(T) is the complexity of the comparison, in this case is considered O(1), because it is unrelated to the input size 
          of the mountain list. This occurs when the mergesort function is called. 
        """

        # Loops through all the mountain in the list and append the mountain into the initialized list
        for mountain in mountains : # O(n)
            self.organized_mountains.append(mountain) # O(1)

        # Sort the list of mountains
        self.organized_mountains = mergesort(self.organized_mountains)  # O(NlogN)

    def cur_position(self, mountain: Mountain) -> int:
        """
        Finds the rank of the provided mountain given all mountains included so far. KeyError is raised if the mountain 
        does not exist.

        Args:
        - mountain: the mountain that is provided to be used to find the rank with

        Returns:
        - rank: an integer value of the rank of the given mountain, if it exists in the list

        Raises:
        - KeyError: when the provided mountain does not exist in the list

        Complexity:
        - Worst case: O(log(n)), where n is the length of the list l, which occurs when the function _binary_search_aux is 
          called.
        - Best case: O(log(n)), where n is the length of the list l, which occurs when the function _binary_search_aux is 
          called.
        """

        rank = binary_search(self.organized_mountains, mountain) # O(log(n))

        try : # O(1)
            found_mountain = self.organized_mountains[rank] # O(1)
            if mountain == found_mountain : # O(1)
              return rank # O(1)
            else : # O(1)
              raise KeyError("Element not found in the list") # O(1)
        except : # O(1)
            raise KeyError("Element not found in the list") # O(1)

if __name__ == "__main__" :
    pass
    

    