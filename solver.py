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
def solve(board, index, emptySpots):
    while index < len(emptySpots):
        i = emptySpots[index]['ipos']
        j = emptySpots[index]['jpos']
        ins = board[i][j]
        board[i][j] = filler(ins, board, i, j)
        if board[i][j] == "$":
            index -= 1
        else:
            index += 1
    return board