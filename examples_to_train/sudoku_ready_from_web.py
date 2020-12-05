import pygame, sys
from pygame.locals import *

#Number of frames per second
FPS = 10

# Sets size of grid
WINDOWMULTIPLIER = int(5) # Modify this number to change size of grid
WINDOWSIZE = int(81) # needs to be multiple of 9
WINDOWWIDTH = int(WINDOWSIZE * WINDOWMULTIPLIER)
WINDOWHEIGHT = int(WINDOWSIZE * WINDOWMULTIPLIER)
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3) # size of a 3x3 square
CELLSIZE = int(SQUARESIZE / 3) # Size of a cell
NUMBERSIZE = int(CELLSIZE /3) # Position of unsolved number

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)
LIGHTGRAY = (200,200,200)
BLUE      = (0  ,0  ,255)
GREEN     = (0  ,255,0  )

def drawGrid():

    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))
    
    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT),2)
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y),2)

    return None

def initiateCells():
    initialGrid = {}
    fullCell = [1,2,3,4,5,6,7,8,9]
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            initialGrid[xCoord,yCoord] = list(fullCell) # Copies List
    return initialGrid

# Takes the remaining numbers and displays them in the cells.
def displayCells(currentGrid):
    # Create offset factors to display numbers in right location in cells.
    xFactor = 0
    yFactor = 0
    for item in currentGrid: # item is x,y co-ordinate from 0-8
        cellData = currentGrid[item] # isolates the numbers still available for that cell
        for number in cellData: #incNumtes through each number
            if number != ' ': # ignores those already dismissed
                xFactor = ((number-1)%3) # 1/4/7 = 0 2/5/8 = 1 3/6/9 =2
                if number <= 3:
                    yFactor = 0
                elif number <=6:
                    yFactor = 1
                else:
                    yFactor = 2
                #(item[0] * CELLSIZE) Positions in the right Cell
                #(xFactor*NUMBERSIZE) Offsets to position number
                if cellData.count(' ') < 8:    
                    populateCells(number,(item[0]*CELLSIZE)+(xFactor*NUMBERSIZE),(item[1]*CELLSIZE)+(yFactor*NUMBERSIZE),'small')
                else:
                    populateCells(number,(item[0]*CELLSIZE),(item[1]*CELLSIZE),'large')
                    
    return None

# writes cellData at given x, y co-ordinates   
def populateCells(cellData, x, y,size):
    if size == 'small':
        cellSurf = BASICFONT.render('%s' %(cellData), True, LIGHTGRAY)
    elif size == 'large':
        cellSurf = LARGEFONT.render('%s' %(cellData), True, GREEN)
        
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)

def drawBox(mousex, mousey):

    boxx =((mousex*27) / WINDOWWIDTH) * (NUMBERSIZE ) # 27 number of squares
    boxy =((mousey*27) / WINDOWHEIGHT) * (NUMBERSIZE ) # 27 number of squares
    pygame.draw.rect(DISPLAYSURF, BLUE, (boxx,boxy,NUMBERSIZE,NUMBERSIZE), 1)

# allows choice of number and displays selected number
def displaySelectedNumber(mousex, mousey, currentGrid):
    xNumber = (mousex*27) / WINDOWWIDTH # xNumber in range 0 - 26
    yNumber = (mousey*27) / WINDOWWIDTH # yNumber in range 0 - 26
    #Determine a 0,1 or 2 for x and y
    modXNumber = xNumber % 3
    modYNumber = yNumber % 3
    if modXNumber == 0:
        xChoices = [1,4,7]
        number = xChoices[modYNumber]        
    elif modXNumber == 1:
        xChoices = [2,5,8]
        number = xChoices[modYNumber]
    else:
        xChoices = [3,6,9]
        number = xChoices[modYNumber]
    
    # need to determine the cell we are in
    xCellNumber = xNumber / 3
    yCellNumber = yNumber / 3
   
    # gets a list of current numbers
    currentState = currentGrid[xCellNumber,yCellNumber]
    incNum = 0
    
    while incNum < 9:
        # if NOT number selected
        if incNum+1 != number:
            currentState[incNum] = ' ' # make ' '
        else:
            currentState[incNum] = number # make = number
        #update currentGrid
        currentGrid[xCellNumber,yCellNumber] = currentState
        incNum += 1
    currentGrid = refreshGrid(currentGrid)
    return currentGrid

# If a number is selected, and then changed the grid needs to be refreshed. 
def refreshGrid(currentGrid):
    fullCell = [1,2,3,4,5,6,7,8,9]
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            cellData = currentGrid[xCoord, yCoord]
            if cellData.count(' ') < 8:
                currentGrid[xCoord,yCoord] = list(fullCell) # Copies List
    return currentGrid
    
def solveSudoku(currentGrid):
    # iterate through all cells and determine if any cells have only one number in them
    # if so they are passed through to removeX/Y/Grid for processing
    for item in currentGrid: # item is x,y co-ordinate from 0-8 - iterates through all.
        cellData = currentGrid[item] # isolates the numbers still available for that individual cell
        if cellData.count(' ') == 8: # only look at those with one number remaining
            for number in cellData: # Determine the only number in the grid
                if number != ' ':
                    updateNumber = number
            #Removes any chosen numbers from Rows, column and grid
            #Only solves where there is a single number in the grid
            currentGrid = removeX(currentGrid, item, updateNumber)
            currentGrid = removeY(currentGrid, item, updateNumber)
            currentGrid = removeGrid(currentGrid, item, updateNumber)
    # determine if any cells contain a number only used once in X/Y/Grid
    currentGrid = onlyNinX(currentGrid)
    currentGrid = onlyNinY(currentGrid)
    currentGrid = onlyNinGrid(currentGrid)
    return currentGrid

###Solving Algorithms
#removes chosen numbers from remaining rows
def removeX(currentGrid, item, number):
    for x in range(0,9):
        if x != item[0]: # ignores current cell (iteration in solveSudoku)
            currentState = currentGrid[(x,item[1])]
            currentState[number-1] = ' '
            currentGrid[(x,item[1])] = currentState
    return currentGrid

#removes chosen numbers from remaining columns
def removeY(currentGrid, item, number):
    for y in range(0,9):
        if y != item[1]:# ignores current cell (iteration in solveSudoku)
            currentState = currentGrid[(item[0],y)]
            currentState[number-1] = ' '
            currentGrid[(item[0],y)] = currentState
    return currentGrid

#removes chosen numbers from remaining grid
def removeGrid(currentGrid, item, number):
    # determines which of the 9 grids looking at to iterate through the 9 grid numbers
    if item[0] < 3:
        xGrid = [0,1,2]
    elif item[0] > 5:
        xGrid = [6,7,8]
    else: xGrid = [3,4,5]

    if item[1] < 3:
        yGrid = [0,1,2]
    elif item[1] > 5:
        yGrid = [6,7,8]
    else: yGrid = [3,4,5]

    #iterates through each of the nine numbers in the grid
    for x in xGrid:
        for y in yGrid:
            if (x,y) != item: # for all squares except the one containing the number
                currentState = currentGrid[(x,y)] # isolates the numbers still available for that cell
                currentState[number-1] = ' ' # make them blank.
                currentGrid[(x,y)] = currentState
            
    return currentGrid

# Go through each cell in each row
# check if it contains a number which is not in the rest of the row.
def onlyNinX(currentGrid):

    # check all items in currentGrid list
    for item in currentGrid:
        
        # create two empty lists
        allNumbers = []
        currentNumbers = []
        
        # determine all numbers remaining in the row - store in allNumbers
        for xRange in range(0,9):
            for rowNumbers in currentGrid[(xRange,item[1])]:
                if rowNumbers != ' ':
                    allNumbers.append(rowNumbers)
                    
        # determine numbers remaining in individual cell being looked at - store in currentNumbers
        for cellNumbers in currentGrid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
        
        # look at numbers remaining in a cell. Check if they only appear in the row once.        
        if len(currentNumbers) > 1: # run only if there is more than one number remaining, ignoring cells already solved
            for checkNumber in currentNumbers: #iterate currentNumbers (potential numbers)
                if allNumbers.count(checkNumber) == 1:  #if there is only one in the row i.e. in that grid you are on
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = currentGrid[item] # get currentState list for the item to prepare for modification
                    for individualNumber in currentState: # iterate through currentState list
                        if individualNumber != checkNumber and individualNumber != ' ': # if each != checkNumber and not already found i.e. ' '
                            currentState[individualNumber-1] = ' ' # ensures only the single number remains
                            currentGrid[item] = currentState # adds data back into currentGrid dictionary
                            
    return currentGrid

def onlyNinY(currentGrid):

    # check all items in currentGrid list
    for item in currentGrid:
        
        # create two empty lists
        allNumbers = []
        currentNumbers = []
        
        # determine all numbers remaining in the column - store in allNumbers
        for yRange in range(0,9):
            for columnNumbers in currentGrid[(item[0],yRange)]:
                if columnNumbers != ' ':
                    allNumbers.append(columnNumbers)
                    
        # determine numbers remaining in individual cell being looked at - store in currentNumbers
        for cellNumbers in currentGrid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
        
        # look at numbers remaining in a cell. Check if they only appear in the column once.        
        if len(currentNumbers) > 1: # run only if there is more than one number remaining, ignoring cells already solved
            for checkNumber in currentNumbers: #iterate currentNumbers (potential numbers)
                if allNumbers.count(checkNumber) == 1:  #if there is only one in the column i.e. in that grid you are on
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = currentGrid[item] # get currentState list for the item to prepare for modification
                    for individualNumber in currentState: # iterate through currentState list
                        if individualNumber != checkNumber and individualNumber != ' ': # if each != checkNumber and not already found i.e. ' '
                            currentState[individualNumber-1] = ' ' # ensures only the single number remains
                            currentGrid[item] = currentState # adds data back into currentGrid dictionary
                            
    return currentGrid

def onlyNinGrid(currentGrid):

    # check all items in currentGrid list
    for item in currentGrid:

    # determine the co-ordinates for the grid we are dealing with
    
        if item[0] < 3:
            xGrid = [0,1,2]
        elif item[0] > 5:
            xGrid = [6,7,8]
        else: xGrid = [3,4,5]

        if item[1] < 3:
            yGrid = [0,1,2]
        elif item[1] > 5:
            yGrid = [6,7,8]
        else: yGrid = [3,4,5]

        # create two empty lists
        allNumbers = []
        currentNumbers = []

        #iterates through each of the nine numbers in the grid
        for x in xGrid:
            for y in yGrid:
            
                # determine all numbers remaining in the grid - store in allNumbers
                for gridNumbers in currentGrid[(x,y)]:
                    if gridNumbers != ' ':
                        allNumbers.append(gridNumbers)
                        
            # determine numbers remaining in individual cell being looked at - store in currentNumbers
        for cellNumbers in currentGrid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
        
        # look at numbers remaining in a cell. Check if they only appear in the grid once.        
        if len(currentNumbers) > 1: # run only if there is more than one number remaining, ignoring cells already solved
            for checkNumber in currentNumbers: #iterate currentNumbers (potential numbers)
                if allNumbers.count(checkNumber) == 1:  #if there is only one in the grid i.e. in that grid you are on
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = currentGrid[item] # get currentState list for the item to prepare for modification
                    for individualNumber in currentState: # iterate through currentState list
                        if individualNumber != checkNumber and individualNumber != ' ': # if each != checkNumber and not already found i.e. ' '
                            currentState[individualNumber-1] = ' ' # ensures only the single number remains
                            currentGrid[item] = currentState # adds data back into currentGrid dictionary
                            
    return currentGrid

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mouseClicked = False
  
    mousex = 0
    mousey = 0
    
    pygame.display.set_caption('Sudoku Solver')

    global BASICFONT, BASICFONTSIZE, LARGEFONT, LARGEFONTSIZE
    BASICFONTSIZE = 15
    LARGEFONTSIZE = 55
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)

    currentGrid = initiateCells() #sets all cells to have number 1-9
    
    # repaints screen
    DISPLAYSURF.fill(WHITE)
    displayCells(currentGrid)
    drawGrid()

    while True: #main game loop
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            #Mouse click commands
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                mouseClicked = True
           
        if mouseClicked == True:
            # allow number to be selected
            currentGrid = displaySelectedNumber(mousex, mousey, currentGrid)

        solveSudoku(currentGrid)

        # repaints screen
        DISPLAYSURF.fill(WHITE)
        displayCells(currentGrid)
        drawGrid()
        # call function to draw box
        drawBox(mousex,mousey)
        
        pygame.display.update()    
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()