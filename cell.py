from enum import Enum

class CellState(Enum):
    CLOSED = 0
    OPEN = 1
    FLAGGED = 2

class Cell:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.state = CellState.CLOSED

    def try_open(self) -> bool:
        if self.state == CellState.FLAGGED:
            return False

        self.state = CellState.OPEN
        return False

    def toggle_flag(self):
        if self.state == CellState.OPEN:
            return
        
        if self.state == CellState.CLOSED:
            self.state = CellState.FLAGGED
        else:
            self.state = CellState.CLOSED
