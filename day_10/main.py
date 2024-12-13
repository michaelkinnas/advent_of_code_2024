data = open('day_10/data.txt', 'r').read().splitlines()
grid = [[int(x) if x != '.' else '.' for x in line ] for line in data]

# print(grid)

def find_next_steps(pos_x, pos_y, grid):
    directions = [(pos_x-1, pos_y), (pos_x, pos_y+1), (pos_x+1, pos_y), (pos_x, pos_y-1)]
    valid_directions = []
    for (x, y) in directions:
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): continue
        if grid[y][x] == '.': continue
        # print(pos_x, pos_y, x, y,  grid[y][x] - grid[pos_y][pos_x])
        if grid[y][x] - grid[pos_y][pos_x] == 1:
            valid_directions.append((x,y))

    return valid_directions

def walk(pos_x, pos_y, grid):
    paths = set()
    if grid[pos_y][pos_x] == 9:
        paths.add((pos_x, pos_y))
        return paths
    
    valid_directions = find_next_steps(pos_x, pos_y, grid)
    # print(pos_x, pos_y, valid_directions)
    if len(valid_directions) > 0:
        for x, y in valid_directions:
            paths.update(walk(x, y, grid))

    return paths


def walk2(pos_x, pos_y, grid):
    paths = 0
    if grid[pos_y][pos_x] == 9:
        paths += 1
        return paths
    
    valid_directions = find_next_steps(pos_x, pos_y, grid)
    # print(pos_x, pos_y, valid_directions)
    if len(valid_directions) > 0:
        for x, y in valid_directions:
            paths += walk2(x, y, grid)

    return paths
    
valid_paths = 0
distinct_paths = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 0:
            found_paths = walk(x, y, grid)
            distinct_paths += walk2(x, y, grid)
            valid_paths += len(found_paths)
        
            

print("Part 1:", valid_paths)

print("Part 2:", distinct_paths)

# print(find_next_steps(0, 3, grid))


