import matplotlib.pyplot as plt
import time
import random
from collections import deque
import heapq
import math


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

# ─────────────────────────────────────────────────────────
# HEURISTIC 1 — MANHATTAN
# ─────────────────────────────────────────────────────────

def heuristic_manhattan(block, goal):

    r, c = block.pos1

    gr, gc = goal

    return abs(r - gr) + abs(c - gc)


# ─────────────────────────────────────────────────────────
# HEURISTIC 2 — EUCLIDEAN
# ─────────────────────────────────────────────────────────

def heuristic_euclidean(block, goal):

    r, c = block.pos1

    gr, gc = goal

    return math.sqrt((r - gr) ** 2 + (c - gc) ** 2)


# ─────────────────────────────────────────────────────────
# HEURISTIC 3 — WEIGHTED MANHATTAN
# ─────────────────────────────────────────────────────────

def heuristic_weighted(block, goal):

    r, c = block.pos1

    gr, gc = goal

    return 2 * (abs(r - gr) + abs(c - gc))


# ─────────────────────────────────────────────────────────
# A* SEARCH
# ─────────────────────────────────────────────────────────

def astar(board, block, heuristic_function):

    frontier = []

    visited = set()

    explored_states = 0

    max_depth = 0

    start_time = time.time()

    # FIND GOAL

    goal = None

    for i in range(len(board.grid)):

        for j in range(len(board.grid[i])):

            if board.grid[i][j] == 9:

                goal = (i, j)

    start_state = block.get_state()

    counter = 0

    heapq.heappush(
        frontier,
        (
            0,
            counter,
            block.copy(),
            []
        )
    )

    visited.add(start_state)

    moves = ["u", "d", "l", "r"]

    while frontier:

        _, _, current_block, path = heapq.heappop(frontier)

        explored_states += 1

        max_depth = max(max_depth, len(path))

        if board.is_win(current_block):

            end_time = time.time()

            print("\n=== A* Results ===")

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

                g_cost = len(new_path)

                h_cost = heuristic_function(new_block, goal)

                f_cost = g_cost + h_cost

                counter += 1

                heapq.heappush(
                    frontier,
                    (
                        f_cost,
                        counter,
                        new_block,
                        new_path
                    )
                )

    print("No A* solution found")

    return None







