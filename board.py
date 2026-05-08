class Board:
    def __init__(self, grid):
        self.grid = grid

    def display(self):
        for row in self.grid:
            print(row)

    def find_start(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 2:
                    return (i, j)

    def is_valid_position(self, position):

        row, col = position

        if row < 0 or row >= len(self.grid):
            return False

        if col < 0 or col >= len(self.grid[0]):
            return False

        if self.grid[row][col] == 0:
            return False

        return True


    def is_valid_block(self, block):

        return (
            self.is_valid_position(block.pos1)
            and
            self.is_valid_position(block.pos2)
        )

    def is_win(self, block):

        if block.get_orientation() != "standing":
            return False

        row, col = block.pos1

        return self.grid[row][col] == 9