import pygame

from minefield import Minefield

class Renderer():
    def __init__(self, field : Minefield) -> None:
        self.field = field

    def draw(self, time : int):
        self.draw_header(time)
        self.draw_field()

    def draw_header(self, time : int):
        self.draw_timer(time)
        self.draw_flags_remaining()

    def draw_timer(self, time : int):
        pass

    def draw_flags_remaining(self):
        pass

    def draw_field(self):
        pass
