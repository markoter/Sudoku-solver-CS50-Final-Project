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
    grid = []
    print("Create new grid row by row: ")
    for l in range (0,9):
        while True:
            line = (input(f"Write row {l+1}: "))
            if len(line) == 9:
                line = list(map(int, line))
                grid.append(line)
                break
            print("Row must be 9 numbers long!")
    # print 123123132
    for row in grid:
        print(row)

create_grid()