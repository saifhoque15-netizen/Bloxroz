# import time
# import copy
# from collections import deque 

# def bfs(board, block):

#     queue = deque()

#     visited = set()

#     start_state = block.get_state()
   

#     queue.append((block, []))

#     visited.add(start_state)

#     print("Start State:", start_state)

#     moves={"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
#     start_time = time.time()
#     explored_states = 0
#     max_depth = 0
#     while queue:

#         current_block, path = queue.popleft()
#         explored_states += 1
#         max_depth = max(max_depth, len(path))
#         current_state = current_block.get_state()

#         if board.is_win(current_block):
#             # print("Solution Found:", path)
#             print("States Explored:", explored_states)
#             print("Max Depth:", max_depth)
#             end_time = time.time()
#             print("Time Taken:", end_time - start_time)
#             return path

#         for move_name, (dr, dc) in moves.items():

#             # new_block = copy.deepcopy(current_block)
#             new_block=current_block.copy()    

#             if move_name == "u":
#                 new_block.move_up()
#             elif move_name == "d":
#                 new_block.move_down()
#             elif move_name == "l":
#                 new_block.move_left()
#             elif move_name == "r":
#                 new_block.move_right()

#             new_state = new_block.get_state()

#             if board.is_valid_block(new_block) and new_state not in visited:
#                 visited.add(new_state)
#                 new_path = path + [move_name]
#                 queue.append((new_block, new_path))
    

# def dfs(board, block):

#     stack = []

#     visited = set()

#     start_state = block.get_state()

#     stack.append((block, []))

#     visited.add(start_state)

#     explored_states = 0

#     start_time = time.time()

#     max_depth = 0

#     moves = {
#         "u": (-1,0),
#         "d": (1,0),
#         "l": (0,-1),
#         "r": (0,1)
#     }

#     while stack:

#         current_block, path = stack.pop()

#         explored_states += 1

#         max_depth = max(max_depth, len(path))

#         if board.is_win(current_block):

#             end_time = time.time()

#             print("DFS Results")
#             print("Solution Length:", len(path))
#             print("States Explored:", explored_states)
#             print("Max Depth:", max_depth)
#             print("Time Taken:", (end_time - start_time) * 1000, "ms")

#             return path

#         for move_name, (dr, dc) in moves.items():

#             new_block = copy.deepcopy(current_block)

#             if move_name == "u":
#                 new_block.move_up()
#             elif move_name == "d":
#                 new_block.move_down()
#             elif move_name == "l":
#                 new_block.move_left()
#             elif move_name == "r":
#                 new_block.move_right()

#             new_state = new_block.get_state()

#             if board.is_valid_block(new_block) and new_state not in visited:

#                 visited.add(new_state)

#                 new_path = path + [move_name]

#                 stack.append((new_block, new_path))

#     print("No solution found")

#     return None








import time
import random
from collections import deque


# ─────────────────────────────────────────────────────────
# BFS — Breadth First Search
# ─────────────────────────────────────────────────────────

def bfs(board, block):

    frontier = deque()

    visited = set()

    start_state = block.get_state()

    frontier.append((block.copy(), []))

    visited.add(start_state)

    moves = ["u", "d", "l", "r"]

    explored_states = 0

    max_depth = 0

    start_time = time.time()

    while frontier:

        current_block, path = frontier.popleft()

        if current_block.pos1 is None or current_block.pos2 is None:
            continue

        explored_states += 1

        max_depth = max(max_depth, len(path))

        if board.is_win(current_block):

            end_time = time.time()

            print("\n=== BFS Results ===")
            print("Solution Path   :", path)
            print("Solution Length :", len(path))
            print("States Explored :", explored_states)
            print("Max Depth       :", max_depth)
            print("Time Taken      :", (end_time - start_time) * 1000, "ms")

            return {
                "path": path,
                "states": explored_states,
                "depth": max_depth,
                "time": (end_time - start_time) * 1000
            }

        for move_name in moves:

            new_block = current_block.copy()

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

                frontier.append((new_block, new_path))

    print("No BFS solution found")

    return None


# ─────────────────────────────────────────────────────────
# DFS — Depth First Search
# ─────────────────────────────────────────────────────────

def dfs(board, block):

    frontier = []

    visited = set()

    start_state = block.get_state()

    frontier.append((block.copy(), []))

    visited.add(start_state)

    moves = ["u", "d", "l", "r"]

    explored_states = 0

    max_depth = 0

    start_time = time.time()

    while frontier:

        current_block, path = frontier.pop()

        if current_block.pos1 is None or current_block.pos2 is None:
            continue

        explored_states += 1

        max_depth = max(max_depth, len(path))

        if board.is_win(current_block):

            end_time = time.time()

            print("\n=== DFS Results ===")
            print("Solution Path   :", path)
            print("Solution Length :", len(path))
            print("States Explored :", explored_states)
            print("Max Depth       :", max_depth)
            print("Time Taken      :", (end_time - start_time) * 1000, "ms")

            return {
                "path": path,
                "states": explored_states,
                "depth": max_depth,
                "time": (end_time - start_time) * 1000
            }

        for move_name in moves:

            new_block = current_block.copy()

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

                frontier.append((new_block, new_path))

    print("No DFS solution found")

    return None 







