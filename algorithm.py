import array, random, math, time
print("***** Sudoku solver v0.1 *****")

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

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

# create list to track empty spots
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

# function that try to put number in empty spot TODO
def if_fits(board):
    emptySpots = is_empty(board)
    for i in range(0, len(emptySpots)):
        for j in range(0, len(emptySpots)):
            if emptySpots[i][j] == 'o':
                board[i][j] = '1'
    return board

# debug printer
for row in grid:
    print(row)
for row in if_fits(grid):
    print (row)