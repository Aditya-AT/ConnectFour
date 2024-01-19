# Connect Four Game in Python with Pygame

## Overview
This project is an implementation of the classic game Connect Four, developed in Python using the Pygame library. The game features a graphical user interface where players can take turns to drop colored discs into a seven-column, six-row vertically suspended grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Features
- **Graphical User Interface**: Built with Pygame, the game features a colorful and intuitive interface.
- **Two Player Game**: The game allows two players to play against each other, taking turns to drop their pieces.
- **Winning and Draw Detection**: The game automatically detects and announces a win for either player or a draw if the board is filled completely without any winning condition.

## How to Play
- The game starts with an empty grid.
- Players take turns to drop their colored discs into the grid.
- A piece will occupy the lowest available space within the selected column.
- The first player to form an unbroken line of four discs horizontally, vertically, or diagonally wins the game.
- If the entire grid is filled without a winning line, the game is declared a draw.

## Controls
- **Mouse Movement**: Move the cursor left or right to choose a column.
- **Mouse Click**: Click to drop the piece into the selected column.

## Installation
1. Ensure Python and Pygame are installed on your system.
2. Clone the repository or download the source code.
3. Run the Python script to start the game.

## Technologies Used
- **Python**: The core programming language used for the game logic.
- **Pygame**: A Python library used for creating the graphical interface and handling user interactions.
