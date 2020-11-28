import grids, random, solver
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid

print("Number of empty spots: ", len(solver.emptyList(grid)))

ggrid = solver.rnd_solve(grid)

grids.print_grid(ggrid)

number_of_cells = int(input("How many empty spaces? "))

print("you want to erase ", number_of_cells, "numbers")
solver.clean_cells(ggrid, number_of_cells)

grids.print_grid(ggrid)


