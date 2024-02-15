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
