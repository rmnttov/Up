from random import random

import pygame
import sys

CUBE_CHAOTIC_V = 2
CUBE_USER_V = 20


class Cube:

    @classmethod
    def generate_cubes(cls, map_width, map_height, n_cubes):
        cls.all_cubes = []
        for i in range(n_cubes):
            Cube.add_cube(map_width, map_height)
        if n_cubes > 0:
            cls.active_cube = 0

    @classmethod
    def add_cube(cls, map_width, map_height):
        v_x = random() * 2 * CUBE_CHAOTIC_V - CUBE_CHAOTIC_V
        # if v_x == 0:
        #     v_x = randrange(2.0 * CUBE_CHAOTIC_V) - CUBE_CHAOTIC_V
        v_y = random() * 2 * CUBE_CHAOTIC_V - CUBE_CHAOTIC_V
        # if v_y == 0:
        #     v_y = randrange(2 * CUBE_CHAOTIC_V) - CUBE_CHAOTIC_V
        cls.all_cubes.append(Cube(map_width / 2, map_height / 2, v_x, v_y))

    @classmethod
    def get_active_cube(cls):
        return cls.all_cubes[cls.active_cube]

    @classmethod
    def change_active_cube(cls):
        cls.active_cube = (cls.active_cube + 1) % len(cls.all_cubes)


    @classmethod
    def handle_keys(cls, keys):
        if keys[pygame.K_LEFT]:
            Cube.get_active_cube().pos_x -= CUBE_USER_V
        if keys[pygame.K_RIGHT]:
            Cube.get_active_cube().pos_x += CUBE_USER_V
        if keys[pygame.K_DOWN]:
            Cube.get_active_cube().pos_y += CUBE_USER_V
        if keys[pygame.K_UP]:
            Cube.get_active_cube().pos_y -= CUBE_USER_V
        # if keys[pygame.K_SPACE]:
        #     print(123, cls.active_cube, len(cls.all_cubes))
        #     cls.active_cube = (cls.active_cube + 1) % len(cls.all_cubes)

    def __init__(self, pos_x, pos_y, v_x, v_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y

    def check_cord(self, map_width, map_height) -> bool:
        if self.pos_x > map_width or self.pos_x < 0 or self.pos_y > map_height or self.pos_y < 0:
            return False
        return True

    def handle_position(self):
        self.pos_x += self.v_x
        self.pos_y += self.v_y

    def draw_cube(self, screen):
        rect1 = pygame.Rect((self.pos_x, self.pos_y, 40, 40))
        color = "red"
        if Cube.get_active_cube() == self:
            color = "blue"
        pygame.draw.rect(screen, color, rect1)
