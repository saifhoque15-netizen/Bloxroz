import pygame

from game import Game
from level import LEVELS

pygame.init()

# ─────────────────────────────────────────────
# SETTINGS
# ─────────────────────────────────────────────

WIDTH = 800
HEIGHT = 600

TILE_SIZE = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bloxorz")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

# ─────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
BLUE = (50, 120, 255)
GREEN = (50, 220, 50)
RED = (220, 50, 50)
YELLOW = (255, 220, 50)
GRAY = (100, 100, 100)

# ─────────────────────────────────────────────
# GAME
# ─────────────────────────────────────────────

game = Game(LEVELS)

# ─────────────────────────────────────────────
# DRAW BOARD
# ─────────────────────────────────────────────

def draw_board():

    screen.fill(BLACK)

    grid = game.board.grid

    for row in range(len(grid)):

        for col in range(len(grid[row])):

            tile = grid[row][col]

            x = col * TILE_SIZE
            y = row * TILE_SIZE

            # FLOOR
            if tile == 1 or tile == 2:

                pygame.draw.rect(
                    screen,
                    WHITE,
                    (x, y, TILE_SIZE, TILE_SIZE)
                )

            # HOLE
            elif tile == 0:

                pygame.draw.rect(
                    screen,
                    RED,
                    (x, y, TILE_SIZE, TILE_SIZE)
                )

            # GOAL
            elif tile == 9:

                pygame.draw.rect(
                    screen,
                    GREEN,
                    (x, y, TILE_SIZE, TILE_SIZE)
                )

            pygame.draw.rect(
                screen,
                GRAY,
                (x, y, TILE_SIZE, TILE_SIZE),
                2
            )

# ─────────────────────────────────────────────
# DRAW BLOCK
# ─────────────────────────────────────────────

def draw_block():

    positions = [game.block.pos1, game.block.pos2]

    for row, col in positions:

        x = col * TILE_SIZE
        y = row * TILE_SIZE

        pygame.draw.rect(
            screen,
            BLUE,
            (
                x + 5,
                y + 5,
                TILE_SIZE - 10,
                TILE_SIZE - 10
            )
        )

# ─────────────────────────────────────────────
# DRAW UI
# ─────────────────────────────────────────────

def draw_ui():

    level_text = font.render(
        f"Level: {game.current_level + 1}",
        True,
        YELLOW
    )

    moves_text = font.render(
        f"Moves: {game.moves}",
        True,
        YELLOW
    )

    orientation_text = font.render(
        f"Orientation: {game.block.get_orientation()}",
        True,
        YELLOW
    )

    screen.blit(level_text, (450, 50))
    screen.blit(moves_text, (450, 100))
    screen.blit(orientation_text, (450, 150))

# ─────────────────────────────────────────────
# GAME LOOP
# ─────────────────────────────────────────────

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                game.move_block("u")

            elif event.key == pygame.K_DOWN:
                game.move_block("d")

            elif event.key == pygame.K_LEFT:
                game.move_block("l")

            elif event.key == pygame.K_RIGHT:
                game.move_block("r")

            game.moves += 1

            # LOSE
            if not game.board.is_valid_block(game.block):

                print("You Lost!")

                game.load_level()

            # WIN
            elif game.board.is_win(game.block):

                print("Level Completed!")

                game.current_level += 1

                if game.current_level >= len(LEVELS):

                    print("You Finished All Levels!")

                    running = False

                else:

                    game.load_level()

    draw_board()

    draw_block()

    draw_ui()

    pygame.display.update()

pygame.quit()