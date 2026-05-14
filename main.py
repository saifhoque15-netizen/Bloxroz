from game import Game
from level import LEVELS

from solver import (
    bfs,
    dfs,
    astar,
    heuristic_manhattan,
    heuristic_euclidean,
    heuristic_weighted
)

import matplotlib.pyplot as plt


game = Game(LEVELS)


# ─────────────────────────────────────────────
# STORE TIMES
# ─────────────────────────────────────────────

bfs_times = []

dfs_times = []

manhattan_times = []

euclidean_times = []

weighted_times = []

level_names = []


# ─────────────────────────────────────────────
# RUN ALL LEVELS
# ─────────────────────────────────────────────

for i in range(len(LEVELS)):

    print("\n========================")
    print("LEVEL", i + 1)
    print("========================\n")

    game.current_level = i

    game.load_level()

    level_names.append(f"Level {i+1}")


    # ─────────────────────────────
    # BFS
    # ─────────────────────────────

    print("Running BFS...\n")

    bfs_result = bfs(game.board, game.block)

    if bfs_result is not None:

        print("BFS Path:", bfs_result["path"])

        bfs_times.append(bfs_result["time"])

    else:

        print("No BFS solution")

        bfs_times.append(0)


    # ─────────────────────────────
    # DFS
    # ─────────────────────────────

    game.load_level()

    print("\nRunning DFS...\n")

    dfs_result = dfs(game.board, game.block)

    if dfs_result is not None:

        print("DFS Path:", dfs_result["path"])

        dfs_times.append(dfs_result["time"])

    else:

        print("No DFS solution")

        dfs_times.append(0)


    # ─────────────────────────────
    # A* MANHATTAN
    # ─────────────────────────────

    game.load_level()

    print("\nRunning A* Manhattan...\n")

    result1 = astar(
        game.board,
        game.block,
        heuristic_manhattan
    )

    if result1 is not None:

        print("A* Manhattan Path:", result1["path"])

        manhattan_times.append(result1["time"])

    else:

        print("No Manhattan solution")

        manhattan_times.append(0)


    # ─────────────────────────────
    # A* EUCLIDEAN
    # ─────────────────────────────

    game.load_level()

    print("\nRunning A* Euclidean...\n")

    result2 = astar(
        game.board,
        game.block,
        heuristic_euclidean
    )

    if result2 is not None:

        print("A* Euclidean Path:", result2["path"])

        euclidean_times.append(result2["time"])

    else:

        print("No Euclidean solution")

        euclidean_times.append(0)


    # ─────────────────────────────
    # A* WEIGHTED
    # ─────────────────────────────

    game.load_level()

    print("\nRunning A* Weighted...\n")

    result3 = astar(
        game.board,
        game.block,
        heuristic_weighted
    )

    if result3 is not None:

        print("A* Weighted Path:", result3["path"])

        weighted_times.append(result3["time"])

    else:

        print("No Weighted solution")

        weighted_times.append(0)


# ─────────────────────────────────────────────
# GRAPH
# ─────────────────────────────────────────────

plt.figure(figsize=(12,6))

x = range(len(level_names))

plt.plot(
    x,
    bfs_times,
    marker='o',
    label="BFS"
)

plt.plot(
    x,
    dfs_times,
    marker='o',
    label="DFS"
)

plt.plot(
    x,
    manhattan_times,
    marker='o',
    label="A* Manhattan"
)

plt.plot(
    x,
    euclidean_times,
    marker='o',
    label="A* Euclidean"
)

plt.plot(
    x,
    weighted_times,
    marker='o',
    label="A* Weighted"
)

plt.xticks(x, level_names)

plt.xlabel("Levels")

plt.ylabel("Time (ms)")

plt.title("Search Algorithm Comparison")

plt.legend()

plt.grid(True)

plt.show()

    

