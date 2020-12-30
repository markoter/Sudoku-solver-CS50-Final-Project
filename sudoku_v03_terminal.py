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
        if (argv[1] == 'generate'):
            generate_sudoku(argv[2])
        elif (argv[1] == 'import'):
            import_sudoku(argv[2])
        elif (argv[1] == 'check'):
            check_sudoku(argv[2])
        elif argv[1] == 'new':
            new_sudoku(argv[2])
        else:
            usage_and_exit()
    elif len(argv) == 4:
        if (argv[1] == 'generate'):
            generate_sudoku(argv[2],argv[3])
        else:
            usage_and_exit()
    else:
        usage_and_exit()

# function to call when wrong command       
def usage_and_exit():
    print(" Usage:")
    print("  py sudoku_v03_terminal.py [import] [filename.txt]\n   - import sudoku board from file and solve it.")
    print("  py sudoku_v03_terminal.py [check] [filename.txt]\n   - import sudoku board from file and check if it is valid (has one, unique sollution).")
    print("  py sudoku_v03_terminal.py [generate] [number of empty spots] [*optional_filename.txt]\n   - generate sudoku board with given number of empty spots (from 1 to 81) and export it into file.")
    print("  py sudoku_v03_terminal.py [new] [*optional_filename.txt]\n   - write new sudoku board, line by line and export it to file.")
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

def check_sudoku(filenametxt):
    # import
    imported_grid = grids.import_grid(filenametxt)
    # print imported grid
    print(f"\nSudoku imported from: {filenametxt}:")
    grids.print_grid(imported_grid) 
    # solve, print and export sollution
    solving_start = time.time()
    is_unique = solved_grid = solver.test_if_unique(imported_grid)
    solving_time = (time.time() - solving_start)
    print(f"Checking sudoku took {solving_time} seconds.")
    if is_unique == True:
        print("This sudoku grid is probably valid (has only one sollution).")
    else:
        print("This sudoku has at least 2 different sollutions, so it's not valid.")

# function to generate and export sudoku grid
def generate_sudoku(number_zeros, filenametxt = "generated_sudoku.txt"):
    try: 
        number_zeros = int(number_zeros)
    except:
        print("Error ! - [number of empty spots] - should be number from 1 to 81")
        exit(1)
    if number_zeros not in range(1,81):
        print("Error ! - [number of empty spots] - should be number from 1 to 81")
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
    grids.export_grid(filenametxt, board)

# function to write new sudoku right through terminal
def new_sudoku(filenametxt = "new_sudoku.txt"):
    # create new grid line by line by user
    new_grid = grids.create_grid()
    # print and export created grid
    print(f"\nGenerated sudoku grid:")
    grids.print_grid(new_grid)
    grids.export_grid(filenametxt, new_grid)

# run main
main()