from enum import Enum
from minefield import Minefield


class MouseButton(Enum):
    LEFT = 1
    RIGHT = 2


class GameInputHandler:
    def __init__(self, minefield: Minefield, minefield_rec):
        self.minefield = minefield
        self.minefield_rec = minefield_rec

    def handle_input(self, mouse_button, mouse_pos):
        if mouse_button == MouseButton.LEFT:
            self.handle_left_click(mouse_pos)
        elif mouse_button == MouseButton.RIGHT:
            self.handle_right_click(mouse_pos)


    def handle_left_click(self, mouse_pos):
        point = self.get_clicked_cell_coords(mouse_pos)
        if point is None:
            return

        x, y = point
        self.minefield.open_cell(x, y)


    def handle_right_click(self, mouse_pos):
        point = self.get_clicked_cell_coords(mouse_pos)
        if point is None:
            return

        x, y = point
        self.minefield.flag_cell(x, y)


    def get_clicked_cell_coords(self, mouse_pos):
        x, y = mouse_pos
        left, top, width, height = self.minefield_rec
        if x < left or x > left + width or y < top or y > top + height:
            return None

        cell_width = (width - left) // self.minefield.size
        cell_height = (height - top) // self.minefield.size
        cell_x = (x - left) // cell_width
        cell_y = (y - top) // cell_height
        return (cell_x, cell_y)
