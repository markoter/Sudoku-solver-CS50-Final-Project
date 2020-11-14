grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

#create box for defined i and j
def make_box(board, i, j):
    box = [[None for _ in range(3)] for _ in range(3)]
    for m in range(3):
        for n in range(3):
            modi = i % 3
            modj = j % 3
            box[m][n] = board[i + m - modi][j + n - modj]
    return box

i = 2
j = 1

boxik = make_box(grid, i, j)
for row in boxik:
    print(row)