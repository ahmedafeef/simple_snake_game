import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_TITLE = "Snake Game"
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# set up the font
font = pygame.font.SysFont(None, 25)

# set up the clock
clock = pygame.time.Clock()

# set up the snake
snake_block_size = 10
snake_speed = 15

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, BLACK, [x[0], x[1], snake_block_size, snake_block_size])

# set up the game loop
def game_loop():
    game_over = False
    game_close = False

    # set up the initial position of the snake
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    # set up the initial position of the food
    food_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0

    # set up the initial direction of the snake
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # game loop
    while not game_over:

        # display game over message
        while game_close == True:
            game_window.fill(WHITE)
            message = font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            game_window.blit(message, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # check if the snake hits the borders
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True

        # update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # draw the food
        game_window.fill(WHITE)
        pygame.draw.rect(game_window, RED, [food_x, food_y, snake_block_size, snake_block_size])

        # draw the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        snake(snake_block_size, snake_list)
        pygame.display.update()

        # check if the snake hits the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
            length_of_snake += 1

        # set up the clock
        clock.tick(snake_speed)

    # quit Pygame
    pygame.quit()

game_loop()