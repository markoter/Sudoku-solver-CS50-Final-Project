def filler(board, i, j):
    for ins in range(1,9):
        if search(ins, board, i, j) == 0:
            return ins
        else:
            return "&"

def filler(ins):
    while ins < 99:
        if search(ins, board, i, j) == 0:
            return ins
        else:
            ins += 1
            return filler(ins)
