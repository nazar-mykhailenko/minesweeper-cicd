import random
from cell import Cell

class Minefield:
    def __init__(self, size, bomb_count):
        self.size = size
        self.bomb_count = bomb_count
        self.cells = self.initialize_cells()

    def initialize_cells(self):
        list = []
        for _ in range(self.bomb_count):
            list.append(Cell(True))

        for _ in range(self.size - self.bomb_count):
            list.append(Cell(False))

        random.shuffle(list)
        return [list[i:i+self.size] for i in range(0, len(list), self.size)]

    def get_cell(self, x, y) -> Cell:
        return self.cells[x][y]

    # TODO:
    def open_cell(self, x, y):
        pass

    def flag_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.toggle_flag()

    # TODO: return a GameState enum
    def get_game_state(self):
        pass
