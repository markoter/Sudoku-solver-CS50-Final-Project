import pygame, sys

fps = 10
# set size of the grid
windowSize = int(90)
windowMultiplier = int(5) # here modify the size of the window
windowWidth = int(windowSize * windowMultiplier)
windowHeight = int(windowSize * windowMultiplier)
squareSize = int((windowSize * windowMultiplier) / 3)
cellSize = int(squareSize / 3)

# set colors
white = (255,255,255)
black = (0,0,0)
lightGray = (200,200,200)

def drawGrid(screen):
    # minor lines
    for x in range(0, windowWidth, cellSize):
        pygame.draw.line(screen, lightGray, (x,0), (x,windowHeight))
    
    return None

def main():
    # initialize the pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    # set screen
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    # set name shown on window
    pygame.display.set_caption('Sudoku Solver v03 GUI')
    # set background
    screen.fill(white)

    drawGrid(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        fpsClock.tick(fps)


if __name__ == '__main__':
    main()
