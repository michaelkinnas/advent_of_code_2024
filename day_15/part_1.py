data = open("day_15/data.txt", 'r').readlines()

#parse data like an idiot
grid = []
instructions = []
for line in data:
    new_line = []
    for char in line:
        if char != '\n' and char not in ['<', '^', 'v', '>'] and char != " ":
            new_line.append(char)
        if char in ['<', '^', 'v', '>']:
            instructions.append(char)
    if len(new_line) > 0:
        grid.append(new_line)

#a little easier to read the code if the robot is a class (for me atleast)
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@':
            robot = Robot(x, y, instructions)


def print_grid(grid):
    stra = ''
    for line in grid:
        for char in line:
            stra += char
        stra += '\n'
    print(stra)


def is_inside_grid(x, y, grid):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


def get_new_coords_ahead(x, y, direction):
    if direction == '>':
        x = x + 1
    elif direction == 'v':
        y = y + 1 
    elif direction == '<':
        x = x - 1
    elif direction == '^':
        y = y - 1
    return x, y


def is_empty_space(x, y, grid):
    return grid[y][x] == '.'


def is_box(x, y, grid):
    return grid[y][x] == 'O'


def is_border(x, y, grid):
    return grid[y][x] == '#'


def push_box(x, y, direction, grid):
    new_x, new_y = get_new_coords_ahead(x, y, direction)
    if is_box(new_x, new_y, grid):
        push_box(new_x, new_y, direction, grid)
    if is_empty_space(new_x, new_y, grid):
        grid[new_y][new_x] = 'O'
        grid[y][x] = '.'


def calculate_gps_sum(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                total += y * 100 + x
    return total


def execute_instruction(grid, robot, direction):
    # if empty space in front just move
    # if box in front check for empty space in the direction
    # if wall ahead do nothing
    new_x, new_y = get_new_coords_ahead(robot.x, robot.y, direction)
    if is_inside_grid(new_x, new_y, grid):
        if is_box(new_x, new_y, grid):
            push_box(new_x, new_y, direction, grid)
        if is_empty_space(new_x, new_y, grid):               
            grid[new_y][new_x] = '@'
            grid[robot.y][robot.x] = '.'
            robot.x = new_x
            robot.y = new_y


for instruction in instructions:
    execute_instruction(grid, robot, instruction)
    # print_grid(grid)
    # print(instruction)
    # input()

print("Part 1:", calculate_gps_sum(grid))
