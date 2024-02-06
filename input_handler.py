import pygame
from minefield import Minefield

class InputHandler:
    def __init__(self, minefield: Minefield):
        self.minefield = minefield

    # TODO: also handle when buttons are pressed (or make is a separate function)?
    # or make this accept a pos of the click and a button, not event?
    def handle_input(self, event, minefield_rec):
        if event.type != pygame.MOUSEBUTTONUP:
            return

        if event.button == 1:
            self.handle_left_click(event.pos, minefield_rec)
        elif event.button == 3:
            self.handle_right_click(event.pos, minefield_rec)


    def handle_left_click(self, mouse_pos, minefield_rec):
        point = self.get_clicked_cell_coords(mouse_pos, minefield_rec)
        if point is None:
            return

        x, y = point
        self.minefield.open_cell(x, y)


    def handle_right_click(self, mouse_pos, minefield_rec):
        point = self.get_clicked_cell_coords(mouse_pos, minefield_rec)
        if point is None:
            return

        x, y = point
        self.minefield.flag_cell(x, y)


    def get_clicked_cell_coords(self, mouse_pos, minefield_rec):
        x, y = mouse_pos
        left, top, width, height = minefield_rec
        if x < left or x > left + width or y < top or y > top + height:
            return None

        cell_width = (width - left) // self.minefield.size
        cell_height = (height - top) // self.minefield.size
        cell_x = (x - left) // cell_width
        cell_y = (y - top) // cell_height
        return (cell_x, cell_y)
