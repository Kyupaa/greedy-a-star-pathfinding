# Heuristic Pathfinding Algorithms: Greedy Best-First Search & A*
## Overview

This project was developed as part of an academic programming assignment to practice heuristic search algorithms and understand how they can be used to solve pathfinding problems.

The program simulates a robot navigating a grid with obstacles. It implements and compares two search algorithms, Greedy Best-First Search and A*, to find a path from a starting point to a goal while avoiding blocked cells.

## Objectives

- Practice implementing heuristic search algorithms in Python.
- Understand how heuristic estimates help guide the search process.
- Compare Greedy Best-First Search and A* in terms of path length, explored states, and execution time.
- Learn how to represent a grid, manage a search frontier, and reconstruct a path.

## Features

- Grid-based environment with a starting point, a goal, free cells, and obstacles.
- Manhattan distance heuristic to estimate the distance to the goal.
- Greedy Best-First Search implementation.
- A* Search implementation using accumulated path costs and heuristic estimates.
- Path reconstruction and display of the resulting route.
- Tracking of explored states and execution time.
- Interactive menu to select an algorithm.

## Algorithms

**1. Greedy Best-First Search**

Selects the next state based on its estimated distance to the goal. It can find a path quickly, but it does not guarantee the shortest path.

**2. A* Search**

Combines the cost of the path already traveled with the estimated remaining distance. With the Manhattan heuristic and uniform movement costs used in this project, A* can find an optimal path when a solution exists.

## Technologies Used

- **Language:** Python
- **Modules:** `heapq`, `time`

## Requirements

- Python 3.8 or later.
- A code editor or terminal to run Python scripts.

No external libraries are required.

## Installation and Execution

1. Install Python from [python.org] if it is not already installed.
2. Clone this repository or download the source code.
3. Open a terminal in the project directory.
4. Run the program:

```bash
python heuristica.py
```

## How to Use

When the program starts, it displays the grid and a menu with three options:

1. **Greedy:** Runs Greedy Best-First Search.
2. **A*:** Runs the A* search algorithm.
3. **Exit:** Closes the program.

After selecting an algorithm, the program displays the resulting path, the number of movements, the number of explored states, and the execution time.

## Grid Legend

- `S` — Starting position.
- `G` — Goal position.
- `.` — Free cell.
- `#` — Obstacle.

The robot can move up, down, left, and right. Each movement has a cost of 1.

## What I Learned

Through this project, I practiced implementing search algorithms, working with priority queues, applying heuristic functions, reconstructing paths, and measuring algorithm performance. I also learned how Greedy Best-First Search and A* differ in their approach to finding a solution.

## Project Type

Academic project developed for programming practice and learning purposes.