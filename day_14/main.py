data = [x.split(" ") for x in open('day_14/data.txt', 'r').readlines()]

coords = [[int(y) for y in x[0][2:].split(",")] for x in data]
velocities = [[int(y) for y in x[1][2:].removesuffix("\n").split(",")] for x in data]

# test size
# floor_width = 11
# floor_height = 7

floor_width = 101
floor_height = 103

grid = [["." for x in range(floor_width)] for y in range(floor_height)]

for x, y in coords:
    grid[y][x] = 0

def print_grid(grid):
    stra = ''
    for line in grid:
        for char in line:
            stra += '.' if char == 0 else str(char)
        stra += '\n'
    print(stra)

def update_grid(grid, coords):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = 0

    for x, y in coords:
        grid[y][x] += 1


def calculate_safety_factor(grid):
    tlq = 0
    blq = 0
    trq = 0
    brq = 0

    for y in range(0, len(grid) // 2):
        for x in range(0, len(grid[0]) // 2):
            tlq += grid[y][x]

    for y in range((len(grid) // 2) + 1, len(grid)):
        for x in range(0, len(grid[0]) // 2):
            blq += grid[y][x]

    for y in range(0, len(grid) // 2):
        for x in range((len(grid[0]) // 2) + 1, len(grid[0])):
            trq += grid[y][x]

    for y in range((len(grid) // 2) + 1, len(grid)):
        for x in range((len(grid[0]) // 2) + 1, len(grid[0])):
            brq += grid[y][x]

    return tlq * blq * trq * brq
        
dangers = []
for i in range(10000):
    for j in range(len(coords)):
        coords[j][0] = (coords[j][0] + velocities[j][0]) % floor_width
        coords[j][1] = (coords[j][1] + velocities[j][1]) % floor_height

    update_grid(grid, coords)
    dangers.append(calculate_safety_factor(grid))

    if i == 99:
        print("Part 1: ", calculate_safety_factor(grid))

    # this index is calculated from numpy argmin bellow. yes i'm lazy
    # if you want to visualize the tree run the code again with the bellow three lines uncommented    
    # if i == 7891: 
    #     print_grid(grid)
    #     input()

from numpy import argmin
print("Part 2: ", argmin(dangers) + 1)

