import solver, grids, random
from sys import argv, exit
print("***** Sudoku solver v0.3 terminal edition *****")

# terminal 
def main():
    if len(argv) == 2:
        if argv[1] == 'new':
            print("TODO writing new board")
        else:
            usage_and_exit()
    elif len(argv) == 3:
        if (argv[1] == 'generate') and (argv[2] != False):
            generate_sudoku(argv[2])
        elif (argv[1] == 'import') and (argv[2] != False):
            print("TODO import grid from file and solve it")
            import_sudoku(argv[2])
        else:
            usage_and_exit()
    else:
        usage_and_exit()

# function to call when wrong command       
def usage_and_exit():
    print(" Usage:")
    print("  py sudoku_v03_terminal.py [import] [file.txt] - import sudoku board from file and solve it")
    print("  py sudoku_v03_terminal.py [generate] [int (1 to 81)] [] - generate sudoku board and export it into file")
    print("  py sudoku_v03_terminal.py [new] - write new sudoku board, line by line to solve by program")
    exit(1)

# Todo
def import_sudoku(filenametxt):
    imported_grid = grids.import_grid(filenametxt)
    print(f"\nSudoku imported from: {filenametxt}:")
    grids.print_grid(imported_grid)    
    solved_grid = solver.solve(imported_grid)
    print(f"\nSollution:")
    grids.print_grid(solved_grid)
# function to generate and export sudoku grid
def generate_sudoku(number_zeros):
    try: 
        number_zeros = int(number_zeros)
    except:
        print("Error ! - You should write int number in range (1,81)")
        exit(1)
    board = solver.rnd_solve(grids.zgrid)

    # clean some cells
    solver.clean_cells(board, number_zeros)

    # print generated sudoku board
    grids.print_grid(board)

    # check if it has only one sollution
    if solver.test_if_unique(board) == True:
        print("This grid has one valid solution.")
    else:
        print("Warning! - Grid has multiple solutions, so it's no good.")
    
    # export generated grid to txt file
    grids.export_grid(f"generated_sudoku_with_{number_zeros}_emptycells.txt", board)





# run main
main()

"""
# debug printer
print(f"Empty spots to fill: {len(solver.emptyList(grid))}")

print("Original sudoku grid:")
grids.print_grid(grid)

# debug test unique
result_unique = solver.test_if_unique(grid)
print(f" is it unique - {result_unique}")
'''
print("Sudoku solved with normal algorithm after changes:")
newGrid = solver.solve(grid)
grids.print_grid(newGrid)

print("Sudoku solved with random algorithm after changes:")
newRandomGrid = solver.rnd_solve(grid)
grids.print_grid(newRandomGrid)
'''
"""