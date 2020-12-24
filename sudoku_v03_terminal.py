import solver, grids, random
from sys import argv, exit
print("***** Sudoku solver v0.3 terminal edition *****")

def usage_and_exit():
    print(" Usage:")
    print("  py sudoku_v03_terminal.py [import] [file.txt] - import sudoku board from file and solve it")
    print("  py sudoku_v03_terminal.py [generate] [number of empty spaces] - generate sudoku board and export it into file")
    print("  py sudoku_v03_terminal.py [new] - write new sudoku board, line by line to solve by program")
    exit(1)

if len(argv) == 2:
    if argv[1] == 'new':
        print("TODO writing new board")
    else:
        usage_and_exit()
elif len(argv) == 3:
    if (argv[1] == 'generate') and (argv[2] != False):
        print("TODO generate new board with int empty spaces")
    elif (argv[1] == 'import') and (argv[2] != False):
        print("TODO import grid from file and solve it")
    else:
        usage_and_exit()
else:
    usage_and_exit()

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