import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Turn based game")

pos = [10, 10]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # квадрат
    rect1 = pygame.Rect((pos[0], pos[1], 40, 40))
    pygame.draw.rect(screen, "red", rect1)

    # game logic
    pos[0] += 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pos[0] -= 20
    if keys[pygame.K_RIGHT]:
        pos[0] += 20


    # круг, Михаил
    # pygame.draw.circle(screen, "red", player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60)
    # dt = clock.tick(60) / 1000

# Quit Pygame
pygame.quit()