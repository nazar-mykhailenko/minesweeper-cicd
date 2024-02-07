import pygame
from minefield import Minefield, GameState
from record_manager import RecordManager
from difficulty import Difficulty
from renderer import Renderer

FPS = 60
LEFT_MOUSE_BUTTON = 1
RIGHT_MOUSE_BUTTON = 3

class GameManager:
    def __init__(self, difficulty: Difficulty):
        self.start_time = 0
        self.running = True
        self.menu_open = False
        self.stats_open = False
        self.game_state = GameState.IN_PROGRESS
        self.difficulty = difficulty

        self.minefield = Minefield(difficulty.value[0], difficulty.value[2])
        self.record_manager = RecordManager()
        self.renderer = Renderer(self.minefield)

        # HACK: find a better way to retrieve the Rects?
        self.clickable_elements = {
            self.on_minefield_click: self.renderer.get_field_coords(),
            self.on_menu_button_click: self.renderer.get_menu_button_coords(),
            self.on_exit_button_click: self.renderer.get_exit_button_coords(),
            self.on_resume_button_click: self.renderer.get_resume_button_coords(),
            self.on_restart_button_click: self.renderer.get_restart_button_coords(),
            self.on_stats_button_click: self.renderer.get_stats_button_coords(),
        }

    def run_game(self):
        self.start_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()
        seconds_elapsed = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event, pygame.mouse.get_pos())

            clock.tick(FPS)
            if self.game_state == GameState.IN_PROGRESS:
                seconds_elapsed = (pygame.time.get_ticks() - self.start_time) // 1000

            if self.menu_open:
                if self.stats_open:
                    self.renderer.draw_stats(self.record_manager.get_records(self.difficulty))
                else:
                    self.renderer.draw_menu()
            else:
                self.renderer.draw(seconds_elapsed)

            self.game_state = self.minefield.get_game_state()


    def restart_game(self):
        self.game_state = GameState.IN_PROGRESS
        self.start_time = pygame.time.get_ticks()
        size = self.minefield.size
        mine_count = self.minefield.mine_count
        self.minefield = Minefield(size, mine_count)
        self.renderer.field = self.minefield


    def click_cell(self, x, y, mouse_button):
        if mouse_button == LEFT_MOUSE_BUTTON:
            self.minefield.open_cell(x, y)
            return True
        elif mouse_button == RIGHT_MOUSE_BUTTON:
            self.minefield.flag_cell(x, y)
            return True

        return False


    def handle_click(self, event, mouse_pos):
        for func, rect in self.clickable_elements.items():
            if self.is_point_in_rect(mouse_pos, rect):
                if func(event, mouse_pos):
                    break


    def on_menu_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and not self.stats_open:
            self.menu_open = True
            return True

        return False


    def on_restart_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open and not self.stats_open:
            self.restart_game()
            self.menu_open = False
            return True

        return False


    def on_resume_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open and not self.stats_open:
            self.menu_open = False
            return True

        return False


    def on_exit_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open and not self.stats_open:
            self.running = False
            return True

        return False


    def on_stats_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open and not self.stats_open:
            self.stats_open = True
            return True

        return False


    def on_minefield_click(self, event, mouse_pos):
        if self.menu_open or self.stats_open or self.game_state != GameState.IN_PROGRESS:
            return False

        left, top, width, height = self.clickable_elements[self.on_minefield_click]
        x, y = mouse_pos
        cell_width = width // self.minefield.size
        cell_height = height // self.minefield.size
        cell_x = (x - left) // cell_width
        cell_y = (y - top) // cell_height
        return self.click_cell(cell_x, cell_y, event.button)


    def is_point_in_rect(self, point, rect):
        x, y = point
        left, top, width, height = rect
        return left <= x <= left + width and top <= y <= top + height
