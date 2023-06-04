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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the font
font = pygame.font.SysFont(None, 25)

# set up the clock
clock = pygame.time.Clock()

# set up the Snake
snake_block_size = 10
snake_speed = 15
snake_list = []
length_of_snake = 5

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, BLUE, [x[0], x[1], snake_block_size, snake_block_size])

# set up the game loop
def game_loop():
    game_over = False
    game_close = False

    # set up the initial position of the Snake
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    # set up the initial position of the food
    food_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0

    # set up the initial direction of the Snake
    x1_change = 0
    y1_change = 0

    # set up the initial size of the Snake
    global length_of_snake
    length_of_snake = 5
    snake_list.clear()

    # set up the initial speed of the Snake
    global snake_speed
    snake_speed = 15

    # set up the obstacles
    obstacles = []
    num_obstacles = 5
    for i in range(num_obstacles):
        obs_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
        obs_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
        obs_w = random.randint(1, 3) * snake_block_size
        obs_h = random.randint(1, 3) * snake_block_size
        obstacles.append(pygame.Rect(obs_x, obs_y, obs_w, obs_h))

    # set up the power-ups
    power_ups = []
    num_power_ups = 3
    for i in range(num_power_ups):
        power_up_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
        power_up_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
        power_up_type = random.choice(["speed", "length"])
        power_ups.append({"rect": pygame.Rect(power_up_x, power_up_y, snake_block_size, snake_block_size), "type": power_up_type})

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

        # check if the Snake hits the borders or obstacles
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True

        for obs in obstacles:
            if obs.collidepoint(x1, y1):
                game_close = True

        # update the position of the Snake
        x1 += x1_change
        y1 += y1_change

        # draw the background and obstacles
        game_window.fill(WHITE)
        for obs in obstacles:
            pygame.draw.rect(game_window, BLACK, obs)

        # draw the food
        pygame.draw.rect(game_window, RED, [food_x, food_y, snake_block_size, snake_block_size])

        # update the Snake's length and speed if it eats the food
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for power_up in power_ups:
            if power_up["rect"].collidepoint(x1, y1):
                if power_up["type"] == "speed":
                    snake_speed += 5
                elif power_up["type"] == "length":
                    length_of_snake += 5
                power_ups.remove(power_up)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
            length_of_snake += 1

            # add new obstacle
            if len(obstacles) < num_obstacles:
                obs_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
                obs_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
                obs_w = random.randint(1, 3) * snake_block_size
                obs_h = random.randint(1, 3) * snake_block_size
                obstacles.append(pygame.Rect(obs_x, obs_y, obs_w, obs_h))

            # add new power-up
            if len(power_ups) < num_power_ups:
                power_up_x = round(random.randrange(0, WINDOW_WIDTH - snake_block_size) / 10.0) * 10.0
                power_up_y = round(random.randrange(0, WINDOW_HEIGHT - snake_block_size) / 10.0) * 10.0
                power_up_type = random.choice(["speed", "length"])
                power_ups.append({"rect": pygame.Rect(power_up_x, power_up_y, snake_block_size, snake_block_size), "type": power_up_type})

        # update the Snake's position and draw it on the screen
        snake(snake_block_size, snake_list)

        # update the score
        score = length_of_snake - 5
        score_text = font.render("Score: " + str(score), True, BLACK)
        game_window.blit(score_text, [0, 0])

        # update the display and wait for a short time
        pygame.display.update()
        clock.tick(snake_speed)

    # quit Pygame and exit the program
    pygame.quit()
    quit()

# start the game loop
game_loop()