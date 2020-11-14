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

def search(number, board, i, j):
    for k in range(0, len(board)):
        if board[k][j] == number:
            return 1
    for l in range(0, len(board)):
        if board[i][l] == number:
            return 1
    return 0

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

def if_fits(board):
    emptySpots = is_empty(board)
    for i in range(0, len(emptySpots)):
        for j in range(0, len(emptySpots)):
            if emptySpots[i][j] == 'o':
                board[i][j] = '1'
    return board

for row in grid:
    print(row)
for row in if_fits(grid):
    print (row)