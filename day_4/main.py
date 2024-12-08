data = open('day_4/data', 'r').read()
matrix = data.splitlines()

matrix = [[char for char in line] for line in matrix]

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])-3):
        if matrix[i][j] == 'X' and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
            count += 1
        elif matrix[i][j] == 'S' and matrix[i][j+1] == 'A' and matrix[i][j+2] == 'M' and matrix[i][j+3] == 'X':
            count += 1 

# vertical
for i in range(len(matrix)-3):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X' and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
            count += 1
        elif matrix[i][j] == 'S' and matrix[i+1][j] == 'A' and matrix[i+2][j] == 'M' and matrix[i+3][j] == 'X':
            count += 1 

# diagonal top left to bootom right
for i in range(len(matrix)-3):
    for j in range(len(matrix[i])-3):
        if matrix[i][j] == 'X' and matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
            count += 1
        elif matrix[i][j] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M' and matrix[i+3][j+3] == 'X':
            count += 1 

# diagonal bottom left to top right
for i in range(len(matrix)-3):
    for j in range(len(matrix[i])-3):
        if matrix[i+3][j] == 'X' and matrix[i+2][j+1] == 'M' and matrix[i+1][j+2] == 'A' and matrix[i][j+3] == 'S':
            count += 1
        elif matrix[i+3][j] == 'S' and matrix[i+2][j+1] == 'A' and matrix[i+1][j+2] == 'M' and matrix[i][j+3] == 'X':
            count += 1 

print("Part 1: ", count)

#part2
count2 = 0
for i in range(len(matrix)-2):
    for j in range(len(matrix[i])-2):
        if matrix[i][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'S' and matrix[i+2][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i][j+2] == 'S':
            count2 += 1
        elif matrix[i][j] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M' and matrix[i+2][j] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i][j+2] == 'M':
            count2 += 1
        elif matrix[i][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'S' and matrix[i+2][j] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i][j+2] == 'M':
            count2 += 1
        elif matrix[i][j] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M' and matrix[i+2][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i][j+2] == 'S':
            count2 += 1

print("Part 2: ", count2)