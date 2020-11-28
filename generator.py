import grids, random, solver
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid

print("Number of empty spots: ", len(solver.emptyList(grid)))

ggrid = solver.rnd_solve(grid)

grids.print_grid(ggrid)

numbers_to_remove = input("How many empty spaces?")

print("you want to erase ", numbers_to_remove, "numbers")


