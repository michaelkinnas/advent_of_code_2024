data = open("day_12/data.txt").read().splitlines()
grid = [[x for x in line] for line in data]


def is_inside_grid(x, y, grid):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


visited = set()
def calculate_perimeter(plant, pos_x, pos_y, grid, visited):    
    if not is_inside_grid(pos_x, pos_y, grid): return 1
    if grid[pos_y][pos_x] != plant: return 1
    visited.add((pos_x,pos_y))
    neighbors = [(pos_x + 1, pos_y), (pos_x, pos_y + 1), (pos_x-1, pos_y), (pos_x, pos_y - 1)]
    perimeter = 0
    for x, y in neighbors:
        if (x, y) in visited: continue       
        perimeter += calculate_perimeter(plant, x, y, grid, visited)
    return perimeter


def mark_processed(visited, grid):
    for (x ,y) in visited:
        grid[y][x] = '.'

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != '.':        
            visited = set()
            perimeter = calculate_perimeter(grid[y][x], x, y, grid, visited)
            mark_processed(visited, grid)
            total += perimeter * len(visited)

print(f"Part 1:", total)

