# Import modules, files, and data structures
from __future__ import annotations
from layer_store import SetLayerStore, AdditiveLayerStore, SequenceLayerStore, LayerStore
from data_structures.referential_array import ArrayR
from layer_util import Layer


class Grid:
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0

    def __init__(self, draw_style: DRAW_STYLE_OPTIONS, x: int, y: int) -> None:
        """
        Initialise the grid object.

        Args:
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.
        - brush_size: The brush size during painting

        Returns:
        - None

        Complexity:
        - Worst case: O(mno), where m is the width of the grid, n is the length of the grid, 
          and o is the length of queue that is in AdditiveLayerStore
        - Best case: O(mn), where m is the width of the grid and n is the length of the grid, 
          and it will only occur when the layer being initialized is SetLayerStore or 
          SequenceLayerStore
        """

        # Initialize variables 
        self.draw_style = draw_style # O(1)
        self.x = x # O(1)
        self.y = y # O(1)
        self.brush_size = self.DEFAULT_BRUSH_SIZE # O(1)

        # Initialise a grid using data structure ArrayR
        self.grid = ArrayR(x) # O(n)

        # Loop through the dimensions of the grid and select the specific layer store based on the draw_style
        for each_x in range(x) : # O(n)
            self.grid[each_x] = ArrayR(y) # O(n)
            for each_y in range(y) : # O(n)
                if self.draw_style == self.DRAW_STYLE_SET : # O(1)
                    self.grid[each_x][each_y] = SetLayerStore() # O(1)

                elif self.draw_style == self.DRAW_STYLE_ADD : # O(1)
                    self.grid[each_x][each_y] = AdditiveLayerStore() # O(n)

                elif self.draw_style == self.DRAW_STYLE_SEQUENCE : # O(1)
                    self.grid[each_x][each_y] = SequenceLayerStore() # O(1)

    def increase_brush_size(self) -> None:
        """
        Increases the size of the brush by 1, if the brush size is already MAX_BRUSH, then do
        nothing.

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where 1 operation happens when brush size is lesser than the maximum brush
          size, and brush size is increased by 1
        - Best case: O(1), where 1 operation happens when brush size is the maximum brush size or more, 
          so immidiately pass
        """

        # If the brush size is lesser then maximum value, brush size is increased by 1, else do nothing
        if self.brush_size < self.MAX_BRUSH : # O(1)
            self.brush_size += 1 # O(1)
        else : # O(1)
            pass # O(1)

    def decrease_brush_size(self) -> None:
        """
        Decreases the size of the brush by 1, if the brush size is already MIN_BRUSH, then do 
        nothing.

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where 1 operation happens when the brush size is more than the minimum brush
          size, and brush size is decreased by 1
        - Best case: O(1), where 1 operation happens when brush size is the minimum brush size, then immidiately
          pass
        """

        # If the brush size is more than the minimum value, brush size is decreased by 1, else do nothing
        if self.brush_size > self.MIN_BRUSH : # O(1)
            self.brush_size -= 1 #(1)
        else : #(1)
            pass #(1)

    def special(self) -> PaintAction:
        """
        Applying the special affect on all grid squares within the grid

        Returns:
        - PaintAction: PaintAction object called PaintAction

        Complexity:
        - Worst case: O(mn o log(p)), where m is the amount of times it loops through the width of the grid, n is the amount
          of times it loops through the length of the grid, and in special function, o is amount of times it loops through 
          based on the length of layers, and log(p) occurs when the the index of that layer exists in the BSet, that 
          layer is added into the temporary array sorted list, in add function, the position of the index is to be 
          found using the function _index_to_add, which iterates logarithmically, because it involves halving the 
          number of elements in an array
        - Best case: O(mn), where m is the amount of times it loops through the width of the grid, n is the amount of times
          it loops through the length of the grid. This only occurs for the special function of  SetLayerStore and 
          AdditiveLayerStore
        """

        # Import classes 
        from action import PaintAction, PaintStep

        # Loop through the dimension of the grid and apply the special function to each grid square
        for each_x in range(self.x) : # O(n)
            for each_y in range(self.y) : # O(n)
                self.grid[each_x][each_y].special() # WCS: O(m log(n))   BCS: O(1)
        
        # Return this class for paint action for replay
        return PaintAction(is_special=True) # O(1)

    def paint_grid(self, layer: Layer, x: int, y: int) -> PaintAction:
        """
        Apply paint to each grid square within the manhattan distance at grid x and y, based on the 
        given brush size. The paint should not be applied to invalid grid positions, such as
        position (-1, 5).

        Args:
        - layer: The layer to be applied 
        - x: The x coordinate
        - y: The y coordinate

        Returns:
        - paint_action: Object called paint_action 

        Complexity:
        - Worst case: O(n^2), where n is the amount of times the for loop of manhattan distance occurs 
          for the x coordinate and y coordinate, which is the same amount of time. Then, for the add 
          function, the worst case scenario is O(1), for every sequence layer 
        - Best case: O(n^2),  where n is the amount of times the for loop of manhattan distance occurs 
          for the x coordinate and y coordinate, which is the same amount of time. This happens if the 
          final coordinate is out of range (exp: (-1, 4)), so the color does not apply to that
          grid square
        """

        # Import classes
        from action import PaintAction, PaintStep # O(1)

        # Initialize an object
        paint_action = PaintAction() # O(1)

        # Loop through the manhattan algorithm of the coordinate and add the layer when the coordinate is valid
        for x_cord in range((x-self.brush_size), (x+self.brush_size+1)) : # O(n)
            for y_cord in range((y-self.brush_size), (y+self.brush_size+1)) : # O(n)
                manhattan_algorithm_x = abs(x_cord - x) # O(1)
                manhattan_algorithm_y = abs(y_cord - y) # O(1)
                manhattan_algorithm = manhattan_algorithm_x + manhattan_algorithm_y # O(1)

                if manhattan_algorithm <= self.brush_size : # O(1)
                    if not(x_cord < 0 or y_cord < 0 or x_cord >= self.x or y_cord >= self.y) : # O(1)
                        if self.grid[x_cord][y_cord].add(layer) : # BCS: O(1)   WCS: O(1) 
                            paint_action.add_step(PaintStep((x_cord, y_cord), layer)) # O(1)
        
        # Return the object paint_action
        return paint_action # O(1)

    def __getitem__(self, i: int) -> LayerStore : 
        """
        Magic method is used for accessing an item from the invoked instances' attribute

        Args:
        - i: index

        Returns:
        - grid[i]: instance of layer store

        Complexity:
        - Worst case: O(1), which gets the item from the array with an index
        - Best case: O(1), which gets the item for the arrat with an index
        """

        return self.grid[i] # O(1)
