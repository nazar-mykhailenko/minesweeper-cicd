import random
from cell import Cell, CellState
from enum import Enum


class GameState(Enum):
    LOST = 0
    WON = 1
    IN_PROGRESS = 2


class Minefield:
    def __init__(self, size, mine_count):
        self.size = size
        self.mine_count = mine_count
        self.cells = self.initialize_cells()

    def initialize_cells(self):
        list = []
        for _ in range(self.mine_count):
            list.append(Cell(True))

        cell_count = self.size * self.size
        for _ in range(cell_count - self.mine_count):
            list.append(Cell(False))

        random.shuffle(list)
        return [list[i:i+self.size] for i in range(0, len(list), self.size)]

    def get_cell(self, x, y) -> Cell:
        return self.cells[x][y]

    def open_cell(self, x, y):
        cell = self.get_cell(x, y)
        if not cell.try_open() or cell.has_mine:
            return

        queue = [(x, y)]
        visited = set()
        while len(queue) > 0:
            current_point = queue.pop(0)
            visited.add(current_point)
            current_cell = self.get_cell(current_point[0], current_point[1])
            if current_cell.has_mine:
                continue

            current_cell.try_open()
            neighboring_points = self.get_neighboring_points(current_point[0], current_point[1])
            neighboring_mine_count = self.count_cells_with_mines(neighboring_points)
            if neighboring_mine_count > 0:
                continue

            for point in neighboring_points:
                if point not in visited:
                    queue.append(point)

    def flag_cell(self, x, y):
        cell = self.get_cell(x, y)
        flagged_count = self.count_flagged_cells()
        if flagged_count >= self.mine_count and cell.state == CellState.CLOSED:
            return

        cell.toggle_flag()

    def get_game_state(self) -> GameState:
        total_count = self.size * self.size
        flagged_count = 0
        open_count = 0
        for x in range(self.size):
            for y in range(self.size):
                cell = self.get_cell(x, y)
                if cell.state == CellState.OPEN:
                    if cell.has_mine:
                        return GameState.LOST

                    open_count += 1
                elif cell.state == CellState.FLAGGED:
                    flagged_count += 1

        if open_count + flagged_count == total_count:
            return GameState.WON

        return GameState.IN_PROGRESS


    def get_number_of_mines_around_cell(self, x, y) -> int:
        neighboring_points = self.get_neighboring_points(x, y)
        return neighboring_points.count(lambda p: self.get_cell(p[0], p[1]).has_mine)

    def get_neighboring_points(self, x, y):
        points = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                cell_x, cell_y = x + dx, y + dy
                if cell_x < 0 or cell_x >= self.size or cell_y < 0 or cell_y >= self.size:
                    continue

                points.append((cell_x, cell_y))

        return points

    def count_cells_with_mines(self, points) -> int:
        return points.count(lambda p: self.get_cell(p[0], p[1]).has_mine)

    def count_flagged_cells(self) -> int:
        count = 0
        for x in range(self.size):
            for y in range(self.size):
                cell = self.get_cell(x, y)
                if cell.state == CellState.FLAGGED:
                    count += 1

        return count
