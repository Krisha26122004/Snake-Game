import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Snake and game settings
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Initialize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game with Data Structures")
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("calibri", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    """Display the player's score on the screen."""
    value = score_font.render(f"Score: {score}", True, YELLOW)
    screen.blit(value, [10, 10])


def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def message(msg, color):
    """Display a message in the center of the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def main_game():
    # Initial settings
    game_over = False
    game_close = False

    # Snake's starting position and movement
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    dx, dy = 0, 0

    # Snake body managed using deque
    snake_body = deque([[x, y]])
    snake_length = 1

    # Food position
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("You lost! Press P to play again or Q to quit", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main_game()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        # Check for wall collisions
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            game_close = True

        # Update snake's head position
        x += dx
        y += dy
        snake_body.append([x, y])

        # Check for food collision
        if x == food_x and y == food_y:
            food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
        else:
            snake_body.popleft()  # Remove the tail if the snake didn't grow

        # Check for self-collision
        if list(snake_body)[-1] in list(snake_body)[:-1]:
            game_close = True

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])  # Draw food
        draw_snake(snake_body)  # Draw snake
        display_score(snake_length - 1)
        pygame.display.update()

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main_game()
