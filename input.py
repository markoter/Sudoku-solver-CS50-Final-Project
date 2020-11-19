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

def ask_by_line():
    grid = []
    for l in range (0,3):
        line = (input(f"write line {l+1}: "))
        if len(line) != 3:
            print ("it myst be 9 numbers")
            exit()
        grid.append(list(line))
    # print
    for row in grid:
        print(row)

ask_by_line()