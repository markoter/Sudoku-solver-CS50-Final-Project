import solver, grids
from sys import argv, exit
print("***** Sudoku solver v0.2 *****")

if len(argv) != 2:
    grid = grids.grid
elif argv[1] == 'new':
    grid = grids.create_grid()

emptySpots = solver.emptyList(grid)


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