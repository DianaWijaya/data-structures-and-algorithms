import arcade.key as keys
import math
from grid import Grid
from layer_util import get_layers, Layer
from layers import lighten
import arcade
from replay import ReplayTracker
from undo import UndoTracker

class MyWindow(arcade.Window):
    """ Painter Window """

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 700
    SIDEBAR_WIDTH = 100
    BUTTONS_HEIGHT = 100
    SCREEN_TITLE = "Paint"

    REPLAY_TIMER_DELTA = 0.05

    GRID_SIZE_X = 32
    GRID_SIZE_Y = 32

    BG = [255, 255, 255]

    # SCAFFOLD PART
    # Unless you're adding new features, you shouldn't need to touch this.

    def __init__(self) -> None:
        """Initialise visual and logic variables."""
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        arcade.set_background_color(self.BG)
        self.grid: Grid = None
        self.draw_style = Grid.DRAW_STYLE_SET
        self.z_pressed = False
        self.y_pressed = False
        self.z_timer = 0
        self.y_timer = 0
        self.enable_ui = True
        self.replay_timer = 0
        self.on_init()

    def reset(self) -> None:
        """Reset the screen."""
        self.grid = Grid(self.draw_style, self.GRID_SIZE_X, self.GRID_SIZE_Y)
        self.timestamp = 0

        self.selected_layer_index = -1
        self.dragging = None
        self.prev_drawn = None
        self.prev_pos = None
        self.draw_size = 2

        # Visual calculations
        self.DRAW_PANEL = self.SCREEN_WIDTH - self.SIDEBAR_WIDTH
        self.GRID_SQ_WIDTH = self.DRAW_PANEL / self.GRID_SIZE_X
        self.GRID_SQ_HEIGHT = self.SCREEN_HEIGHT / self.GRID_SIZE_Y
        self.LAYER_BUTTON_SIZE = self.SIDEBAR_WIDTH / 2
        # Action button sprites
        self.action_buttons = arcade.SpriteList()
        self.draw_mode_button = arcade.Sprite(
            "img/on_off.png" if self.draw_style == Grid.DRAW_STYLE_SET else (
                "img/additive.png" if self.draw_style == Grid.DRAW_STYLE_ADD else "img/sequence.png"
            ),
            scale=50/48,
        )
        self.draw_mode_button.center_x = self.DRAW_PANEL + self.LAYER_BUTTON_SIZE / 2
        self.draw_mode_button.center_y = self.LAYER_BUTTON_SIZE / 2
        self.action_buttons.append(self.draw_mode_button)
        self.replay_button = arcade.Sprite(
            "img/replay.png",
            scale=50/48,
        )
        self.replay_button.center_x = self.DRAW_PANEL + 3 * self.LAYER_BUTTON_SIZE / 2
        self.replay_button.center_y = self.LAYER_BUTTON_SIZE / 2
        self.action_buttons.append(self.replay_button)
        self.brush_big_button = arcade.Sprite(
            "img/brush_up.png",
            scale=50/48,
        )
        self.brush_big_button.center_x = self.DRAW_PANEL + self.LAYER_BUTTON_SIZE / 2
        self.brush_big_button.center_y = 3 * self.LAYER_BUTTON_SIZE / 2
        self.action_buttons.append(self.brush_big_button)
        self.brush_small_button = arcade.Sprite(
            "img/brush_down.png",
            scale=50/48,
        )
        self.brush_small_button.center_x = self.DRAW_PANEL + 3 * self.LAYER_BUTTON_SIZE / 2
        self.brush_small_button.center_y = 3 * self.LAYER_BUTTON_SIZE / 2
        self.action_buttons.append(self.brush_small_button)
        self.special_button = arcade.Sprite(
            "img/special.png",
            scale=50/48,
        )
        self.special_button.center_x = self.DRAW_PANEL + self.LAYER_BUTTON_SIZE / 2
        self.special_button.center_y = 5 * self.LAYER_BUTTON_SIZE / 2
        self.action_buttons.append(self.special_button)

        self.on_reset()

    def setup(self) -> None:
        """Set up the game and initialize the variables."""
        self.reset()

    def on_draw(self) -> None:
        """Draw everything"""
        self.clear()
        # UI - Layers
        for i, layer in enumerate(get_layers()):
            if layer is None: break
            xstart = (i % 2) * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            xend = ((i % 2)+1) * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = self.SCREEN_HEIGHT - (i//2) * self.LAYER_BUTTON_SIZE
            yend = self.SCREEN_HEIGHT - (i//2+1) * self.LAYER_BUTTON_SIZE
            bg = lighten.apply(layer.bg or self.BG[:], 0, 0, 0) if self.selected_layer_index == i else (layer.bg or self.BG[:])
            if not self.enable_ui:
                bg = lighten.apply(bg, 0, 0, 0)
            arcade.draw_lrtb_rectangle_filled(xstart, xend, ystart, yend, bg)
            arcade.draw_lrtb_rectangle_outline(
                xstart, xend, ystart, yend, (0, 0, 0), border_width=1,
            )
            arcade.draw_text(str(i), xstart, (ystart+yend)/2, (0, 0, 0), 18, width=xend-xstart, align="center", bold=True, anchor_y="center")
        # UI - Draw Modes / Action buttons
        self.action_buttons.draw()
        # Grid
        for x in range(self.GRID_SIZE_X):
            for y in range(self.GRID_SIZE_Y):
                arcade.draw_lrtb_rectangle_filled(
                    self.GRID_SQ_WIDTH * x,
                    self.GRID_SQ_WIDTH * (x+1),
                    self.GRID_SQ_HEIGHT * (y+1),
                    self.GRID_SQ_HEIGHT * y,
                    self.grid[x][y].get_color(self.BG[:], self.timestamp, x, y),
                )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        """Called when the mouse buttons are pressed."""
        if x > self.DRAW_PANEL:
            if not self.enable_ui:
                return
            # Buttons
            for i, layer in enumerate(get_layers()):
                if layer is None: break
                xstart = (i % 2) * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
                xend = ((i % 2)+1) * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
                ystart = self.SCREEN_HEIGHT - (i//2) * self.LAYER_BUTTON_SIZE
                yend = self.SCREEN_HEIGHT - (i//2+1) * self.LAYER_BUTTON_SIZE
                if xstart <= x < xend and yend <= y < ystart:
                    self.selected_layer_index = i
                    break
            # Actions
            xstart = self.DRAW_PANEL
            xend = self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = self.LAYER_BUTTON_SIZE
            yend = 0
            if xstart <= x < xend and yend <= y < ystart:
                self.change_draw_mode()
            xstart = self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            xend = 2 * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = self.LAYER_BUTTON_SIZE
            yend = 0
            if xstart <= x < xend and yend <= y < ystart:
                self.start_replay()
            xstart = self.DRAW_PANEL
            xend = self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = 2 * self.LAYER_BUTTON_SIZE
            yend = self.LAYER_BUTTON_SIZE
            if xstart <= x < xend and yend <= y < ystart:
                self.on_increase_brush_size()
            xstart = self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            xend = 2 * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = 2 * self.LAYER_BUTTON_SIZE
            yend = self.LAYER_BUTTON_SIZE
            if xstart <= x < xend and yend <= y < ystart:
                self.on_decrease_brush_size()
            xstart = self.DRAW_PANEL
            xend = 1 * self.LAYER_BUTTON_SIZE + self.DRAW_PANEL
            ystart = 3 * self.LAYER_BUTTON_SIZE
            yend = 2 * self.LAYER_BUTTON_SIZE
            if xstart <= x < xend and yend <= y < ystart:
                self.on_special()
        else:
            self.dragging = True
            self.try_draw(x, y)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        """Called when the mouse buttons are released."""
        self.dragging = False
        self.prev_drawn = None
        self.prev_pos = None

    def on_mouse_motion(self, x, y, dx, dy) -> None:
        """Called when the mouse moves."""
        if not self.dragging:
            return
        if not(0 <= self.selected_layer_index < len(get_layers())):
            return
        if x > self.DRAW_PANEL:
            return
        self.try_draw(x, y)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """Called when a keyboard key is pressed."""
        if not self.enable_ui:
            return
        self.z_pressed = keys.Z == symbol and (modifiers & keys.MOD_CTRL)
        self.y_pressed = keys.Y == symbol and (modifiers & keys.MOD_CTRL)
        if self.z_pressed:
            self.on_undo()
            self.z_timer = 0.5
        if self.y_pressed:
            self.on_redo()
            self.y_timer = 0.5

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        """Called when a keyboard key is released."""
        self.z_pressed = False
        self.y_pressed = False

    def try_draw(self, x, y) -> None:
        """Attempt to draw at a position, but safely fail if an invalid square."""
        if self.selected_layer_index == -1:
            return
        layer = get_layers()[self.selected_layer_index]
        if self.prev_pos is not None:
            # Try draw in increments of 0.5 to avoid skipping squares.
            mhat_dist = abs(x - self.prev_pos[0]) + abs(y - self.prev_pos[1])
            increment = 0.5
            points_to_draw = []
            for d in range(1, math.ceil(mhat_dist/increment)+1):
                distance = min(d * increment / mhat_dist, 1)
                nx = distance * (x - self.prev_pos[0]) + self.prev_pos[0]
                ny = distance * (y - self.prev_pos[1]) + self.prev_pos[1]
                nx_pos = int(nx // self.GRID_SQ_WIDTH)
                ny_pos = int(ny // self.GRID_SQ_HEIGHT)
                points_to_draw.append((nx_pos, ny_pos))
        else:
            x_pos = int(x // self.GRID_SQ_WIDTH)
            y_pos = int(y // self.GRID_SQ_HEIGHT)
            points_to_draw = [
                (x_pos, y_pos)
            ]
        for px, py in points_to_draw:
            if self.prev_drawn is None or (px, py) != self.prev_drawn:
                if 0 <= px < self.GRID_SIZE_X and 0 <= py < self.GRID_SIZE_Y:
                    self.on_paint(layer, px, py)
                    self.prev_drawn = (px, py)
        self.prev_pos = (x, y)

    def start_replay(self) -> None:
        """Begin the replay mode."""
        self.enable_ui = False
        self.grid = Grid(self.draw_style, self.GRID_SIZE_X, self.GRID_SIZE_Y)
        self.replay_timer = self.REPLAY_TIMER_DELTA
        self.on_replay_start()

    def on_update(self, delta_time) -> None:
        """Movement and game logic."""
        self.timestamp += delta_time
        if self.z_pressed:
            self.z_timer -= delta_time
            if self.z_timer <= 0:
                self.on_undo()
                self.z_timer += 0.05
        if self.y_pressed:
            self.y_timer -= delta_time
            if self.y_timer <= 0:
                self.on_redo()
                self.y_timer += 0.05
        if not self.enable_ui:
            self.replay_timer -= delta_time
            if self.replay_timer <= 0:
                self.replay_timer += self.REPLAY_TIMER_DELTA
                finished = self.on_replay_next_step()
                if finished:
                    self.enable_ui = True

    def change_draw_mode(self) -> None:
        """Changes the draw mode of the application, and resets the window."""
        if self.draw_style == Grid.DRAW_STYLE_SET:
            self.draw_style = Grid.DRAW_STYLE_ADD
        elif self.draw_style == Grid.DRAW_STYLE_ADD:
            self.draw_style = Grid.DRAW_STYLE_SEQUENCE
        elif self.draw_style == Grid.DRAW_STYLE_SEQUENCE:
            self.draw_style = Grid.DRAW_STYLE_SET
        self.reset()

    # STUDENT PART

    def on_init(self) -> None:
        """
        Initialisation that occurs after the system initialisation

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which occurs when arrayStack and circular queue is created, with a fixed amount of elements
        - Best case: O(1), which occurs when arrayStack and circular queue is created, with a fixed amount of elements
        """

        self.undo_class = UndoTracker() # O(n)
        self.replay_class = ReplayTracker() # O(n)

    def on_reset(self) -> None:
        """
        Called when a window reset is requested

        Returns:
        - None

        Complexity:
        - Worst case: O(1), which occurs when arrayStack and circular queue is created, with a fixed amount of elements
        - Best case: O(1), which occurs when arrayStack and circular queue is created, with a fixed amount of elements
        """

        self.on_init()

    def on_paint(self, layer: Layer, px, py) -> None:
        """
        Called when a grid square is clicked on, which should trigger painting in the vicinity.
        Vicinity squares outside of the range [0, GRID_SIZE_X) or [0, GRID_SIZE_Y) can be safely ignored.

        Args:
        - layer: The layer being applied
        - px: x position of the brush
        - py: y position of the brush

        Returns:
        - None

        Complexity:
        - Worst case: O(n^2), this happens when the worst case scenario of painting grid occurs. In this 
          case, n is the amount of times the for loop of manhattan distance occurs for the x coordinate 
          and y coordinate, which is the same amount of time. Then, for the add function, the worst case 
          scenario is O(1), for every sequence layer 
        - Best case: O(n^2), this happens only when the best case scenario of painting grid occurs. In this
          case, n is the amount of times the for loop of manhattan distance occurs for the x coordinate and 
          y coordinate, which is the same amount of time. This happens if the final coordinate is out of 
          range (exp: (-1, 4)), so the color does not apply to that
        """

        on_paint = self.grid.paint_grid(layer, px, py) # WCS: O(n^2)   BCS: O(n^2)
        self.undo_class.add_action(on_paint) # WCS & BCS: O(1)
        self.replay_class.add_action(on_paint) # WCS: O(n)   BCS: O(1)

    def on_undo(self) -> None:
        """
        Called when an undo is requested.

        Returns:
        - None

        Complexity:
        - Worst case: O(mn o log(p)), which occurs when undo from undo_class is applied to the grid, and is_special is True, 
          which leads to the special function from SequenceLayerStore being the worst case scenario. In this case, m is the 
          amount of times it loops through the width of the grid, n is the amount of times it loops through the length of the 
          grid, and in special function, o is amount of times it loops through based on the length of layers, and log(p) 
          occurs when the the index of that layer exists in the BSet, that layer is added into the temporary array sorted 
          list, in add function, the position of the index is to be found using the function _index_to_add, which iterates 
          logarithmically, because it involves halving the number of elements in an array
        - Best case: O(1), which occurs when the undo_list is empty, nothing happens so None is returned immediately
        """

        self.replay_class.add_action(self.undo_class.undo(self.grid), True) # O(m log(n))

    def on_redo(self) -> None:
        """
        Called when a redo is requested

        Returns:
        - None

        Complexity:
        - Worst case: O(mn o log(p)), which occurs when redo from undo_class is applied to the grid, and is_special is True, which 
          leads to the special function from SequenceLayerStore being the worst case scenario. In this case, m is the amount
          of times it loops through the width of the grid, n is the amount of times it loops through the length of the 
          grid, and in special function, o is amount of times it loops through based on the length of layers, and log(p) 
          occurs when the the index of that layer exists in the BSet, that layer is added into the temporary array sorted 
          list, in add function, the position of the index is to be found using the function _index_to_add, which iterates 
          logarithmically, because it involves halving the number of elements in an array
        - Best case: O(1), which occurs when the redo_list is empty, nothing is done and None is returned
        """

        self.replay_class.add_action(self.undo_class.redo(self.grid)) # O(m log(n))

    def on_special(self) -> None:
        """
        Called when the special action is requested

        Returns:
        - None

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

        special_function = self.grid.special() # WCSL: O(mno log(p))   BCS: O(mn)
        self.undo_class.add_action(special_function) # O(1)
        self.replay_class.add_action(special_function) # WCS: O(n)   BCS: O(1)

    def on_replay_start(self) -> None:
        """
        Called when the replay starting is requested

        Returns:
        - None

        Complexity:
        - Worst case: O(1), not accessed
        - Best case: O(1), not accessed
        """

        self.replay_class.start_replay() # O(1)

    def on_replay_next_step(self) -> bool:
        """
        Called when the next step of the replay is requested. Returns whether the replay is finished

        Returns:
        - boolean value to indicate whether the replay is finished

        Complexity:
        - Worst case: O(mn o log(p)), in play_next_action, when undo_apply or redo_apply is applied to the grid, and 
          is_special is True, which leads to the special function from SequenceLayerStore being the worst case scenario. 
          In this case, m is the amount of times it loops through the width of the grid, n is the amount of times it 
          loops through the length of the grid, and in special function, o is amount of times it loops through based on 
          the length of layers, and log(p) occurs when the the index of that layer exists in the BSet, that layer 
          is added into the temporary array sorted list, in add function, the position of the index is to be found 
          using the function _index_to_add, which iterates logarithmically, because it involves halving the number 
          of elements in an array
        - Best case: O(1), which occurs when the circular queue is empty, so no actions are to be replayed, so nothing 
          happens and True is returned
        """

        return self.replay_class.play_next_action(self.grid) # BCS: O(1)   WCS: O(mn o log(p))

    def on_increase_brush_size(self) -> None:
        """
        Called when an increase to the brush size is requested

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where 1 operation happens when brush size is lesser than the maximum brush
          size, and brush size is increased by 1
        - Best case: O(1), where 1 operation happens when brush size is the maximum brush size or more, 
          so immidiately pass
        """

        self.grid.increase_brush_size() # O(1)

    def on_decrease_brush_size(self) -> None:
        """
        Called when a decrease to the brush size is requested

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where 1 operation happens when the brush size is more than the minimum brush
          size, and brush size is decreased by 1
        - Best case: O(1), where 1 operation happens when brush size is the minimum brush size, then immidiately
          pass
        """

        self.grid.decrease_brush_size() # O(1)

def main():
    """ Main function """
    window = MyWindow()
    window.setup()
    arcade.run()

def run_with_func(func, pause=False):
    from threading import Thread
    window = MyWindow()
    window.setup()
    if pause:
        _ = input("Press enter to begin test.")
    t = Thread(target=func, args=(window,))
    t.start()
    arcade.run()


if __name__ == "__main__":
    main()
