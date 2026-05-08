from board import Board
from block import Block
from level import LEVELS
from colorama import Fore, Style, init  
init(autoreset=True)


class Game:

    def __init__(self, levels):

        self.levels = levels

        self.current_level = 0

        self.load_level()

    def load_level(self):

        grid = self.levels[self.current_level]

        self.board = Board(grid)

        start = self.board.find_start()

        self.block = Block(start)

        self.moves = 0
    

    def display_state(self):

        self.board.display()

        self.block.display()

        print("Orientation:", self.block.get_orientation())


    def move_block(self, direction):

        if direction == "r":
            self.block.move_right()

        elif direction == "l":
            self.block.move_left()

        elif direction == "u":
            self.block.move_up()

        elif direction == "d":
            self.block.move_down()



    def play(self):

        while True:

            self.display_state()

            move = input("Move (r/l/u/d): ")

            self.move_block(move)

            self.moves += 1

            if not self.board.is_valid_block(self.block):

                print(Fore.RED + "You lost!" + Style.RESET_ALL) ## Help from AI

                self.load_level()

                continue

            if self.board.is_win(self.block):

                print(Fore.GREEN + "Level completed!" + Style.RESET_ALL) ## Help from AI

                self.current_level += 1

                if self.current_level >= len(self.levels):

                    print(Fore.CYAN + "You finished all levels!" + Style.RESET_ALL) ## Help from AI

                    break

                else:

                    self.load_level()






    def display_state(self):

        for i in range(len(self.board.grid)):

            for j in range(len(self.board.grid[i])):

                position = (i, j)

                if (
                    position == self.block.pos1
                    or
                    position == self.block.pos2
                ):

                    print(Fore.BLUE + "B" + Style.RESET_ALL, end=" ") ## Help from AI

                else:

                    tile = self.board.grid[i][j]

                    if tile == 1:
                        print(Fore.WHITE + "." + Style.RESET_ALL, end=" ") ## Help from AI

                    elif tile == 0:
                        print(Fore.RED + "X" + Style.RESET_ALL, end=" ") ## Help from AI

                    elif tile == 2:
                        print(Fore.GREEN + "S" + Style.RESET_ALL, end=" ") ## Help from AI

                    elif tile == 9:
                        print(Fore.YELLOW + "G" + Style.RESET_ALL, end=" ") ## Help from AI

            print()

        print()

        print("Position 1:", self.block.pos1)
        print("Position 2:", self.block.pos2)
        print("Orientation:", self.block.get_orientation())
        print("Moves:", self.moves)