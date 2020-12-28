import grids, random, solver
from sys import argv, exit
print("***** Sudoku generator v0.1 *****")

grid = grids.zgrid
# open textfile to save generated grid
text_file = open("generated_sudoku.txt", "w+")

print("Number of empty spots: ", len(solver.emptyList(grid)))

ggrid = solver.rnd_solve(grid)

grids.print_grid(ggrid)

number_of_cells = int(input("How many empty spaces? "))

print("You want to erase ", number_of_cells, "numbers")
if solver.clean_cells(ggrid, number_of_cells) != 0:
    exit(1)

grids.print_grid(ggrid)
if solver.test_if_unique(ggrid) == True:
    print("This grid has one valid solution.")
else:
    print("Error! - Grid has multiple solutions.")
    
grids.export_grid("generated_sudoku.txt", ggrid)


