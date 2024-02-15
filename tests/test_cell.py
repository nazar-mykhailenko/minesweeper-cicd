import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import pytest
from cell import Cell, CellState

class TestCell:
    def test_cell_is_closed_after_constructor_call(self):
        # Arrange, Act
        cell = Cell(False)
        # Assert
        assert cell.state == CellState.CLOSED

    def test_cell_has_mine_is_correct(self):
        # Arrange, Act
        cell_with_mine = Cell(True)
        cell_without_mine = Cell(False)
        # Assert
        assert cell_with_mine.has_mine
        assert not cell_without_mine.has_mine

    def test_toggle_flag_changes_cell_state_when_cell_is_closed(self):
        # Arrange
        cell = Cell(False)
        # Act
        cell.toggle_flag()
        # Assert
        assert cell.state == CellState.FLAGGED
        # Act
        cell.toggle_flag()
        # Assert
        assert cell.state == CellState.CLOSED

    def test_toggle_flag_doesnt_change_state_when_cell_is_open(self):
        # Arrange
        cell = Cell(False)
        cell.try_open()
        # Act
        cell.toggle_flag()
        # Assert
        assert cell.state == CellState.OPEN

    def test_try_open_cell_opens_cell_when_cell_isnt_flagged(self):
        # Arrange
        cell = Cell(False)
        # Act
        cell.try_open()
        # Assert
        assert cell.state == CellState.OPEN

    def test_try_open_cell_doesnt_open_cell_when_cell_is_flagged(self):
        # Arrange
        cell = Cell(False)
        cell.toggle_flag()
        # Act
        cell.try_open()
        # Assert
        assert cell.state == CellState.FLAGGED
