from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Mountain:

    name: str
    difficulty_level: int
    length: int

    def __lt__(self, compared_mountain: Mountain) -> bool:
        """
        Magic method for less than, when two mountains are compared. Length is to be compared first, then the 
        name is compared if the length is the same. This is assuming the name of each mountain is different.

        Args:
        - compared_mountain: The mountain to be compared to

        Returns:
        - boolean value representing if it is actually less than or not

        Complexity:
        - Worst case: O(comp(T)), for comparison done, which occurs when length is the same, resulting in the name to be
          compared
        - Best case: O(1), which occurs when the only the length is compared
        """
        if self.length == compared_mountain.length :
            return self.name < compared_mountain.name
        return self.length < compared_mountain.length
    
    def __le__(self, compared_mountain: Mountain) -> bool:
        """
        Magic method for less than or equal to, when two mountains are compared. Length is to be compared first, then the 
        name is compared if the length is the same. This is assuming the name of each mountain is different.

        Args:
        - compared_mountain: The mountain to be compared to

        Returns:
        - boolean value representing if it is actually less than or equal to or not

        Complexity:
        - Worst case: O(comp(T)), for comparison done, which occurs when length is the same, resulting in the name to be
          compared
        - Best case: O(1), which occurs when the only the length is compared
        """
        if self.length == compared_mountain.length :
            return self.name <= compared_mountain.name
        return self.length <= compared_mountain.length
    
    def __gt__(self, compared_mountain: Mountain) -> bool:
        """
        Magic method for greater than, when two mountains are compared. Length is to be compared first, then the 
        name is compared if the length is the same. This is assuming the name of each mountain is different.

        Args:
        - compared_mountain: The mountain to be compared to

        Returns:
        - boolean value representing if it is actually greater than or not

        Complexity:
        - Worst case: O(comp(T)), for comparison done, which occurs when length is the same, resulting in the name to be
          compared
        - Best case: O(1), which occurs when the only the length is compared
        """
        if self.length == compared_mountain.length :
            return self.name > compared_mountain.name
        return self.length > compared_mountain.length
    
    def __ge__(self, compared_mountain: Mountain) -> bool:
        """
        Magic method for greater than or equal to, when two mountains are compared. Length is to be compared first, then the 
        name is compared if the length is the same. This is assuming the name of each mountain is different.

        Args:
        - compared_mountain: The mountain to be compared to

        Returns:
        - boolean value representing if it is actually greater than or equal to or not

        Complexity:
        - Worst case: O(comp(T)), for comparison done, which occurs when length is the same, resulting in the name to be
          compared
        - Best case: O(1), which occurs when the only the length is compared
        """
        if self.length == compared_mountain.length :
            return self.name >= compared_mountain.name
        return self.length >= compared_mountain.length
  
    def __eq__(self, compared_mountain: Mountain) -> bool:
        """
        Magic method for equal to, when two mountains are compared. Length is to be compared first, then the 
        name is compared if the length is the same.
        
        Args:
        - compared_mountain: The mountain to be compared to

        Returns:
        - boolean value representing if it is actually greater than or equal to or not

        Complexity:
        - Worst case: O(comp(T)), for comparison done, which occurs when length is the same, resulting in the name to be
          compared
        - Best case: O(1), which occurs when the only the length is compared
        """
        if self.length == compared_mountain.length :
            return self.name == compared_mountain.name
        return self.length == compared_mountain.length
