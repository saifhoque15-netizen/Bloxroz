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

        if block.pos1 is None or block.pos2 is None:
            return False

        r1, c1 = block.pos1
        r2, c2 = block.pos2

        rows = len(self.grid)
        cols = len(self.grid[0])

        if not (0 <= r1 < rows and 0 <= c1 < cols):
            return False

        if not (0 <= r2 < rows and 0 <= c2 < cols):
            return False

        if self.grid[r1][c1] == 0:
            return False

        if self.grid[r2][c2] == 0:
            return False

        return True

    def is_win(self, block):

        if block.pos1 is None or block.pos2 is None:
            return False

        row, col = block.pos1

        if block.get_orientation() == "standing":

            return self.grid[row][col] == 9

        return False