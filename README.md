# Bloxroz
A terminal-based implementation of the Bloxorz puzzle game developed in Python using Object-Oriented Programming and search algorithms.

## Features

- Multiple levels
- Move counter
- Colored terminal interface
- Restart on losing
- Level progression
- BFS solver
- A* solver

  ## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Colorama
- BFS (Breadth First Search)
- A* Search Algorithm

  ## Project Structure

main.py
game.py
board.py
block.py
solver.py
level.py


## How to Run

1. Install Python
2. Install dependencies:

pip install colorama

3. Run the game:

python main.py



## Controls

- r → move right
- l → move left
- u → move up
- d → move down


## Game Rules

- The block can stand upright or lie horizontally/vertically.
- If any part of the block moves outside the board or onto a hole (0), the player loses.
- The player wins by placing the upright block on the goal tile (9).

## Algorithms

### BFS
Breadth First Search is used to find the shortest path to the goal.

### DFS 
Depth Fisrt Search is used to find the goal in short time than BFS.

### A*
A* Search uses heuristics to optimize pathfinding.



## Author
Abu Nayem ,
Bohair Baloch,
Maimuna ,
Mozhdeh Marvi,
Saif Hoque.
