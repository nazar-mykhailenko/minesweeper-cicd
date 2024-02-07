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
        self.difficulty = difficulty
        self.minefield = Minefield(difficulty.value[0], difficulty.value[2])
        self.game_state = GameState.IN_PROGRESS
        self.record_manager = RecordManager()
        self.menu_open = False
        self.renderer = Renderer(self.minefield)
        # Tuples should be replaced with Rects for each respective element
        # Rects can be retrieved from the renderer which is None for now
        # HACK: find a better way to retrieve the Rects?
        self.clickable_elements = {
            self.on_menu_button_click: self.renderer.get_menu_button_coords(),
            self.on_restart_button_click: (0, 0, 0, 0),
            self.on_stats_button_click: (0, 0, 0, 0),
            self.on_minefield_click: self.renderer.get_field_coords(),
        }

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event, pygame.mouse.get_pos())

            self.renderer.draw(clock.get_time())
            clock.tick(FPS)



    def restart_game(self):
        pass


    def toggle_menu(self):
        pass


    # Not sure if this belongs here
    def show_stats(self):
        pass


    def click_cell(self, x, y, mouse_button):
        if mouse_button == LEFT_MOUSE_BUTTON:
            self.minefield.open_cell(x, y)
        elif mouse_button == RIGHT_MOUSE_BUTTON:
            self.minefield.flag_cell(x, y)


    def handle_click(self, event, mouse_pos):
        for func, rect in self.clickable_elements.items():
            if self.is_point_in_rect(mouse_pos, rect):
                func(event, mouse_pos)


    def on_menu_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON:
            self.toggle_menu()


    def on_restart_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open:
            self.restart_game()


    def on_stats_button_click(self, event, _):
        if event.button == LEFT_MOUSE_BUTTON and self.menu_open:
            self.show_stats()


    def on_minefield_click(self, event, mouse_pos):
        if self.menu_open or self.game_state != GameState.IN_PROGRESS:
            return

        left, top, width, height = self.clickable_elements[self.on_minefield_click]
        x, y = mouse_pos
        cell_width = width // self.minefield.size
        cell_height = height // self.minefield.size
        cell_x = (x - left) // cell_width
        cell_y = (y - top) // cell_height
        self.click_cell(cell_x, cell_y, event.button)


    def is_point_in_rect(self, point, rect):
        x, y = point
        left, top, width, height = rect
        return left <= x <= left + width and top <= y <= top + height
