def ask_by_elem():
    grid = []
    for _ in range (0,3):
        line = []
        for _ in range (0,3):
            print("write element:")
            line.append(input())
        grid.append(line)
    for row in grid:
        print(row)

def create_grid():
    newgrid = []
    print("Create new grid row by row: ")
    for l in range (0,9):
        while True:
            line = (input(f"Write row {l+1}: "))
            if len(line) == 9:
                # change string line into list if ints
                line = list(map(int, line))
                newgrid.append(line)
                break
            print("Row must be 9 numbers long!")
    return(newgrid)
    # print
    for row in newgrid:
        print(row)

create_grid()