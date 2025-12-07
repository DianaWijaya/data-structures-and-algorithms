from mountain import Mountain
from data_structures.hash_table import LinearProbeTable
from double_key_table import DoubleKeyTable
from algorithms.mergesort import mergesort

class MountainManager:

    def __init__(self) -> None:
        """
        Initialisation

        Args:
        - None

        Returns:
        - None

        Complexity:
        - Worst case: O(n), where n is the amount of times initialization to None is done, in the initialization of ArrayR, which is the
          table size.
        - Best case: O(n), where n is the amount of times initialization to None is done, in the initialization of ArrayR, which is the 
          table size.
        """
        self.mountains = LinearProbeTable() # O(n)

    def add_mountain(self, mountain: Mountain) -> None:
        """
        Add a mountain to the manager

        Args: 
        - mountain: The mountain to be added 

        Returns: 
        - None

        Raises:
        - FullError: occurs when the hash table is full, and the mountain cannot be added

        Complexity:
        - Worst case: O(hash(key) + N*comp(K)), when we've searched the entire table, where N is the tablesize, comp(K) is the complexity
          of comparing, and hash(key) is just the length of the key.
        - Best case: O(hash(key)), which occurs when the first position is empty, and hash(key) is just the length of the key.
        """
        self.mountains[mountain.name] = mountain # O(n)

    def remove_mountain(self, mountain: Mountain) -> None:
        """
        Remove a mountain from the manager

        Args:
        - mountain: The mountain to be removed

        Returns:
        - None

        Raises:
        - KeyError: occurs when the element is not found in the hash table.

        Complexity:
        - Worst case: O(N*hash(key)+N^2*comp(K)) deleting item is midway through large chain. N is the size of the table, comp(K) is just the 
          complexity of comparison, and hash(key) is just the length of the key.
        - Best case: O(hash(key)), which occurs when deleting item is not probed and in correct spot, hash(key) is just the length of the key.
        """
        del self.mountains[mountain.name] # O(n)

    def edit_mountain(self, old: Mountain, new: Mountain) -> None:
        """
        Edit the mountain by changing the old mountain to the new mountain

        Args: 
        - old: The old mountain to be changed
        - new: The new mountain to be changed to

        Returns:
        - None

        Raises:
        - KeyError: occurs when the element is not found in the hash table
        - FullError: occurs when the hash table is full, and the mountain cannot be added

        Complexity:
        - Worst case: O(N*hash(key)+N^2*comp(K)) deleting item is midway through large chain. N is the size of the table, comp(K) is just the 
          complexity of comparison, and hash(key) is just the length of the key.
        - Best case: O(hash(key)), which occurs when  deleting item is not probed and in correct spot or when the first position is empty 
          when setting item, hash(key) is just the length of the key.
        """

        del self.mountains[old.name] # O(n)
        self.mountains[new.name] = new # O(n)

    def mountains_with_difficulty(self, diff: int) -> list[Mountain]:
        """
        Return a list of all mountains with this difficulty

        Args:
        - diff: difficulty level

        Returns:
        - mountains_difficulty: List of mountains with the specified difficulty

        Complexity:
        - Worst case: O(n), where n is the number of mountains in the linear probe table
        - Best case: O(n), where n is the number of mountains in the linear probe table
        """

        # Initialize an empty list 
        mountains_difficulty = [] # O(1)

        # Loop through each mountain in hash table and compare the difficulty level, if same, then add the mountain to the list
        for each_mountain in self.mountains.values() : # O(n)
            if each_mountain.difficulty_level == diff : # O(1)
                mountains_difficulty.append(each_mountain) # O(1)

        return mountains_difficulty # O(1)

    def group_by_difficulty(self) -> list[list[Mountain]]:
        """
        Returns a list of lists of all mountains, grouped by and sorted by ascending difficulty

        Args:
        - None

        Returns:
        - mountain_list: list of lists of all mountains, grouped by and sorted by ascending difficulty

        Complexity:
        - Worst case: O(mn), where m is the amount of times it loops through the number of unique difficulties, and n is the number
          of mountains in the linear probe table that is done in the loop when the function mountains_with_difficulty is called.
        - Best case: O(mn), where m is the amount of times it loops through the number of unique difficulties, and n is the number
          of mountains in the linear probe table that is done in the loop when the function mountains_with_difficulty is called.
        """

        # Create an empty list to store all the different difficulties
        difficulty_list = [] # O(1)

        # Loop through each mountain in hash table to append each new difficulty
        for each_mountain in self.mountains.values() : # O(n)
            if each_mountain.difficulty_level not in difficulty_list : # O(1)
                difficulty_list.append(each_mountain.difficulty_level) # O(1)

        # Sort the difficulty by merge sort algorithm
        difficulty_list = mergesort(difficulty_list) # O(NlogN)

        # Create a list with empty lists of the amount of difficulties 
        mountain_list = []

        # Loop through each difficulty, and append the mountain that matches the difficulty
        for difficulty_index in difficulty_list : # O(n)
            mountain_list.append(self.mountains_with_difficulty(difficulty_index)) # O(n)

        return mountain_list # O(1)
    

if __name__ == "__main__" :
    pass