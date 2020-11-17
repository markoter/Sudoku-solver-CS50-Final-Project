import array, random, math, time
import my_functions as f1 
print("***** Sudoku solver v0.1 *****")

# grid with only zeros
zgrid = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

# hard grid that brakes the recursion
grid = [ 
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 9, 1, 0, 0, 0],
    [8, 7, 0, 3, 0, 0, 0, 2, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 2], 
    [0, 9, 0, 0, 0, 0, 6, 1, 0],  
    [3, 6, 0, 0, 0, 0, 0, 0, 0],  
    [0, 3, 9, 0, 0, 0, 0, 6, 4], 
    [0, 0, 0, 0, 1, 0, 0, 8, 0], 
    [0, 2, 0, 0, 0, 0, 3, 0, 1] ]

# original tested grid
ogrid = [ 
    [6, 0, 0, 0, 3, 1, 4, 0, 0], 
    [0, 3, 0, 8, 0, 5, 0, 0, 2], 
    [0, 0, 9, 0, 0, 0, 0, 0, 8], 
    [5, 6, 0, 0, 2, 4, 0, 0, 0], 
    [0, 4, 0, 0, 0, 0, 0, 8, 7], 
    [1, 0, 7, 3, 8, 6, 2, 0, 0], 
    [4, 0, 0, 6, 5, 0, 8, 9, 0], 
    [9, 2, 0, 1, 7, 0, 3, 0, 5], 
    [8, 5, 1, 0, 4, 0, 0, 0, 0] ]



# debug printer
emptySpot = f1.emptyList(grid)
print(f"empty spots to fill: {len(emptySpot)}")
#for position in emptySpot:
#  print(position)

print("Original sudoku grid:")
for row in grid:
    print(row)

print("Sudoku after changes:")
newGrid = f1.if_fits(grid, 0, f1.emptySpots)
for row in newGrid:
    print (row)