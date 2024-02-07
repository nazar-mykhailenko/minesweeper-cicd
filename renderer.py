import pygame
from minesweeper import sprites

from minefield import Minefield
TILE_SIZE = 16
HEADER_SIZE = 100


class Renderer():
    def __init__(self, field: Minefield) -> None:
        self.field = field
        self.window_width = field.cells.__len__() * TILE_SIZE
        self.window_height = self.window_width + HEADER_SIZE
        self.win = pygame.display.set_mode(
            (self.window_width, self.window_height))
        self.score = sprites.ScoreBuilder().build()

    def draw(self, time: int):
        self.win.fill((192, 192, 192))
        self.draw_header(time)
        self.draw_field()
        pygame.display.update()

    def draw_header(self, time: int):
        self.draw_timer(time)
        self.draw_flags_remaining()

    def draw_timer(self, time: int):
        timer_coords = (10, 10)
        digit_width = 13
        time_str = str(time)
        for i in range(time_str.__len__()):
            sprite = self.get_number_sprite(time_str[i])
            self.win.blit(sprite, (timer_coords[0] + i * digit_width, timer_coords[1]))
        
    def get_number_sprite(self, number : str):
        match number:
            case '1':
                return self.score.one
            case '2':
                return self.score.two
            case '3':
                return self.score.three
            case '4':
                return self.score.four
            case '5':
                return self.score.five
            case '6':
                return self.score.six
            case '7':
                return self.score.seven
            case '8':
                return self.score.eight
            case '9':
                return self.score.nine
            case '0':
                return self.score.zero
            case _:
                return self.score.zero

    def draw_flags_remaining(self):
        flag_counter_coords = (self.window_width - 20, 10)
        digit_width = 13
        flag_count = self.field.mine_count - self.field.count_flagged_cells()
        flag_count_str = str(flag_count)[::-1]
        for i in range(flag_count_str.__len__()):
            sprite = self.get_number_sprite(flag_count_str[i])
            self.win.blit(sprite, (flag_counter_coords[0] - i * digit_width, flag_counter_coords[1]))
    def draw_field(self):
        pass
