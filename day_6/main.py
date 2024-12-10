data = open('day_6/test.txt', 'r').read().splitlines()

floor = [[x for x in line] for line in data]

class Guard:
    def __init__(self, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction

    def move_forward(self):
        if self.direction == '>':
            self.pos_x += 1
        if self.direction == '<':
            self.pos_x -= 1
        if self.direction == '^':
            self.pos_y -= 1
        if self.direction == 'v':
            self.pos_y += 1
    
    def has_obstacle_ahead(self, floor):
        if self.direction == '>' and floor[self.pos_y][self.pos_x + 1] == '#':
            return True
        if self.direction == '<' and floor[self.pos_y][self.pos_x - 1] == '#':
            return True
        if self.direction == '^' and floor[self.pos_y - 1][self.pos_x] == '#':            
            return True
        if self.direction == 'v' and floor[self.pos_y + 1][self.pos_x] == '#':
            return True
        return False

    def turn_right(self):
        if self.direction == '>':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '<'
        elif self.direction == '<':
            self.direction = '^'
        elif self.direction == '^':
            self.direction = '>'

    def is_at_border_looking_out(self, floor):
        if self.pos_x == len(floor[0])-1 and self.direction == '>':
            return True
        if self.pos_x == 0 and self.direction == '<':
            return True        
        if self.pos_y == len(floor)-1 and self.direction == 'v':
            return True
        if self.pos_y == 0 and self.direction == '^':
            return True
        return False
    
    def is_position_ahead_visited_again(self, floor):
        if self.direction == '>' and floor[self.pos_y][self.pos_x + 1] == self.direction:
            return True
        if self.direction == '<' and floor[self.pos_y][self.pos_x - 1] == self.direction:
            return True
        if self.direction == '^' and floor[self.pos_y - 1][self.pos_x] == self.direction:            
            return True
        if self.direction == 'v' and floor[self.pos_y + 1][self.pos_x] == self.direction:
            return True
        return False

    def is_current_position_visited_again(self, floor):
        return floor[self.pos_y][self.pos_x] == self.direction



#find initial guard position and direction
pos_x, pos_y = None, None
direction = None
for i in range(len(floor)):
    for j in range(len(floor[i])):
        if floor[i][j] in ['v', '^', '<', '>']:
            pos_x, pos_y = j, i
            direction = floor[i][j]

#initialize guard at initial position
guard = Guard(pos_x=pos_x, pos_y=pos_y, direction=direction)

def mark_visited_location(x, y, floor):
    floor[y][x] = 'X'

def mark_count_visited(floor):
    visited = 0
    for line in floor:
        for position in line:
            if position == 'X': visited += 1
    return visited

# mark initial guard position
mark_visited_location(guard.pos_x, guard.pos_y, floor)

#run guard walking prediction
while (not guard.is_at_border_looking_out(floor)):
    if guard.has_obstacle_ahead(floor):        
        guard.turn_right()
    else:
        guard.move_forward()
        mark_visited_location(guard.pos_x, guard.pos_y, floor)

print("Part 1: ", mark_count_visited(floor))

def is_position_visited_again(x, y, guard_direction, floor):
    return floor[y][x] == guard_direction

def mark_visited_location_and_direction(x, y, guard_direction, floor):
    floor[y][x] = guard_direction

                
def print_floor(floor):
    stra = ''
    for line in floor:
        for char in line:
            stra += char
        stra += '\n'
    print(stra)



loops = 0
for i in range(len(floor)):
    print(f"At line {i}")
    for j in range(len(floor[i])):
        temp = [[x for x in line] for line in data]
        temp[i][j] = '#'

        pos_x, pos_y = None, None
        direction = None
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] in ['v', '^', '<', '>']:
                    pos_x, pos_y = j, i
                    direction = temp[i][j]
        #initialize guard at initial position
        guard = Guard(pos_x=pos_x, pos_y=pos_y, direction=direction)

        #mark initial position
        mark_visited_location_and_direction(guard.pos_x, guard.pos_y, guard.direction, temp)

        while (not guard.is_at_border_looking_out(temp)):
            # print(f"Guard is at position {guard.pos_x} {guard.pos_y} with direction {guard.direction}")
            print_floor(temp)
      
            if guard.has_obstacle_ahead(temp):
                guard.turn_right()
            # else:                
            guard.move_forward()

            if guard.is_current_position_visited_again(temp):
                loops += 1
                break

            mark_visited_location_and_direction(guard.pos_x, guard.pos_y, guard.direction, temp)

print(loops)