import array, random, math, time
import my_functions as mf
import grids as gr
print("***** Sudoku solver v0.1 *****")

grid = gr.grid
emptySpots = mf.emptyList(grid)

# debug printer
print(f"Empty spots to fill: {len(emptySpots)}")

print("Original sudoku grid:")
for row in grid:
    print(row)

print("Sudoku after changes:")
newGrid = mf.solve(grid, 0, emptySpots)
for row in newGrid:
    print (row)