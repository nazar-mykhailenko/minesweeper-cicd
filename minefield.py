import cell

class Minefield:
    def __init__(self, size, bomb_count):
        self.size = size
        self.bomb_count = bomb_count
        self.cells = [[]]
