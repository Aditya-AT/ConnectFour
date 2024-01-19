import numpy as np
import pygame
import sys
import math

# Define colors for the game
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Set the size of the board
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """Create a new game board."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    """Drop a piece into the board."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Check if the selected column has space."""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """Find the next open row in the selected column."""
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    """Print the board to the console."""
    print(np.flip(board, 0))  # Flipping the board for correct visual representation

def winning_move(board, piece):
    """Check if the current move is a winning move."""
    # Check all horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and all(board[r][c + i] == piece for i in range(1, 4)):
                return True

    # Check all vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and all(board[r + i][c] == piece for i in range(1, 4)):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and all(board[r + i][c + i] == piece for i in range(1, 4)):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and all(board[r - i][c + i] == piece for i in range(1, 4)):
                return True

    return False

def draw_board(board):
    """Draw the board in Pygame window."""
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, RED, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

# Initialize Pygame
pygame.init()

# Define the size of squares and the radius of pieces
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

# Calculate the width and height of the game window
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

# Set the size and create the Pygame window
size = (width, height)
screen = pygame.display.set_mode(size)

# Create the board and draw it
board = create_board()
draw_board(board)

# Game loop variables
game_over = False
turn = 0
winningfont = pygame.font.SysFont("monospace", 20)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, GREEN, (pos_x, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x = event.pos[0]
            col = int(math.floor(pos_x / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, turn + 1)

                if winning_move(board, turn + 1):
                    label = winningfont.render(f"Player {turn + 1} Wins!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True
                else:
                    # Check for draw condition
                    is_draw = all(board[ROW_COUNT - 1][c] != 0 for c in range(COLUMN_COUNT))
                    if is_draw:
                        label = winningfont.render("Match Drawn!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            # Switch turns
            turn = (turn + 1) % 2

            print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(10000)
                
