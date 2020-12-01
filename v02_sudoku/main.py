import array, random, math, time
import solver
import grids
print("***** Sudoku solver v0.2 *****")

grid = grids.grid
emptySpots = solver.emptyList(grid)

# debug printer
print(f"Empty spots to fill: {len(emptySpots)}")

print("Original sudoku grid:")
for row in grid:
    print(row)

print("Sudoku after changes:")
newGrid = solver.solve(grid, 0, emptySpots)
for row in newGrid:
    print (row)