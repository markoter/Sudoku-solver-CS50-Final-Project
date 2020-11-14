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
    # box is 2d list so we need to check every line one by one
    for row in box:
        if number in row:
            return "znalazłem w rowie"
    return "ni ma"


# debug print wyniki
szukany_numer = 2
linia = 1
kolumna = 0

wynik = search(szukany_numer, grid, linia, kolumna)

print (wynik)
print (grid[linia][kolumna])