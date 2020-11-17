import array, random, math, time, sys
print("***** Sudoku solver v0.1 *****")
# recursion problem solver:
# show limit
print(sys.getrecursionlimit())
# change limit
# sys.setrecursionlimit(2500)

zgrid = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

grid = [ [0, 0, 0, 0, 0, 0, 0, 3, 0],
           [0, 0, 0, 0, 9, 1, 0, 0, 0],
           [8, 7, 0, 3, 0, 0, 0, 2, 0],
           [0, 0, 4, 0, 0, 0, 0, 0, 2], 
           [0, 9, 0, 0, 0, 0, 6, 1, 0],  
           [3, 6, 0, 0, 0, 0, 0, 0, 0],  
           [0, 3, 9, 0, 0, 0, 0, 6, 4], 
           [0, 0, 0, 0, 1, 0, 0, 8, 0], 
           [0, 2, 0, 0, 0, 0, 3, 0, 1] ]

agrid = [ [6, 0, 0, 0, 3, 1, 4, 0, 0], 
         [0, 3, 0, 8, 0, 5, 0, 0, 2], 
         [0, 0, 9, 0, 0, 0, 0, 0, 8], 
         [5, 6, 0, 0, 2, 4, 0, 0, 0], 
         [0, 4, 0, 0, 0, 0, 0, 8, 7], 
         [1, 0, 7, 3, 8, 6, 2, 0, 0], 
         [4, 0, 0, 6, 5, 0, 8, 9, 0], 
         [9, 2, 0, 1, 7, 0, 3, 0, 5], 
         [8, 5, 1, 0, 4, 0, 0, 0, 0] ]

#create box for defined i and j (there should be 9 boxes)
def make_box(board, i, j):
    # create empty 2d list
    box = [[None for _ in range(3)] for _ in range(3)]
    for m in range(3):
        for n in range(3):
            box[m][n] = board[i + m - (i % 3)][j + n - (j % 3)]
    return box

# function to check if number already exists in line, column or box (1 if it does, 0 if not)
def search(number, board, i, j):
    # search vertically in column
    for k in range(0, len(board)):
        if board[k][j] == number:
            return 1
    # search horizontally in line
    for l in range(0, len(board)):
        if board[i][l] == number:
            return 1
    # search in box (box is 2d list so we need to check every line one by one)
    box = make_box(board, i, j)
    for row in box:
        if number in row:
            return 1
    return 0

"""
# create new board to track empty spots
def is_empty(board):
    emptySpots = [[0 for i in range(9)] for j in range(9)]
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                # print(f"zero found in ({i}, {j})")
                emptySpots[i][j] = 'o'
            else:
                emptySpots[i][j] = 'x'
    return emptySpots
"""
# function to track empty spots positions in list of dicts
def emptyList(board):
    emptySpot = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                emptySpot.append({'ipos':i, 'jpos':j})
    return emptySpot

# function that puts lowest number (1,9) that fits, if it doesnt exists it puts "$"
def filler(ins, board, i, j):
    if ins == 0 or ins == '$':
        ins = 1
    while ins < 10:
        if search(ins, board, i, j) == 0:
            return ins
        else:
            ins += 1
    return "$"

# function that try to put number in empty spot TODO
emptySpots = emptyList(grid)
def if_fits(board, index, emptySpots):
    while index < len(emptySpots):
        i = emptySpots[index]['ipos']
        j = emptySpots[index]['jpos']
        ins = board[i][j]
        board[i][j] = filler(ins, board, i, j)
        if board[i][j] == "$":
            index -= 1
            return if_fits(board, index, emptySpots)
        index += 1
    return board

# debug printer
emptySpot = emptyList(grid)
print(f"empty spots to fill: {len(emptySpot)}")
#for position in emptySpot:
#  print(position)

print("Original sudoku grid:")
for row in grid:
    print(row)

print("Sudoku after changes:")
newGrid = if_fits(grid, 0, emptySpots)
for row in newGrid:
    print (row)
