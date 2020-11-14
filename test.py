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

def search(number, board, i, j):
    # search vertically
    for k in range(0, len(board)):
        if board[k][j] == number:
            # print(f"znalazłem {number} w ({k},{j})")
            return "znalazłem w kolumnie"
    # search horizontally
    for l in range(0, len(board)):
        if board[i][l] == number:
            # print(f"znalazłem {number} w ({i},{l})")
            return "znalazłem w linii"
    # search in box
    box = make_box(board, i, j)
    if number in box:
        return("znalazłem w boxie")
    
    return 0

wynik = search(1, grid, 3, 0)

print (wynik)


print (grid[1][0])