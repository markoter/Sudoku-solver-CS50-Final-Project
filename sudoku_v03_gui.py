import pygame, sys

fps = 10
# set size of the grid
size = windowWidth, windowHeight = 450, 450
# set colors
white = (255,255,255)

def main():
    # initialize the pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    # set screen
    screen = pygame.display.set_mode(size)
    # set name shown on window
    pygame.display.set_caption('Sudoku Solver v03 GUI')
    # set background
    screen.fill(white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        fpsClock.tick(fps)

if __name__ == '__main__':
    main()
