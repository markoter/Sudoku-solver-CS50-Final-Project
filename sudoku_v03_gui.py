import pygame, sys

# initialize the pygame
pygame.init()

size = width, height = 450, 450
black = 0, 0, 0

# create the screen
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()