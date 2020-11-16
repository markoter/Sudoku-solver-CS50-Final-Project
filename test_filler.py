def filler():
    for ins in range(1,9):
        if search(ins, board, i, j) == 0:
            board[i][j] = ins
        else:
            board[i][j] = "&"
            return board