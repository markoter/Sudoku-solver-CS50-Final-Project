grid = []
for i in range (0,3):
    line = []
    for j in range (0,3):
        print("write element:")
        line.append(input())
    grid.append(line)
for row in grid:
    print(row)