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
            # print(f"znalazłem {number} w ({k},{j})")
            return 1
    for l in range(0, len(board)):
        if board[i][l] == number:
            # print(f"znalazłem {number} w ({i},{l})")
            return 1
    return 0

wynik = search(1, grid, 3, 0)

if wynik == 1:
    print("znaleziono")
else:
    print("nie ma")


print (grid[1][0])