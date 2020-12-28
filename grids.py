# grid with only zeros
zgrid = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

# hard grid that brakes the recursion
hgrid = [ 
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 9, 1, 0, 0, 0],
    [8, 7, 0, 3, 0, 0, 0, 2, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 2], 
    [0, 9, 0, 0, 0, 0, 6, 1, 0],  
    [3, 6, 0, 0, 0, 0, 0, 0, 0],  
    [0, 3, 9, 0, 0, 0, 0, 6, 4], 
    [0, 0, 0, 0, 1, 0, 0, 8, 0], 
    [0, 2, 0, 0, 0, 0, 3, 0, 1] ]

# original tested grid
ogrid = [ 
    [6, 0, 0, 0, 3, 1, 4, 0, 0], 
    [0, 3, 0, 8, 0, 5, 0, 0, 2], 
    [0, 0, 9, 0, 0, 0, 0, 0, 8], 
    [5, 6, 0, 0, 2, 4, 0, 0, 0], 
    [0, 4, 0, 0, 0, 0, 0, 8, 7], 
    [1, 0, 7, 3, 8, 6, 2, 0, 0], 
    [4, 0, 0, 6, 5, 0, 8, 9, 0], 
    [9, 2, 0, 1, 7, 0, 3, 0, 5], 
    [8, 5, 1, 0, 4, 0, 0, 0, 0] ]

# destroyer brute force algorithms
dgrid = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 3, 0, 8, 5], 
    [0, 0, 1, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 5, 0, 7, 0, 0, 0], 
    [0, 0, 4, 0, 0, 0, 1, 0, 0], 
    [0, 9, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 7, 3], 
    [0, 0, 2, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 4, 0, 0, 0, 9] ]

# function to create grig line by line 
def create_grid():
    newgrid = []
    print("Create new grid row by row: ")
    for l in range (0,9):
        while True:
            line = (input(f"Write row {l+1}: "))
            if len(line) == 9:
                # change string line into list if ints
                line = list(map(int, line))
                newgrid.append(line)
                break
            print("Row must be 9 numbers long!")
    return(newgrid)

# simple grid printer
def print_grid(board):
    for iteration, row in enumerate(board):
        print(f"#{iteration+1}:{row}")
    print(" ----------------------------")

# export sudoku grid to file.txt
def export_grid(txtfile, board):
    with open(txtfile, 'w') as file:
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in board)

# import sudoku grid from file.txt
def import_grid(txtfile):
    board = []
    with open(txtfile, 'r') as file:
        for line in file:
            number_strings = line.split() # split the line of runs of whitespace
            numbers = [int(n) for n in number_strings] # convert to integers
            board.append(numbers) # add the "row" to list
    return(board)