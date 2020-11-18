import array, random, math, time
import my_functions as mf
import grids as gr
print("***** Sudoku solver v0.1 *****")

grid = gr.grid
# debug printer
emptySpots = mf.emptyList(grid)

emptySpot = mf.emptyList(grid)
print(f"empty spots to fill: {len(emptySpot)}")
#for position in emptySpot:
#  print(position)

print("Original sudoku grid:")
for row in grid:
    print(row)

print("Sudoku after changes:")
newGrid = mf.solve(grid, 0, emptySpots)
for row in newGrid:
    print (row)