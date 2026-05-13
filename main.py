from game import Game
from level import LEVELS
from solver import bfs, dfs

import matplotlib.pyplot as plt


game = Game(LEVELS)

# ─────────────────────────────
# STORE TIMES
# ─────────────────────────────

bfs_times = []
dfs_times = []

level_names = []

# ─────────────────────────────
# RUN ALL LEVELS
# ─────────────────────────────

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

        print("BFS could not solve this level")

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

        print("DFS could not solve this level")

        dfs_times.append(0)


# ─────────────────────────────
# TIME COMPARISON GRAPH
# ─────────────────────────────

plt.figure(figsize=(10,5))

x = range(len(level_names))

plt.plot(x, bfs_times, marker='o', label="BFS")

plt.plot(x, dfs_times, marker='o', label="DFS")

plt.xticks(x, level_names)

plt.xlabel("Levels")

plt.ylabel("Time (ms)")

plt.title("BFS vs DFS Time Comparison")

plt.legend()

plt.grid(True)

plt.show()

    

