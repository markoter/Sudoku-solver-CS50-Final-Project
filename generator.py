import solver, grids, random
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid

emptySpots = solver.emptyList(grid)

print("Number of empty spots: ", len(emptySpots))

random.shuffle(emptySpots)

ggrid = solver.solve(grid, 0, emptySpots)

indx = 0
for row in ggrid:
    indx +=1
    print(f"#{indx}:{row}")




