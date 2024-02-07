import pygame
from cell import Cell, CellState
from minesweeper import sprites
from minefield import Minefield

TILE_SIZE = 16
HEADER_SIZE = 100
MENU_BUTTON_SIZE = 56


class Renderer():
    def __init__(self, field: Minefield) -> None:
        self.field = field
        self.window_width = field.cells.__len__() * TILE_SIZE
        self.window_height = self.window_width + HEADER_SIZE
        self.win = pygame.display.set_mode(
            (self.window_width, self.window_height))
        self.score = sprites.ScoreBuilder().build()
        self.tiles = sprites.TileBuilder(sprites.TileSheets(
            sprites.TileSheets.two_thousand)).build()
        self.menu_button_x_offset = (
            self.window_width - 2 * MENU_BUTTON_SIZE) // 3
        self.menu_button_y_offset = (
            self.window_height - 2 * MENU_BUTTON_SIZE) // 3

    def draw(self, time: int):
        self.update_screen()
        self.draw_menu_button()
        self.draw_header(time)
        self.draw_field()

    def update_screen(self):
        pygame.display.update()
        self.win.fill((192, 192, 192))

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
            self.win.blit(
                sprite, (timer_coords[0] + i * digit_width, timer_coords[1]))

    def get_number_sprite(self, number: str):
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
            self.win.blit(
                sprite, (flag_counter_coords[0] - i * digit_width, flag_counter_coords[1]))

    def draw_field(self):
        for x in range(self.field.size):
            for y in range(self.field.size):
                cell = self.field.get_cell(x, y)
                self.draw_cell(cell, x, y)
        # for i in range(self.field.cells.__len__()):
        #     for j in range(self.field.cells[i].__len__()):
        #         cell = self.field.cells[i][j]
        #         self.draw_cell(cell, i, j)

    def draw_cell(self, cell: Cell, i, j):
        x = i * TILE_SIZE
        y = j * TILE_SIZE + HEADER_SIZE
        match cell.state:
            case CellState.CLOSED:
                self.win.blit(self.tiles.unopened, (x, y))
            case CellState.FLAGGED:
                self.win.blit(self.tiles.flag, (x, y))
            case CellState.OPEN:
                if cell.has_mine:
                    self.win.blit(self.tiles.mine, (x, y))
                else:
                    mines_num = self.field.get_number_of_mines_around_cell(
                        i, j)
                    self.win.blit(self.tiles[mines_num], (x, y))

    def get_field_coords(self):
        return (0, HEADER_SIZE, self.window_width, self.window_height - HEADER_SIZE)

    def draw_menu(self):
        self.update_screen()
        self.draw_restart_button()
        self.draw_exit_button()
        self.draw_resume_button()
        self.draw_stats_button()

    def draw_stats(self, records: list[str]):
        self.update_screen()

    def get_restart_button_coords(self):
        return (self.window_width - MENU_BUTTON_SIZE - self.menu_button_x_offset, self.menu_button_y_offset,
                 MENU_BUTTON_SIZE, MENU_BUTTON_SIZE)

    def get_resume_button_coords(self):
        return (self.menu_button_x_offset, self.menu_button_y_offset, MENU_BUTTON_SIZE, MENU_BUTTON_SIZE)

    def get_exit_button_coords(self):
        return (self.window_width - MENU_BUTTON_SIZE - self.menu_button_x_offset,
                self.window_height - MENU_BUTTON_SIZE - self.menu_button_y_offset, MENU_BUTTON_SIZE, MENU_BUTTON_SIZE)

    def get_stats_button_coords(self):
        return (self.menu_button_x_offset, self.window_height - MENU_BUTTON_SIZE - self.menu_button_y_offset,
                 MENU_BUTTON_SIZE, MENU_BUTTON_SIZE)

    def draw_restart_button(self):
        restart_button_coords = self.get_restart_button_coords()
        icon_path = 'assets/restart_button.png'
        icon = pygame.image.load(icon_path)
        self.win.blit(icon, restart_button_coords[:2])

    def draw_exit_button(self):
        exit_button_coords = self.get_exit_button_coords()
        icon_path = 'assets/exit_button.png'
        icon = pygame.image.load(icon_path)
        self.win.blit(icon, exit_button_coords[:2])

    def draw_resume_button(self):
        resume_button_coords = self.get_resume_button_coords()
        icon_path = 'assets/resume_button.png'
        icon = pygame.image.load(icon_path)
        self.win.blit(icon, resume_button_coords[:2])

    def draw_stats_button(self):
        stats_button_coords = self.get_stats_button_coords()
        icon_path = 'assets/stats_button.png'
        icon = pygame.image.load(icon_path)
        self.win.blit(icon, stats_button_coords[:2])
