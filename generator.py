import solver, grids, random
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid

emptySpots = solver.emptyList(grid)

print("Number of empty spots: ", len(emptySpots))
rnd = random.randint(1,10)
for i in range(0, 99):
    print(f"#{i} random - {random.randint(1,9)}")
