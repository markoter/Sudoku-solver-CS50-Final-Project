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
    for _ in range (0,3):
        line = (input("write line: "))
        grid.append(line)
    for row in grid:
        print(row)

ask_by_elem()