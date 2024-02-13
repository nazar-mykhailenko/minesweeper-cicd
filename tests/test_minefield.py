import sys, os
# HACK: average python moment
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from minefield import Minefield

class TestMinefield:
    def test_minefield_has_correct_size(self):
        # Arrange
        expected_size = 10
        # Act
        minefield = Minefield(expected_size, 10)
        # Assert
        assert minefield.size == expected_size
        assert len(minefield.cells) == expected_size
        assert len(minefield.cells[0]) == expected_size
