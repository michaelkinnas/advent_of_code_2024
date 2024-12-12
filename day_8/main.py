data = open('day_8/data.txt', 'r').read().splitlines()
grid = [[x for x in line] for line in data]

'''
TODO Refactor some of the code, but since this puzzle was pure torture I will probably not do it.
'''

frequencies = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frequencies += frequencies.lower()
frequencies += '0123456789'


def print_grid(grid):
    stra = ''
    for line in grid:
        for char in line:
            stra += char
        stra += '\n'
    print(stra)


def calculate_blocked_line_of_sight_cells(antenna_x, antenna_y, obstruction_x, obstruction_y, grid):
    blocked_locations = set()
    offset_x = obstruction_x - antenna_x
    offset_Y = obstruction_y - antenna_y
    x = obstruction_x + offset_x
    y = obstruction_y + offset_Y
    while (x < len(grid) and x >= 0 and y < len(grid[0]) and y >= 0):
        blocked_locations.add((x, y))
        x += offset_x
        y += offset_Y
    blocked_locations.add((antenna_x, antenna_y))
    return blocked_locations


def calculate_antinode_cell(antenna_x, antenna_y, obstruction_x, obstruction_y, grid):
    offset_x = obstruction_x - antenna_x
    offset_Y = obstruction_y - antenna_y
    antinode_x = obstruction_x + offset_x
    antinode_y = obstruction_y + offset_Y
    if antinode_y < len(grid) and antinode_y >= 0 and antinode_x < len(grid[0]) and antinode_x >= 0:
        return (antinode_x, antinode_y)

def find_antinodes_from_this_position(pos_x, pos_y, grid):
    # search bottom right quadrant
    antinodes = set()
    blocked_locations = set()
    for y in range(pos_y, len(grid)):
        for x in range(pos_x, len(grid[0])):
            if (x, y) in blocked_locations: continue
            if (x, y) == (pos_x, pos_y): continue
            if grid[y][x] == grid[pos_y][pos_x]:
               for i in calculate_blocked_line_of_sight_cells(pos_x, pos_y, x, y, grid):
                   blocked_locations.add(i)
               antinodes.add(calculate_antinode_cell(pos_x, pos_y, x, y, grid))

    # bottom left quadrant
    for y in range(pos_y, len(grid)): 
        for x in range(pos_x, -1, -1):
            if (x, y) in blocked_locations: continue
            if (x, y) == (pos_x, pos_y): continue
            if grid[y][x] == grid[pos_y][pos_x]:
                for i in calculate_blocked_line_of_sight_cells(pos_x, pos_y, x, y, grid):
                    blocked_locations.add(i)
                antinodes.add(calculate_antinode_cell(pos_x, pos_y, x, y, grid))

    # top left quadrant
    for y in range(pos_y, -1, -1): 
        for x in range(pos_x, -1, -1):
            if (x, y) in blocked_locations: continue
            if (x, y) == (pos_x, pos_y): continue
            if grid[y][x] == grid[pos_y][pos_x]:
                for i in calculate_blocked_line_of_sight_cells(pos_x, pos_y, x, y, grid):
                    blocked_locations.add(i)
                antinodes.add(calculate_antinode_cell(pos_x, pos_y, x, y, grid))

    # top right quadrant
    for y in range(pos_y, -1, -1): 
        for x in range(pos_x, len(grid[0])):
            if (x, y) in blocked_locations: continue
            if (x, y) == (pos_x, pos_y): continue
            if grid[y][x] == grid[pos_y][pos_x]:
                for i in calculate_blocked_line_of_sight_cells(pos_x, pos_y, x, y, grid):
                    blocked_locations.add(i)
                antinodes.add(calculate_antinode_cell(pos_x, pos_y, x, y, grid))

    return antinodes, blocked_locations


def mark_antinodes(blocked_positions, grid):
    for (x, y) in blocked_positions:
        # if grid[y][x] not in frequencies:
        grid[y][x] = '#'


antinodes = set()
repeated_antinodes_set = set()
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] in frequencies:
            ant, rant = find_antinodes_from_this_position(x, y, grid)
            for i in ant:
                if i is not None:
                    antinodes.add((i[0], i[1]))
  
            for i in rant:
                repeated_antinodes_set.add((i[0], i[1]))

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(repeated_antinodes_set)}")
