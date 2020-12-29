import solver, grids, random, time
from sys import argv, exit
print("***** Sudoku solver v0.3 terminal edition *****")

# terminal 
def main():
    if len(argv) == 2:
        if argv[1] == 'new':
            new_sudoku()
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

# import, solve and export sollution
def import_sudoku(filenametxt):
    # import
    imported_grid = grids.import_grid(filenametxt)
    # print imported grid
    print(f"\nSudoku imported from: {filenametxt}:")
    grids.print_grid(imported_grid)    
    # solve, print and export sollution
    solving_start = time.time()
    solved_grid = solver.solve(imported_grid)
    solving_time = (time.time() - solving_start)
    print(f"\nSollution (in {solving_time} seconds):")
    grids.print_grid(solved_grid)
    grids.export_grid("imported_sudoku_sollution.txt", solved_grid)

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
    print(f"\nGenerated sudoku grid:")
    grids.print_grid(board)
    # check if it has only one sollution
    if solver.test_if_unique(board) == True:
        print("This grid has one valid solution.")
    else:
        print("Warning! - Grid has multiple solutions, better try again.")
    # export generated grid to txt file
    grids.export_grid(f"generated_sudoku_with_{number_zeros}_emptycells.txt", board)

# function to write new sudoku right through terminal
def new_sudoku():
    # create new grid line by line by user
    new_grid = grids.create_grid()
    # print and export created grid
    print(f"\nGenerated sudoku grid:")
    grids.print_grid(new_grid)
    grids.export_grid("new_sudoku.txt", new_grid)
    # solve, print and export sollution
    solved_new_grid = solver.solve(new_grid)
    print(f"\nSolved new sudoku grid:")
    grids.print_grid(solved_new_grid)
    grids.export_grid("new_sudoku_sollution.txt", solved_new_grid)

# run main
main()

"""
# debug printer
print(f"Empty spots to fill: {len(solver.emptyList(grid))}")

print("Sudoku solved with normal algorithm after changes:")
newGrid = solver.solve(grid)
grids.print_grid(newGrid)

print("Sudoku solved with random algorithm after changes:")
newRandomGrid = solver.rnd_solve(grid)
grids.print_grid(newRandomGrid)
'''
"""