from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __lt__(self, other: "Beehive") -> bool : # O(1)
        """
            Magic method for less than, when comparing beehives. Compares the nutrient factor of the two beehives, by 
            multiplying the minimum of the capacity and volume of the beehive with the nutrient factor of the beehive.

            Arg:
            - other: the beehive to be compared to 

            Returns:
            - boolean value representing whether the beehive is less than the other beehive

            Raises:
            - None

            Complexity:
            - WCS: O(1), when the beehives are compared, only operations and comparisons are done
            - BCS: O(1), same as WCS
        """
        return ((min(self.capacity, self.volume)) * self.nutrient_factor) < ((min(other.capacity, other.volume))*other.nutrient_factor) # O(1)
    
    def __le__(self, other: "Beehive") -> bool : # O(1)
        """
            Magic method for less than or equal to, when comparing beehives. Compares the nutrient factor of the two 
            beehives, by multiplying the minimum of the capacity and volume of the beehive with the nutrient factor of 
            the beehive.

            Arg:
            - other: the beehive to be compared to 

            Returns:
            - boolean value representing whether the beehive is less than or equal to the other beehive

            Raises:
            - None

            Complexity:
            - WCS: O(1), when the beehives are compared, only operations and comparisons are done
            - BCS: O(1), same as WCS
        """
        return ((min(self.capacity, self.volume)) * self.nutrient_factor) <= ((min(other.capacity, other.volume))*other.nutrient_factor) # O(1)
    
    def __gt__(self, other: "Beehive") -> bool : # O(1)
        """
            Magic method for greater than, when comparing beehives. Compares the nutrient factor of the two beehives, by 
            multiplying the minimum of the capacity and volume of the beehive with the nutrient factor of the beehive.

            Arg:
            - other: the beehive to be compared to 

            Returns:
            - boolean value representing whether the beehive is greater than the other beehive

            Raises:
            - None

            Complexity:
            - WCS: O(1), when the beehives are compared, only operations and comparisons are done
            - BCS: O(1), same as WCS
        """
        return ((min(self.capacity, self.volume)) * self.nutrient_factor) > ((min(other.capacity, other.volume))*other.nutrient_factor) # O(1)
    
    def __ge__(self, other: "Beehive") -> bool : # O(1)
        """
            Magic method for greater than or equal to, when comparing beehives. Compares the nutrient factor of the two 
            beehives, by multiplying the minimum of the capacity and volume of the beehive with the nutrient factor of 
            the beehive.

            Arg:
            - other: the beehive to be compared to 

            Returns:
            - boolean value representing whether the beehive is greater than or equal to the other beehive

            Raises:
            - None

            Complexity:
            - WCS: O(1), when the beehives are compared, only operations and comparisons are done
            - BCS: O(1), same as WCS
        """
        return ((min(self.capacity, self.volume)) * self.nutrient_factor) >= ((min(other.capacity, other.volume))*other.nutrient_factor) # O(1)

    def __eq__(self, other: "Beehive") -> bool : # O(1)
        """
            Magic method for equal to, when comparing beehives. Compares the nutrient factor of the two beehives, by 
            multiplying the minimum of the capacity and volume of the beehive with the nutrient factor of the beehive.

            Args:
            - other: the beehive to be compared to 

            Returns:
            - boolean value representing whether the beehive is equal to the other beehive

            Raises:
            - None

            Complexity:
            - WCS: O(1), when the beehives are compared, only operations and comparisons are done
            - BCS: O(1), same as WCS
        """
        return ((min(self.capacity, self.volume)) * self.nutrient_factor) == ((min(other.capacity, other.volume))*other.nutrient_factor) # O(1)

class BeehiveSelector:
    def __init__(self, max_beehives: int) -> None:
        """
            Initializes BeehiveSelector, creates and empty MaxHeap with the length of max_beehives

            Args:
            - max_beehives (int): the max number of beehives

            Returns:
            - None

            Raises:
            - None

            Complexity:
            - WCS: O(n), for creating a MaxHeap with a max capacity of max_beehives, and n is the length of max_beehives.
            - BCS: O(n), same as WCS
        """
        self.heap = MaxHeap(max_beehives) # O(1)

    def set_all_beehives(self, hive_list: list[Beehive]) -> None :
        """
            replaces all the current beehives in the heap with the beehives provided in hive_list

            Args:
            - hive_list (list[Beehive]): a new list of beehives to replace the current beehives

            Returns:
            - None

            Raises:
            - None

            Complexity:
            - WCS: O(M), where M is the length of hive_list, occurs when the heap is replaced with a new heap,
                   and heapify is called on the new heap.
            - BCS: O(M), same as WCS
        """
        self.heap = MaxHeap(len(hive_list), hive_list) # O(n)
        
    def add_beehive(self, hive: Beehive) -> None :
        """
            adds a beehive into the heap 

            Args:
            - hive (Beehive): the beehive to be added into the heap

            Returns:
            - None

            Raises:
            - None

            Complexity:
            - WCS: O(log(N)), where log(N) is the depth of the heap.
            - BCS: O(log(N)), same as WCS
        """
        self.heap.add(hive) # O(log(n))
    
    def harvest_best_beehive(self) -> float :
        """
            locates the 'best' beehive in the heap and 'consumed' the beehive is then replaced into the heap.

            Args:
            - None

            Returns:
            - emeralds (float): the amount of emeralds earned from harvesting the beehive

            Raises:
            - None

            Complexity:
            - WCS: O(log(N)), where log(N) is the depth of the heap, where the reduced heap is reshuffled to satisfy heap property
            - BCS: O(log(N)), same as WCS
        """
        max_emerald: Beehive = self.heap.get_max() # O(log(n)

        new_volume = max_emerald.volume - min(max_emerald.capacity, max_emerald.volume) # O(1)
        if new_volume > 0 : # O(1)
            self.add_beehive(Beehive(max_emerald.x, max_emerald.y, max_emerald.z, max_emerald.capacity, max_emerald.nutrient_factor, new_volume)) # O(log(n))

        return ((min(max_emerald.capacity, max_emerald.volume)) * max_emerald.nutrient_factor) # O(1)

if __name__ == '__main__':
    pass
