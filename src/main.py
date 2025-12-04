import math

import pygame
from cube import Cube

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PERIOD = 10

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Turn based game")

game_time = 0
flag = 0
last_created = 0

Cube.generate_cubes(SCREEN_WIDTH, SCREEN_HEIGHT, 3)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Cube.change_active_cube()
                # Cube.active_cube = (Cube.active_cube + 1) % len(Cube.all_cubes)
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    keys = pygame.key.get_pressed()
    for q in Cube.all_cubes:
        q.draw_cube(screen)
        q.handle_position()
    Cube.handle_keys(keys)

    # RENDER YOUR GAME HERE
    # квадрат
    # rect1 = pygame.Rect((pos[0], pos[1], 40, 40))
    # pygame.draw.rect(screen, "red", rect1)

    # game logic
    # keys = pygame.key.get_pressed()
    # some_cube.handle_position(keys)
    # pos[0] += 2
    # if keys[pygame.K_LEFT]:
    #     pos[0] -= 20
    # if keys[pygame.K_RIGHT]:
    #     pos[0] += 20


    # pygame.draw.circle(screen, "red", player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # clock.tick(60)
    dt = clock.tick(60) / 1000
    game_time += dt
    print(game_time)


    if math.floor(game_time) % 5 == 0 and flag < 5:
        # TODO генерить постепенно используя период
        Cube.add_cube(SCREEN_WIDTH, SCREEN_HEIGHT)
        flag += 1


# Quit Pygame
pygame.quit()