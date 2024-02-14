import sys, os
# HACK: average python moment
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import pytest
from minefield import Minefield, GameState
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


    @pytest.mark.parametrize("size", [0, -1])
    def test_minefield_raises_error_when_size_is_less_then_one(self, size):
        # Act, Assert
        with pytest.raises(ValueError):
            Minefield(size, 10)


    def test_minefield_raises_error_when_mines_count_is_less_then_zero(self):
        # Act, Assert
        with pytest.raises(ValueError):
            Minefield(10, -1)


    @pytest.mark.parametrize("size, mine_count", [(10, 100 - 8), (10, 100), (10, 1000)])
    def test_minefield_raises_error_when_too_much_mines(self, size, mine_count):
        # Act, Assert
        with pytest.raises(ValueError):
            Minefield(size, mine_count)


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


    def test_open_cell_doesnt_open_mines(self, minefield_mine_in_corner):
        # Act
        minefield_mine_in_corner.open_cell(2, 2)
        # Assert
        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    assert minefield_mine_in_corner.cells[i][j].state == CellState.CLOSED
                else:
                    assert minefield_mine_in_corner.cells[i][j].state == CellState.OPEN


    @pytest.mark.parametrize("x, y", [(-1, 0), (0, -1), (5, 0), (0, 5)])
    def test_open_cell_raises_error_when_out_of_bounds(self, x, y):
        # Arrange
        minefield = Minefield(5, 10)
        # Act, Assert
        with pytest.raises(IndexError):
            minefield.open_cell(x, y)


    def test_get_game_state_returns_in_progress_when_mines_left(self, minefield_mine_in_corner):
        # Arrange
        minefield_mine_in_corner.open_cell(2, 2)
        # Act
        game_state = minefield_mine_in_corner.get_game_state()
        # Assert
        assert game_state == GameState.IN_PROGRESS


    def test_get_game_state_returns_lost_when_opened_mine(self, minefield_mine_in_corner):
        # Arrange
        minefield_mine_in_corner.open_cell(0, 0)
        # Act
        game_state = minefield_mine_in_corner.get_game_state()
        # Assert
        assert game_state == GameState.LOST


    def test_get_game_state_returns_won_when_no_mines_left(self, minefield_mine_in_corner):
        # Arrange
        minefield_mine_in_corner.open_cell(2, 2)
        minefield_mine_in_corner.flag_cell(0, 0)
        # Act
        game_state = minefield_mine_in_corner.get_game_state()
        # Assert
        assert game_state == GameState.WON


    @pytest.fixture
    def minefield_mine_in_corner(self):
        # Arrange
        minefield = Minefield(5, 1)
        minefield.cells = [
            [Cell(True), Cell(False), Cell(False), Cell(False), Cell(False)],
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)],
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)],
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)],
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)],
        ]
        minefield.opened = True
        return minefield

