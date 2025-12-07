from __future__ import annotations
from action import PaintAction
from grid import Grid
from undo import UndoTracker
from data_structures import queue_adt

class ReplayTracker:

    def __init__(self) -> None:
        """
        Initialize variable

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which is the creation of Circular queue with a fixed amount of element
        - Best case: O(1), which is the creation of Circular queue with a fixed amount of element
        """
        
        # Create instance variable, the data structure used is Circular queue from queue_adt
        self.replay_list = queue_adt.CircularQueue(10000) # O(n)

    def start_replay(self) -> None:
        """
        Called whenever we should stop taking actions, and start playing them back.

        Useful if you have any setup to do before `play_next_action` should be called.

        !! NOT USED !!

        :pre: 
        :post:
        :complexity:
        """

    def add_action(self, action: PaintAction, is_undo: bool=False) -> None:
        """
        Adds an action to the replay

        Args:
        - action: Action to be done
        - is_undo: boolean value to indicate if it is an undo action

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which occurs during the creation of object UndoTracker which is the creation of arraystacks, 
          with a fixed amount of elements
        - Best case: O(1), which occurs when is_undo is False, the action is immediately appended into the circular queue
        """

        # If action is not undo, append the action into the queue
        if is_undo == False : # O(1)
            self.replay_list.append(action) # O(1)

        # If action is undo, create UndoTracker object, and add the action to the object. Lastly, append the object to the queue
        else :
            undo = UndoTracker() # O(1)
            undo.add_action(action) # O(1)
            self.replay_list.append(undo) # O(1)
            

    def play_next_action(self, grid: Grid) -> bool:
        """
        Plays the next replay action on the grid. If there were no more actions to play, nothing  happens and return True,
        otherwise return False.

        Args:
        - grid: The grid where actions are applied to

        Returns:
        - Boolean value. 
            ~ If there were no more actions to play, and so nothing happened, return True.
            ~ Otherwise, return False.

        Complexity:
        - Worst case: O(mn o log(p)), which occurs when undo_apply or redo_apply is applied to the grid, and is_special 
          is True, which leads to the special function from SequenceLayerStore being the worst case scenario. In this 
          case, m is the amount of times it loops through the width of the grid, n is the amount of times it loops 
          through the length of the grid, and in special function, o is amount of times it loops through based on 
          the length of layers, and log(p) occurs when the the index of that layer exists in the BSet, that layer 
          is added into the temporary array sorted list, in add function, the position of the index is to be found 
          using the function _index_to_add, which iterates logarithmically, because it involves halving the number 
          of elements in an array
        - Best case: O(1), which occurs when the circular queue is empty, so no actions are to be replayed, so nothing 
          happens and True is returned
        """

        # If the queue is empty, nothing happens and True is returned
        if self.replay_list.is_empty() == True : # O(1)
            return True # O(1)
        
        # Else, the queue's first element is served
        else : # O(1)
            first_element = self.replay_list.serve() # O(1)

            # If the action is an undo adtion, get the first element in the undo list and apply undo to the grid
            if isinstance(first_element, UndoTracker) == True : # O(1)
                # check.undo_list.pop().undo_apply(grid) 
                popped_item = first_element.undo_list.peek() # O(1)
                first_element.undo_list.pop() # O(1)
                popped_item.undo_apply(grid) # O(mn o log(p))
                
            # Else, apply redo to the grid
            else : # O(1)
                first_element.redo_apply(grid) # O(mn o log(p))

            return False # O(1)



if __name__ == "__main__":
    action1 = PaintAction([], is_special=True)
    action2 = PaintAction([])

    g = Grid(Grid.DRAW_STYLE_SET, 5, 5)

    r = ReplayTracker()
    # add all actions
    r.add_action(action1)
    r.add_action(action2)
    r.add_action(action2, is_undo=True)
    # Start the replay.
    r.start_replay()
    f1 = r.play_next_action(g) # action 1, special
    f2 = r.play_next_action(g) # action 2, draw
    f3 = r.play_next_action(g) # action 2, undo
    t = r.play_next_action(g)  # True, nothing to do.
    assert (f1, f2, f3, t) == (False, False, False, True)

