from ast import arguments
from turtle import forward, left
from unicodedata import name
import import_helper
import sys
# from robot import do_maze_runner
# from maze import maze_it_up
# import world

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

mazes = ['maze_it_up']
if  len(sys.argv)>2 and sys.argv[2] in mazes:
    obstacles = import_helper.dynamic_import('maze.' +sys.argv[2].lower())
    argument = str(sys.argv[2])
    min_y, max_y = -50, 50
    min_x, max_x = -50, 50
else:
    import maze.obstacles as obstacles
    argument = 'obstacles'
    min_y, max_y = -200, 200 # area limit for default obstacles
    min_x, max_x = -100, 100

def show_position(robot_name, position_x, position_y):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, blocks):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    elif directions[current_direction_index] == 'mazerun':
        new_y, new_x = new_y, new_x - steps
    
    if not is_position_allowed(new_x, new_y):
        return False, False
        
    if obstacles.is_path_blocked(position_x, position_y, new_x, new_y, blocks):
        return False, True

    position_x = new_x
    position_y = new_y
    return True, False






def do_forward(robot_name, steps, blocks):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    in_area, blocked = update_position(steps, blocks)
    if in_area and not blocked:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif blocked:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps, blocks):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    # if update_position(-steps):
    in_area, blocked = update_position(-steps, blocks)
    if in_area and not blocked:
        

        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif blocked:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    
       

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    
       

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def show_obstacles(blocks, robot_name, obstacle_size):
    print(f"{robot_name}: Loaded {argument}.")    
    print('There are some obstacles:')
    for obstacle in blocks:
        print(f"- At position {obstacle[0]},{obstacle[1]} (to {obstacle[0]+4},{obstacle[1]+4})")

# def show_obstacles(obstacles, robot_name, obstacle_size):
#     ''' Prints out the obstacles in the Turtle.
#     '''
#     print(f"{robot_name}: Loaded {argument}.")


       


def reset():
    global position_x, position_y, current_direction_index
    position_y = 0
    position_x = 0
    current_direction_index = 0

# def setup_world():
#     pass

