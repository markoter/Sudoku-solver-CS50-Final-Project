import solver, grids, random
from sys import argv, exit
print("***** Sudoku solver v0.2 *****")

if len(argv) != 2:
    grid = grids.zgrid
elif argv[1] == 'new':
    grid = grids.create_grid()
else:
    print("****** Wrong command!")
    print("*******'new' - create your own grid")
    print("******* none - run for default grid")
    exit(1)

emptySpots = solver.emptyList(grid)
random.shuffle(emptySpots)

# debug printer
print(f"Empty spots to fill: {len(emptySpots)}")

print("Original sudoku grid:")
indx = 0
for row in grid:
    indx +=1
    print(f"#{indx}:{row}")

print("Sudoku after changes:")
newGrid = solver.solve(grid, 0, emptySpots)
indx = 0
for row in newGrid:
    indx +=1
    print(f"#{indx}:{row}")