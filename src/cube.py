from random import random

import pygame

CUBE_CHAOTIC_V = 1.4

CUBE_USER_V = 20


class Cube:

    @classmethod
    def get_total_cubes_amount(cls) -> int:
        return len(cls.all_cubes)

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
        # print(cls.all_cubes[cls.active_cube].v_x)
        return cls.all_cubes[cls.active_cube]

    @classmethod
    def change_v(cls, new_v):

        # cls.all_cubes.remove(cls.get_active_cube())
        v_x_ = random() * 2 * (CUBE_CHAOTIC_V + new_v) - CUBE_CHAOTIC_V - new_v
        v_y_ = random() * 2 * (CUBE_CHAOTIC_V + new_v) - CUBE_CHAOTIC_V - new_v

        cls.all_cubes[cls.active_cube - 1].v_x = v_x_
        cls.all_cubes[cls.active_cube - 1].v_y = v_y_

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

    @classmethod
    def is_continue_condition_all(cls, screen_w, screen_h):
        for i in cls.all_cubes:
            if not i.is_continue_condition(screen_w, screen_h):
                return False
        return True

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

    def is_continue_condition(self, screen_w, screen_h) -> bool:
        if self.pos_x + 40 > screen_w or self.pos_y + 40 > screen_h or self.pos_x < 0 or self.pos_y < 0:
            return False
        else:
            return True
