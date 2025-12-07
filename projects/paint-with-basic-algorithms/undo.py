from __future__ import annotations
from action import PaintAction
from grid import Grid
import layer_store
from data_structures.stack_adt import ArrayStack

class UndoTracker:
    def __init__(self) -> None:
        """
        Initialize variables

        Returns:
        - None

        Complexity:
        - Worst case: O(n), which is the creation of arraystacks, with a fixed amount of elements
        - Best case: O(n), which is the creation of arraystacks, with a fixed amount of elements
        """

        # Initialize instance variables, the data structure used is ArrayStack from stack_adt
        self.undo_list = ArrayStack(10000) # O(1)
        self.redo_list = ArrayStack(10000) # O(1)

    def add_action(self, action: PaintAction) -> None:
        """
        Adds an action to the undo tracker. If your collection is already full, feel free to exit early and not add the action

        Args:
        - action: Action to be done

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which occurs when the undo_list is not full, and the action is pushed to the top of the stack
        - Best case: O(1), which occurs when the undo_list is full, pass immediately
        """

        # If the stack is not full, push the action to the top of the stack, else nothing happens 
        if self.undo_list.is_full() == False : # O(1)
            self.undo_list.push(action) # O(1)
        else : # O(1)
            pass # O(1)
        
    def undo(self, grid: Grid) -> PaintAction|None:
        """
        Undo an operation, and apply the relevant action to the grid. If there are no actions to undo, simply do nothing.

        Args:
        - grid: The grid to apply the undo to

        Returns:
        - PaintAction: The action that is undone
        - None

        Complexity:
        - Worst case: O(mn o log(p)), which occurs when undo_apply is applied to the grid, and is_special is True, this 
          leads to the special function from SequenceLayerStore being the worst case scenario. In this case, m is the amount
          of times it loops through the width of the grid, n is the amount of times it loops through the length of the 
          grid, and in special function, o is amount of times it loops through based on the length of layers, and log(p) 
          occurs when the the index of that layer exists in the BSet, that layer is added into the temporary array sorted 
          list, in add function, the position of the index is to be found using the function _index_to_add, which iterates 
          logarithmically, because it involves halving the number of elements in an array
        - Best case: O(1), which occurs when the undo_list is empty, nothing happens so None is returned immediately
        """

        # If the stack is not empty, peek and pop the element at the top and apply undo to that layer
        if self.undo_list.is_empty() == False : # O(1)
            undone_action = self.undo_list.peek() # O(1)
            self.undo_list.pop() # O(1)
            undone_action.undo_apply(grid) # O(mn o log(p))

            # Push this action to the top of the stack of redo_list
            self.redo_list.push(undone_action) # O(1)

            # Return the element at the top of the stack
            return undone_action # O(1)
        
        # Else do nothing and None is returned
        else : # O(1)
            return None # O(1)

    def redo(self, grid: Grid) -> PaintAction|None:
        """
        Redo an operation that was previously undone. If there are no actions to redo, simply do nothing.

        Args:
        - grid: The grid to apply redo to

        Returns:
        - PaintAction: The action that is redone
        - None

        Complexity:
        - Worst case: O(mn o log(p)), which occurs when redo_apply is applied to the grid, and is_special is True, which 
          leads to the special function from SequenceLayerStore being the worst case scenario. In this case, m is the amount
          of times it loops through the width of the grid, n is the amount of times it loops through the length of the 
          grid, and in special function, o is amount of times it loops through based on the length of layers, and log(p) 
          occurs when the the index of that layer exists in the BSet, that layer is added into the temporary array sorted 
          list, in add function, the position of the index is to be found using the function _index_to_add, which iterates 
          logarithmically, because it involves halving the number of elements in an array
        - Best case: O(1), which occurs when the redo_list is empty, nothing is done and None is returned
        """

        # If the stack is not empty, peek and pop the element at the top and apply redo to that layer
        if self.redo_list.is_empty() == False : # O(1)
            redo_action = self.redo_list.peek() # O(1)
            self.redo_list.pop() # O(1)
            redo_action.redo_apply(grid) # O(mn o log(p))

            # Push this action to the top of the stack of undo_list
            self.undo_list.push(redo_action) # O(1)

            # Return the element at the top of the stack
            return redo_action # O(1)
        
        # Else do nothing and None is returned
        else : # O(1)
            return None # O(1)
        
        
