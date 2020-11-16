def filler(ins, board, i, j):
    while ins < 10:
        if search(ins, board, i, j) == 0:
            return ins
        else:
            ins += 1
            return filler(ins, board, i, j)
    return "$"