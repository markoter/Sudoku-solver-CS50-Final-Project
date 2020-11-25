import grids, random, solver
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid

print("Number of empty spots: ", len(solver.emptyList(grid)))

ggrid = solver.rnd_solve(grid)

indx = 0
for row in ggrid:
    indx +=1
    print(f"#{indx}:{row}")




