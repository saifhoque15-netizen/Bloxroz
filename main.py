# from board import Board


# board_data = [
#     [1, 1, 1],
#     [1, 2, 1],
#     [1, 1, 9]
# ]


# board = Board(board_data)

# board.display()


# start = board.find_start()

# print(start)





# from block import Block
# block = Block(start)

# block.display()


# print(block.get_orientation())

# # block.move_right()

# # block.display()

# # print(block.get_orientation())



# # block.move_right()
# # block.move_right()

# # block.display()

# # print(block.get_orientation())




# block.move_left()
# block.move_left()

# block.display()

# print(block.get_orientation())



# # block.move_down()

# # block.display()

# # print(block.get_orientation())

# print(board.is_valid_block(block))


# print(board.is_win(block))




# from game import Game


# board_data = [
#     [1,1,1,1,1],
#     [1,1,1,1,1],
#     [1,1,2,1,1],
#     [1,1,1,1,9],
#     [1,1,1,1,1]
# ]

# game = Game(board_data)


# game.play()




from game import Game
from level import LEVELS
from solver import bfs

game = Game(LEVELS)

# game.play()

for i in range(len(LEVELS)):

    game.current_level = i

    game.load_level()

    print("Level", i + 1)

    solution = bfs(game.board, game.block)

    print(solution)
    

