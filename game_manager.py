import pygame
from record_manager import RecordManager

FPS = 60

class GameManager:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.record_manager = RecordManager()
        self.menu_open = False
        self.renderer = None
        self.clickable_elements = []
        # Empty tuples shold be replaced with Rects for each respective element
        # Rects can be retrieved from the renderer which is None for now
        self.clickable_elements.append(((), self.on_menu_button_click))
        self.clickable_elements.append(((), self.on_restart_button_click))
        self.clickable_elements.append(((), self.on_stats_button_click))
        self.clickable_elements.append(((), self.on_minefield_click))


    def run_game(self):
        pass


    def restart_game(self):
        pass


    def toggle_menu(self):
        pass


    # Not sure if this belongs here
    def show_stats(self):
        pass


    def click_cell(self):
        pass


    def handle_click(self):
        pass


    def on_menu_button_click(self, event, mouse_pos):
        pass


    def on_restart_button_click(self, event, mouse_pos):
        pass


    def on_stats_button_click(self, event, mouse_pos):
        pass


    def on_minefield_click(self, event, mouse_pos):
        pass
