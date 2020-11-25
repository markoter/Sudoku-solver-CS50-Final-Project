import solver, grids, random
from sys import argv, exit
print("***** Sudoku solver v0.2 *****")

if (len(argv) == 1) or (argv[1] == 'easy'):
    grid = grids.ogrid
elif argv[1] == 'new':
    grid = grids.create_grid()
elif argv[1] == 'zero':
    grid = grids.zgrid
elif argv[1] == 'hard':
    grid = grids.hgrid
elif argv[1] == 'destroy':
    grid = grids.dgrid
else:
    print("****** Wrong command!")
    print("*******'new' - create your own grid")
    print("*******'easy'or none - run for easy grid")
    print("*******'zero' - run for empty grid")
    print("*******'hard' - run for hard grid")
    print("*******'destroy' - run for bruteforce breaker grid")
    exit(1)

# debug printer
print(f"Empty spots to fill: {len(solver.emptyList(grid))}")

print("Original sudoku grid:")
indx = 0
for row in grid:
    indx +=1
    print(f"#{indx}:{row}")

print("Sudoku solved with normal algorithm after changes:")
newGrid = solver.solve(grid)
indx = 0
for row in newGrid:
    indx +=1
    print(f"#{indx}:{row}")

print("Sudoku solved with random algorithm after changes:")
newRandomGrid = solver.rnd_solve(grid)
indx = 0
for row in newRandomGrid:
    indx +=1
    print(f"#{indx}:{row}")

print("Original sudoku grid:")
indx = 0
for row in grid:
    indx +=1
    print(f"#{indx}:{row}")