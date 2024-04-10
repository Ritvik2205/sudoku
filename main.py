import sys

# Grid size
N = 9

def read_file(filename):
    # read file
    file = open(file=filename, mode='r')
    next(file)
    # initialising values and grid
    i = 0 # row
    j = 0 # column
    grid = [[0 for x in range(N)] for y in range(N)]
    while True:
        j = 0
        line = file.readline()
        for char in line:
            grid[i][j] = int(char)
            j += 1
            if j == N:
                i += 1
                break
        if i == N:
            break
    # print(grid)
    return grid


# check if inserting a number in cell is allowed 
def isCorrect(grid, row, col, num):
    # check for row
    for i in range(N):
        if grid[row][i] == num:
            return False
        
    # check for column
    for i in range(N):
        if grid[i][col] == num:
            return False
        
    # check for square (3x3)
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(int(N/3)):
        for j in range(int(N/3)):
            if grid[startRow + i][startCol + j] == num:
                return False
            
    return True

def printGrid(grid):
    for row in grid:
            print("|", end=" ")
            for num in row:
                print(num, end=" | ")
            print()
            print("-" * (N*3 + (N + 1)))
    return grid

class recursions:
    number_of_recursions = 0

recs= recursions()

def sudokuSolver(grid):
    recs.number_of_recursions += 1
    break_condition = 0
    for i in range(0, N):
        for j in range(0, N):
            if grid[i][j] == 0:
                break_condition = 1
                row = i
                col = j
                break

    if break_condition == 0:
        printGrid(grid)
        print("Number of recursions: ", recs.number_of_recursions)
        exit(0)

    for num in range(1, N+1): 
        if isCorrect(grid, row, col, num):
            grid[row][col] = num
            if sudokuSolver(grid):
                return True
            else:
                grid[row][col] = 0

    return False


grid = read_file(sys.argv[1])
sudokuSolver(grid)