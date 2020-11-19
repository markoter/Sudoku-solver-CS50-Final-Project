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
    print("Write grid line by line: ")
    for l in range (0,9):
        while True:
            line = (input(f"Write row {l+1}: "))
            if len(line) == 9:
                grid.append(list(line))
                break
            print("Row must be 9 numbers long!")
        
    # print
    for row in grid:
        print(row)

ask_by_line()