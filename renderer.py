import pygame
from cell import Cell, CellState
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
        self.tiles = sprites.TileBuilder(sprites.TileSheets(sprites.TileSheets.two_thousand)).build()

    def draw(self, time: int):
        self.win.fill((192, 192, 192))
        self.draw_menu_button()
        self.draw_header(time)
        self.draw_field()
        pygame.display.update()

    def get_menu_button_coords(self):
        menu_button_size = 23
        return (self.window_width // 2 - menu_button_size//2, 10, menu_button_size, menu_button_size)

    def draw_menu_button(self):
        menu_button_coords = self.get_menu_button_coords()
        icon_path = 'assets/menu_button.png'
        icon = pygame.image.load(icon_path)
        self.win.blit(icon, menu_button_coords[:2])

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
        for i in range(self.field.cells.__len__()):
            for j in range(self.field.cells[i].__len__()):
                cell = self.field.cells[i][j]
                self.draw_cell(cell, i, j)

    def draw_cell(self, cell : Cell, i, j):
        x = j * TILE_SIZE
        y = i * TILE_SIZE + HEADER_SIZE
        match cell.state:
            case CellState.CLOSED:
                self.win.blit(self.tiles.unopened, (x, y))
            case CellState.FLAGGED:
                self.win.blit(self.tiles.flag, (x, y))
            case CellState.OPEN:
                if cell.has_mine:
                    self.win.blit(self.tiles.mine, (x, y))
                else:
                    mines_num = self.field.get_number_of_mines_around_cell(i, j) 
                    self.win.blit(self.tiles[mines_num], (x, y))

    def get_field_coords(self):
        return (0, HEADER_SIZE, self.window_width, self.window_height - HEADER_SIZE)