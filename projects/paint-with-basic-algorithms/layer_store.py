from __future__ import annotations
from abc import ABC, abstractmethod
from layer_util import Layer, get_layers
import layers
from data_structures.queue_adt import CircularQueue
from data_structures.stack_adt import ArrayStack
from data_structures.array_sorted_list import ArraySortedList, ListItem
from data_structures.bset import BSet

class LayerStore(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        pass

    @abstractmethod
    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        pass

class SetLayerStore(LayerStore):
    """
    Set layer store. A single layer can be stored at a time (or nothing at all)
    - add: Set the single layer.
    - erase: Remove the single layer. Ignore what is currently selected.
    - special: Invert the colour output.
    """

    def __init__(self) -> None:
        """
        Initialize instance variables

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where instance variable layer is set to None and inverted_colour is set to False
        - Best case: O(1), where instance variable layer is set to None and inverted_colour is set to False
        """

        # Initialize instance variables
        self.layer = None # O(1)
        self.inverted_colour = False # O(1)

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store. Returns true if the LayerStore was actually changed.

        Args:
        - layer: The layer to be applied

        Returns:
        - boolean value, True is returned if LayerStore was actually changed, otherwise return False

        Complexity:
        - Worst case: O(1), which occurs when layer is changed, and True is returned
        - Best case: O(1), which occurs when layer is not changed, and False is returned
        """

        # If layer to be changed is the same, return false, or else change the layer and return True
        if layer == self.layer : # O(1)
            return False # O(1)
        else : # O(1)
            self.layer = layer # O(1)
            return True  # O(1)

    def get_color(self, start: tuple[int, int, int], timestamp: int, x: int, y: int) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.

        Args:
        - start: The original RGB value
        - timestamp: Used only for animated layers
        - x: Used for some layers
        - y: Used for some layers

        Returns:
        - start: The final RGB value to be displayed on the window in the form of a tuple

        Complexity:
        - Worst case: O(n), where n is the timestamp, which will only apply in sparkle.
        - Best case: O(1), which happens when there is no layer and inverted_colour is not 
          True, so the original RGB value is returned immediately, without applying any layer
          or inverting
        """

        # If there is a layer, apply layer to the window
        if self.layer != None : # O(1)
            start = self.layer.apply(start, timestamp, x, y) # O(n)

            # If special is True, then apply invert of the layer to the window
            if self.inverted_colour == True : # O(1)
                return layers.invert.apply(start, timestamp, x, y) # O(1)
            
            # Return the final colour of rgb in a form of a tuple
            else : # O(1)
                return start # O(1)
            
        # If there is no layer, just apply the invert to the entire window
        else : # O(1)
            if self.inverted_colour == True : # O(1)
                return layers.invert.apply(start, timestamp, x, y) # O(1)
            
            # Return the final colour of rgb in a form of a tuple
            else : # O(1)
                return start # O(1)

    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer. Returns true if the LayerStore was actually changed.
        Remove the single layer. Ignore what is currently selected.

        Args:
        - layer: The layer to be erased

        Returns:
        - boolean value, True is returned if layer is removed, otherwise return False

        Complexity:
        - Worst case: O(1), which happens when layer is changed to None and True is returned
        - Best case: O(1), which happens when layer is already None, so it is not changed, and
          False is returned
        """

        # If there is no layer to be erased, then immidiately return False, else change the layer into None and return True
        if layer == None : # O(1)
            return False # O(1)
        else : # O(1)
            self.layer = None # O(1)
            return True # O(1)

    def special(self) -> None:
        """
        Special mode. Invert the colours on the window

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which is changing the boolean value to their opposite
        - Best case: O(1), which is changing the boolean value to their opposite
        """

        # Make the boolean value in variable inverted_colour the opposite. So True -> False and False -> True
        self.inverted_colour = not self.inverted_colour # O(1)

class AdditiveLayerStore(LayerStore):
    """
    Additive layer store. Each added layer applies after all previous ones.
    - add: Add a new layer to be added last.
    - erase: Remove the first layer that was added. Ignore what is currently selected.
    - special: Reverse the order of current layers (first becomes last, etc.)
    """

    def __init__(self) -> None:
        """
        Initialize variables

        Returns:
        - None

        Complexity:
        - Worst case: O(n), where n is the length of the layers multiplied by 100 to be initialized in
          the circular queue
        - Best case: O(n), where n is the length of the layers multiplied by 100 to be initialized in
          the circular queue
        """

        # Initialize instance variables, the data structure used is circular queue
        self.layer_queue = CircularQueue(len(get_layers())*100) # O(n)
        self.reversed_layer = False # O(1)

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store. Returns true if the LayerStore was actually changed. Add a new 
        layer to be added last

        Args:
        - layer: The layer to be added

        Returns:
        - boolean value, True is returned if the layer was actually appended, otherwise return False

        Complexity:
        - Worst case: O(1), which occurs when a layer is successfully appended into the queue and True
          is returned
        - Best case: O(1), which occurs when a layer is not appended into the queue because it is already
          full, so False is returned
        """

        # If the layer list is not full yet, then append the layer and return True, or else return False
        if self.layer_queue.is_full() == False : # O(1)
            self.layer_queue.append(layer) # O(1)
            return True # O(1)
        else : # O(1)
            return False # O(1)

        
    def get_color(self, start: tuple[int, int, int], timestamp: int, x: int, y: int) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.

        Args:
        - start: The original RGB value
        - timestamp: Used only for animated layers
        - x: Used for some layers
        - y: Used for some layers

        Returns:
        - start: The final RGB value to be displayed on the window in the form of a tuple

        Complexity:
        - Worst case: O(mn), where m is the amount of times it loops through based on the length of the 
          queue, and n is the timestamp, which will only apply for animated layer
        - Best case: O(1), which occurs when the Circular Queue is empty, so no layer is added or applied,
          so original RGB value is returned immediately
        """

        # If there is one or more layer in layer list, then for each layer in the layer list, apply the layer to the window. 
        if self.layer_queue.is_empty() == False : # O(1)
            for each_layer in range(len(self.layer_queue)) : # O(n)
                layer = self.layer_queue.serve() # O(1)
                start = layer.apply(start, timestamp, x, y) # O(n)
                self.layer_queue.append(layer) # O(1)
        else : # O(1)
            pass # O(1)

        # Return a layer in the form of tuple of rgb values
        return start # O(1)
            

    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer. Returns true if the LayerStore was actually changed.
        Remove the first layer that was added. Ignore what is currently selected

        Args:
        - layer: Ignore in this function

        Returns:
        - boolean value, True is returned if layer is removed, otherwise return False

        Complexity:
        - Worst case: O(1), which occurs when the queue is not empty, and the queue's front element
          is deleted, followed by returning True
        - Best case: O(1), which occurs when the queue is empty, nothing happens and False is returned
        """

        # If the layer is not empty, then delete the element at the top of the queue and return True, or else return False immidiately
        if self.layer_queue.is_empty() == False : # O(1)
            self.layer_queue.serve() # O(1)
            return True # O(1)
        else : # O(1)
            return False # O(1)
        
    def special(self) -> None:
        """
        Special mode. Reverse the order of current layers (first becomes last, etc.)

        Returns:
        - None

        Complexity:
        - Worst case: O(mn), where m is the amount of given layers, during the creation of bufferStack, and n
          is the amount of times it loops based on the length of the queue and the stack
        - Best case: O(1), which occurs when the queue is empty or it only has one element, nothing happens
        """

        # If there is no element, or only one element in the circular queue, nothing is done for special mode
        if (len(self.layer_queue) == 1) or (self.layer_queue.is_empty() == True) : # O(1)
            return # O(1)

        else :
            # Create a new temporary stack using data structure ArrayStack from stack_adt
            bufferStack = ArrayStack(len(get_layers()) * 100) # O(n)

            # Loop through layers in the circular queue, and push the element to the top of the newly created temporary stack
            for each_element in range(len(self.layer_queue)) : # O(n)
                bufferStack.push(self.layer_queue.serve()) # O(1)

            # Loop through layers in the temporary stack, and add the element to the rear of the queue
            for each_element_2 in range(len(bufferStack)) : # O(n)
                self.layer_queue.append(bufferStack.pop()) # O(1)

class SequenceLayerStore(LayerStore):
    """
    Sequential layer store. Each layer type is either applied / not applied, and is applied in order of index.
    - add: Ensure this layer type is applied.
    - erase: Ensure this layer type is not applied.
    - special:
        Of all currently applied layers, remove the one with median `name`.
        In the event of two layers being the median names, pick the lexicographically smaller one.
    """

    def __init__(self) -> None:
        """
        Initialize variable, to create a BSet

        Returns:
        - None

        Complexity:
        - Worst case: O(1), the creation of a BSet
        - Best case: O(1), the creation of a BSet
        """

        # Initialize an instance variable, the  data structure used is BSet
        self.sequential_layer = BSet() # O(1)

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store. Returns true if the LayerStore was actually changed. Ensure this
        layer type is applied.

        Args:
        - layer: The layer to be "applied"

        Returns:
        - boolean value, True is returned if the layer was changed to "applied", otherwise return False

        Complexity:
        - Worst case: O(1), which occurs when the layer is added, and True is returned
        - Best case: O(1), which occurs when the layer is not added, False is returned immediately
        """

        # If the layer is already "applied", return False, or else add the index to the bset, to make it "applied"
        layer_index = layer.index + 1 # O(1)
        if layer_index in self.sequential_layer : # O(1)
            return False # O(1)
        else : # O(1)
            self.sequential_layer.add(layer_index) # O(1)
            return True # O(1)


    def get_color(self, start: tuple[int, int, int], timestamp: int, x: int, y: int) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers

        Args:
        - start: The original RGB value
        - timestamp: Used only for animated layers
        - x: Used for some layers
        - y: Used for some layers

        Returns:
        - start: The final RGB value to be displayed on the window in the form of a tuple

        Complexity:
        - Worst case: O(mn), where m is the amount of times it loops through the get_layers, and n is the 
          timestamp, which will only apply for animated layers
        - Best case: O(n), where m is the amount of times it loops through the get_layers, which occurs when the 
          layer is None
        """
    
        # Loop through each layer to check if the index is "applied", if it is then apply the layer to the the grid square
        for each_layer in get_layers() : # O(n)
            if each_layer != None : # O(1)
                if (each_layer.index + 1) in self.sequential_layer : # O(1)
                    start = each_layer.apply(start, timestamp, x, y) # O(n)
                else : # O(1)
                    pass # O(1)

        # Return the final RGB value to be displayed on the window in the form of a tuple
        return start # O(1)


    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer. Returns true if the LayerStore was actually changed.
        Ensure this layer type is not applied

        Args:
        - layer: The layer to be "unapplied"

        Returns:
        - boolean value, True is returned if layer is set to "not applied", otherwise return False

        Complexity:
        - Worst case: O(1), which occurs when when the layer is removed, and True is returned
        - Best case: O(1), which occurs when the layer is not removed, and False is returned immediately
        """

        # If the layer is already "not applied", return False, or else remove the index from the bset, to make it "not applied"
        layer_index = (layer.index + 1) # O(1)
        if layer_index not in self.sequential_layer : # O(1)
            return False # O(1)
        else : # O(1)
            self.sequential_layer.remove(layer_index) # O(1)
            return True # O(1)

    def special(self) -> None:
        """
        Special mode. 
        Of all currently applied layers, remove the one with median 'name', ordered lexicographically.
        In the event of two layers being the median names, pick the lexicographically smaller one.

        Returns:
        - None

        Complexity:
        - Worst case: O(m log(n)), where m is amount of times it loops through based on the length of layers,
          and log(n) occurs when the the index of that layer exists in the BSet, that layer is added into the 
          temporary array sorted list, in add function, the position of the index is to be found using the function 
          _index_to_add, which iterates logarithmically, because it involves halving the number of elements in 
          an array
        - Best case: O(n), where n is the amount of times it loops through get_layers, but there is no layer in 
          the temporary sequential layer, so nothing happens
        """

        # Create a temporary array sorted list
        temporary_sequential_layer = ArraySortedList(len(self.sequential_layer)) # O(n)

        # Loop through each layer in get_layers to obtain the layer and name, and add it to the temporary list if it is "applying"
        for each_layer in get_layers() : # O(n)
            if each_layer != None : # O(1)
                if (each_layer.index + 1) in self.sequential_layer : # O(1)
                    temporary_sequential_layer.add(ListItem(each_layer, each_layer.name)) # O(log(n))

        # Calculate the middle point
        times = len(temporary_sequential_layer) // 2 # O(1)

        # If there is no layer that is "applying", nothing is done
        if len(temporary_sequential_layer) == 0 : # O(1)
            return # O(1)
        
        # If there is one layer that is "applying", that one layer's index is removed from the BSet, making it "not applying"
        if len(temporary_sequential_layer) == 1 : # O(1)
            self.sequential_layer.clear() # O(1)
            return # O(1)

        # If there is an even number of layers that is "applying", remove the median, lexicographically smaller one from the 2 medians
        if len(temporary_sequential_layer) % 2 == 0 and len(temporary_sequential_layer) != 0:  # O(1)
            self.sequential_layer.remove((temporary_sequential_layer[times - 1].value).index + 1) # O(1)
            
        # If there is an odd number of layers that is "applying", remove the median 
        elif len(temporary_sequential_layer) % 2 == 1 : # O(1)
            self.sequential_layer.remove((temporary_sequential_layer[times].value).index + 1) # O(1)
