import time
import copy
from collections import deque 

def bfs(board, block):

    queue = deque()

    visited = set()

    start_state = block.get_state()

    queue.append((block, []))

    visited.add(start_state)

    print("Start State:", start_state)

    moves={"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    start_time = time.time()
    explored_states = 0
    max_depth = 0
    while queue:

        current_block, path = queue.popleft()
        explored_states += 1
        max_depth = max(max_depth, len(path))
        current_state = current_block.get_state()

        if board.is_win(current_block):
            print("Solution Found:", path)
            print("States Explored:", explored_states)
            print("Max Depth:", max_depth)
            end_time = time.time()
            print("Time Taken:", end_time - start_time)
            return path

        for move_name, (dr, dc) in moves.items():

            new_block = copy.deepcopy(current_block)

            if move_name == "u":
                new_block.move_up()
            elif move_name == "d":
                new_block.move_down()
            elif move_name == "l":
                new_block.move_left()
            elif move_name == "r":
                new_block.move_right()

            new_state = new_block.get_state()

            if board.is_valid_block(new_block) and new_state not in visited:
                visited.add(new_state)
                new_path = path + [move_name]
                queue.append((new_block, new_path))
    

    