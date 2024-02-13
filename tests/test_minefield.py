import sys, os
# HACK: average python moment
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from minefield import Minefield
from cell import Cell, CellState

class TestMinefield:
    def test_minefield_has_correct_size(self):
        # Arrange, Act
        expected_size = 10
        minefield = Minefield(expected_size, 10)
        # Assert
        assert minefield.size == expected_size
        assert len(minefield.cells) == expected_size
        assert len(minefield.cells[0]) == expected_size


    def test_minefield_has_correct_number_of_mines(self):
        # Arrange
        expected_mines = 10
        minefield = Minefield(10, expected_mines)
        # Act
        minefield.open_cell(0, 0)
        # Assert
        assert sum(sum(cell.has_mine for cell in row) for row in minefield.cells) == expected_mines


    def test_flag_cell_flags_when_cell_closed(self):
        # Arrange
        minefield = Minefield(10, 10)
        minefield.opened = True
        # Act
        minefield.flag_cell(0, 0)
        # Assert
        assert minefield.cells[0][0].state == CellState.FLAGGED


    def test_flag_cell_doesnt_flag_when_cell_opened(self):
        # Arrange
        minefield = Minefield(10, 10)
        minefield.open_cell(0, 0)
        # Act
        minefield.flag_cell(0, 0)
        # Assert
        assert minefield.cells[0][0].state == CellState.OPEN


    def test_open_cell_opens_most_area(self):
        # Arrange
        minefield = Minefield(5, 16)
        minefield.cells = [
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)],
            [Cell(True), Cell(False), Cell(False), Cell(False), Cell(True)],
            [Cell(True), Cell(False), Cell(False), Cell(False), Cell(True)],
            [Cell(True), Cell(False), Cell(False), Cell(False), Cell(True)],
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)],
        ]
        minefield.opened = True

        # Act
        minefield.open_cell(2, 2)
        # Assert
        for i in range(5):
            for j in range(5):
                if 1 <= i <= 3 and 1 <= j <= 3:
                    assert minefield.cells[i][j].state == CellState.OPEN
                else:
                    assert minefield.cells[i][j].state == CellState.CLOSED
