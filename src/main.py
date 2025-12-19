import math
import os

import pygame
from cube import Cube

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
PERIOD = 10
MAXIMUM_CUBES_AMOUNT = 6
SCORE_FILE = 'score.txt'

def get_next_period():
    yield 15
    yield 10
    yield 10

def get_next_v(): #генератор для постепенного ускорения
    for i in range(10000000):
        yield float(i/20)

def get_old_score() -> float:
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            return float(f.read())
    else:
        return 0.0


def try_save_score(old_score: float, new_score: float):
    if old_score < new_score:
        with open(SCORE_FILE, 'w') as f:
            f.write(str(new_score))

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Turn based game")

game_time = 0
cube_create_time = 4
last_created = 0

Cube.generate_cubes(SCREEN_WIDTH, SCREEN_HEIGHT, 3)

old_score = get_old_score()
period_generator = get_next_period()
v_generator = get_next_v()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Cube.change_active_cube()
                Cube.change_v(next(v_generator))#Изменение скорости и направления
            if event.key == pygame.K_q:
                try_save_score(old_score, game_time)
                running = False
        if event.type == pygame.QUIT:
            try_save_score(old_score, game_time)
            running = False

    # fill the screen with a color to wipe away anything from last frame

    screen.fill("black")
    for q in Cube.all_cubes:
        q.draw_cube(screen)


    is_continue = Cube.is_continue_condition_all(SCREEN_WIDTH, SCREEN_HEIGHT)
    if is_continue:
        keys = pygame.key.get_pressed()
        for q in Cube.all_cubes:
            q.handle_position()
        Cube.handle_keys(keys)
        # clock.tick(60) limits FPS to 60
        dt = clock.tick(60) / 1000
        game_time += dt
        #print(game_time)
        #print(Cube.is_continue_condition_all(SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        text_your_time = font1.render(f'Ты продержался {game_time:.2f} сек.', True, (255, 255, 255))
        text_rect_your_time = text_your_time.get_rect()
        text_rect_your_time.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)
        screen.blit(text_your_time, text_rect_your_time)
        text_old_record = font1.render(f'Старый рекорд {old_score:.2f} сек.', True, (255, 255, 255))
        text_rect_old_record = text_old_record.get_rect()
        text_rect_old_record.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25)
        screen.blit(text_old_record, text_rect_old_record)

    # RENDER YOUR GAME HERE
    # квадрат
    # rect1 = pygame.Rect((pos[0], pos[1], 40, 40))
    # pygame.draw.rect(screen, "red", rect1)
    # pygame.draw.circle(screen, "red", player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

    if math.floor(game_time) == cube_create_time and Cube.get_total_cubes_amount() <= MAXIMUM_CUBES_AMOUNT:
        Cube.add_cube(SCREEN_WIDTH, SCREEN_HEIGHT)
        cube_create_time += next(period_generator)


# Quit Pygame
pygame.quit()
