data = open("day_12/test5.txt").read().splitlines()
grid = [[x for x in line] for line in data]

#TODO Deal with case of having enclosed pathces by other patches like in test2. It only measures the outside

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


def get_forward_coords(direction, x, y):
    if direction == 'N':
        return x, y-1
    elif direction == 'E':
        return x+1, y
    elif direction == 'S':
        return x, y+1
    elif direction == 'W':
        return x-1, y

def turn_right(direction):
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'
    
def turn_left(direction):
    if direction == 'N':
        return 'W'
    elif direction == 'E':
        return 'N'
    elif direction == 'S':
        return 'E'
    elif direction == 'W':
        return 'S'

def get_left_coords(direction, x, y):
    if direction == 'N':
        return x-1, y
    elif direction == 'E':
        return x, y-1
    elif direction == 'S':
        return x+1, y
    elif direction == 'W':
        return x, y+1

# def is_out_of_grid_bounds(x, y, grid):
#     return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def is_singular(x, y, grid):
    plant = grid[y][x]
    if is_inside_grid(x+1, y, grid) and grid[y][x+1] != plant and is_inside_grid(x, y+1, grid) and grid[y+1][x] != plant and is_inside_grid(x-1, y, grid) and grid[y][x-1] != plant and is_inside_grid(x, y-1, grid) and grid[y-1][x] != plant:
        return True
    

def is_single_isolated(x, y, grid):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): return False
    return grid[y][x-1] == grid[y-1][x] == grid[y][x+1] == grid[y+1][x]


def get_left_border_id(direction, x, y, grid, patch_ids):
    coord_x, coord_y = get_left_coords(direction, x, y)
    if not is_inside_grid(coord_x, coord_y, grid): return 'OUT'
    if (coord_x, coord_y) not in patch_ids: return 'OUT'
    return patch_ids[(coord_x, coord_y)]


def walk_perimeter(plant, x, y, grid, patch_ids):
    #find top edge
    current_x = x
    current_y = y
    # print("Start at", current_x, current_y)
    while True:
        current_y -= 1
        if grid[current_y][current_x] != plant: 
            current_y += 1
            break

        if current_y < 0:
            current_y += 1
            break 
        
        # print("Move at", current_x, current_y)

    border_ids_count = {}
    direction = 'E'
    
    start_x = current_x
    start_y = current_y
    # print("found edge at", current_x, current_y)

    # need to check this aswell omg this code is bad
    if is_singular(current_x, current_y, grid):
        if is_single_isolated(current_x, current_y, grid):
            return 4, patch_ids[(current_x, current_y-1)]
        return 4, None
    

    border_id = get_left_border_id(direction, current_x, current_y, grid, patch_ids)
    if border_id not in border_ids_count:
        border_ids_count[border_id] = 1
    else:
        border_ids_count[border_id] += 1

    turns = 0

    forward_x, forward_y = get_forward_coords(direction, current_x, current_y)    
    if not is_inside_grid(forward_x, forward_y, grid) or grid[forward_y][forward_x] != plant:
        direction = turn_right(direction)
        turns += 1
    # print("position and direction:", current_x, current_y, direction)
    current_x, current_y = get_forward_coords(direction, current_x, current_y)

    border_id = get_left_border_id(direction, current_x, current_y, grid, patch_ids)
    if border_id not in border_ids_count:
        border_ids_count[border_id] = 1
    else:
        border_ids_count[border_id] += 1


    # print("position and direction:", current_x, current_y, direction)
    while not (current_x == start_x and current_y == start_y and direction == 'E'):
        left_x, left_y = get_left_coords(direction, current_x, current_y)
        forward_x, forward_y = get_forward_coords(direction, current_x, current_y)
        if is_inside_grid(left_x, left_y, grid) and grid[left_y][left_x] == plant: #if left is valid turn left
            direction = turn_left(direction)
            turns += 1
            current_x, current_y = get_forward_coords(direction, current_x, current_y)

            border_id = get_left_border_id(direction, current_x, current_y, grid, patch_ids)
            if border_id not in border_ids_count:
                border_ids_count[border_id] = 1
            else:
                border_ids_count[border_id] += 1
            # print("Turned left")

        elif (not is_inside_grid(left_x, left_y, grid) or grid[left_y][left_x] != plant) and (not is_inside_grid(forward_x, forward_y, grid) or grid[forward_y][forward_x] != plant):
            direction = turn_right(direction)
            turns += 1

            border_id = get_left_border_id(direction, current_x, current_y, grid, patch_ids)
            if border_id not in border_ids_count:
                border_ids_count[border_id] = 1
            else:
                border_ids_count[border_id] += 1
            # print("Turned right")

        else: 
            current_x, current_y = get_forward_coords(direction, current_x, current_y)

            border_id = get_left_border_id(direction, current_x, current_y, grid, patch_ids)
            if border_id not in border_ids_count:
                border_ids_count[border_id] = 1
            else:
                border_ids_count[border_id] += 1

    if len(border_ids_count) == 1 and not 'OUT' in border_ids_count:
        return turns, list(border_ids_count.keys())[0]
    return turns, None


def print_grid(grid):
    stra = ''
    for line in grid:
        for char in line:
            stra += char
        stra += '\n'
    print(stra)

def mark_processed(visited, grid):
    for (x ,y) in visited:
        grid[y][x] = '.'

total = 0
total2 = 0
patch_ids = {}
processed_cells = set()
# patch_perimeters = {}
patch_edges = {}
patch_areas = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x,y) not in processed_cells:
            visited = set()
            perimeter = calculate_perimeter(grid[y][x], x, y, grid, visited)
            for cell in visited:
                processed_cells.add(cell)      
                patch_ids[cell] = (x,y)
            total += perimeter * len(visited)
            patch_areas[(x,y)] = len(visited)
            edges, isolated_by = walk_perimeter(grid[y][x], x, y, grid, patch_ids)
            if isolated_by is not None:
                patch_edges[isolated_by] += edges
                print(x+1, y+1, "isolated by" , isolated_by[0]+1, isolated_by[1]+1)
            patch_edges[(x,y)] = edges


# mark_processed(visited, grid)

for key in patch_areas.keys():
    print(key, patch_edges[key], patch_areas[key])
    total2 += patch_areas[key] * patch_edges[key]

print(f"Part 1:", total)
print(f"Part 2:", total2)

# 875206 too low
# 965918 too high!!!!!!!
# 910358 this is wrong also!!!! ALL TESTS PASS BUT INPUT FAILS. REALLY????

