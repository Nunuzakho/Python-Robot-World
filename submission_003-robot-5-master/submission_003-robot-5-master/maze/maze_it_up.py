
obstacle_size = 4
# area limit vars
min_y, max_y = -48, 48
min_x, max_x = -48, 48

blocks = []


maze_layout = [[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,],
               [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,],
               [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,],
               [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,],
               [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,],
               [1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,],
               [1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,],
               [1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,],
               [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,],
               [1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,],
               [1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,0,],
               [1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,], #mid-point
               [1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,],
               [1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,],
               [1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,],
               [1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,],
               [1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,],
               [1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,],
               [1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,],
               [1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,],
               [1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,],
               [1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,0,1,],
               [1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,],
               [1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,1,1,],]


def get_obstacles():
    '''This function displays/makes obstacles from the Maze-layout.
    * The 1s represents the "cells" which are obstacles.
    * The 0s represents the pathway of the maze.
    * The maze cells are 4 by 4.
    * The maze (overall) has 25 blocks(empty blocks included) 
    '''
    maze = maze_layout
    blocks = []
    white_blocks = []
    y = max_y
  
    
    for row in maze:
        row.reverse()
        x = max_x
        y-=4
        for col in row:
            x-=4
            if col == 1:
                blocks.append((x,y))
            elif col == 0:
                white_blocks.append((x,y))  
    return blocks, white_blocks 


def is_position_blocked(x,y,obstacles):
    '''This function checks for blocked path-ways.
    * The red blocks(set as blocked co-ordinates) represents the blocked path that the Robot won't be able to access.
    '''
    for obstacle in obstacles:
        if x in range(obstacle[0]+1, obstacle[0]+obstacle_size) and y in range(obstacle[1]+1, obstacle[1]+obstacle_size):
            return True
    return False

def is_path_blocked(x1,y1,x2,y2,obstacles):
    '''This function checks for a blocked path-way when the Robot goes towards it.
    '''
    for num in range(min(x1, x2), max(x1, x2)+1):
        if is_position_blocked(num, y1,obstacles):
            return True

    for num in range(min(y1, y2), max(y1, y2)+1):
        if is_position_blocked(x1, num,obstacles):
            return True
    return False

def safe_path(dir_order, command_arg, obstacles):
    '''This function executes a safe path in the maze-layout for the Robot to go through when a command_arg(ument) is given for what it should do.
    * When a command_arg is registered it wil explore a specific pathway(determined by the command given) and choose when to go: North, South, East, West.
    '''
    no_obstacles = obstacles[1]
    to_be_explored = []
    explored = []
    path = {}

    x,y = 0,0

    to_be_explored.append((x,y))
    explored.append((x,y))

    while len(to_be_explored) > 0:
        if(command_arg == 'top' or command_arg == '') and y == max_y-4:
            break
        if command_arg == 'left' and x == min_x:
            break
        if command_arg == 'right' and x == max_x-4:
            break
        if command_arg == 'bottom' and y == min_y:
            break
        x,y = to_be_explored.pop()
        for dir in dir_order:
            if (x+4,y) in no_obstacles and (x+4,y) not in explored and dir == 'e':
                block = (x+4,y)
                path[block] = (x,y)
                to_be_explored.append(block)
                explored.append(block)

            if (x-4,y) in no_obstacles and (x-4,y) not in explored and dir == 'w':
                block = (x-4,y)
                path[block] = (x,y)
                to_be_explored.append(block)
                explored.append(block)

            if (x,y+4) in no_obstacles and (x,y+4) not in explored and dir == 'n':
                block = (x,y+4)
                path[block] = (x,y)
                to_be_explored.append(block)
                explored.append(block)

            if (x,y-4) in no_obstacles and (x,y-4) not in explored and dir == 's':
                block = (x,y-4)
                path[block] = (x,y)
                to_be_explored.append(block)
                explored.append(block)
    
    # print(explored)
    return path

            



