
import sys
# import turtle

if len(sys.argv) > 1 and sys.argv[1] == "turtle":
    import world.turtle.world as world
else:
    import world.text.world as world
if len(sys.argv) > 2 and sys.argv[2] == "maze_it_up":
   
    import maze.maze_it_up as block
else:
    import maze.obstacles as block

# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint', 'mazerun']
move_commands = valid_commands[3:]

# variables tracking position and direction




#commands history
history = []


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    directions = ['top', 'left', 'bottom', 'right']
    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed','')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    elif command_name.lower() == 'mazerun':
        return arg1 == '' or arg1.lower() in directions
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - redoes the movement commands
REPLAY SILENT - redoes the movemand commands, only by showing the position output
REPLAY REVERSED - redoes the moves in reverse
REPLAY REVERSED SILENT - redoes movements in reverse, only by showing the position output
MAZERUN - solves the maze by itself going to the top
MAZERUN TOP - solves the maze by itself going to the top
MAZERUN BOTTOM - solves the maze by itself going to the bottom
MAZERUN LEFT - solves the maze by itself going to the left
MAZERUN RIGHT - solves the maze by itself going to the right
"""




def do_sprint(robot_name, steps, blocks):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return world.do_forward(robot_name, 1, blocks)
    else:
        (do_next, command_output) = world.do_forward(robot_name, steps, blocks)
        print(command_output)
        return do_sprint(robot_name, steps -1, blocks)


def do_maze_runner(robot_name, obstacles, way_ahead):
    '''This function checks the possible ways to do a mazerun, considering which position it should take.
    '''
    no_obstacle = []
    # way_ahead = block.safe_path('swen','top', obstacles)
    cell = list(way_ahead.keys())[-1]
    
    while cell != (0,0):
        no_obstacle.append(cell)
        cell = way_ahead[cell]
    no_obstacle.append((0,0))
    no_length = len(no_obstacle)
    
    for i in range(no_length):
        cell = no_obstacle.pop()
        if len(no_obstacle) == 0:
            break
        if world.current_direction_index == 0:
            if cell[0] > no_obstacle[-1][0]:
                print(world.do_left_turn(robot_name)[1])
            if cell[0] < no_obstacle[-1][0]:
                print(world.do_right_turn(robot_name)[1])
            if cell[1] > no_obstacle[-1][1]:
                print(world.do_right_turn(robot_name)[1])
                print(world.do_right_turn(robot_name)[1])
        elif world.current_direction_index == 1:
            if cell[1] > no_obstacle[-1][1]:
                print(world.do_right_turn(robot_name)[1])
            if cell[1] < no_obstacle[-1][1]:
                print(world.do_left_turn(robot_name)[1])
            if cell[0] > no_obstacle[-1][0]:
                print(world.do_right_turn(robot_name)[1])
                print(world.do_right_turn(robot_name)[1])
        elif world.current_direction_index == 2:
            if cell[0] > no_obstacle[-1][0]:
                print(world.do_right_turn(robot_name)[1])
            if cell[0] < no_obstacle[-1][0]:
                print(world.do_left_turn(robot_name)[1])
            if cell[1] < no_obstacle[-1][1]:
                print(world.do_right_turn(robot_name)[1])
                print(world.do_right_turn(robot_name)[1])
        elif world.current_direction_index == 3:
            if cell[1] > no_obstacle[-1][1]:
                print(world.do_left_turn(robot_name)[1])
            if cell[1] < no_obstacle[-1][1]:
                print(world.do_right_turn(robot_name)[1])
            if cell[0] < no_obstacle[-1][0]:
                print(world.do_right_turn(robot_name)[1])
                print(world.do_right_turn(robot_name)[1])
        print(world.do_forward(robot_name, 4, obstacles[0])[1])
    # return True, f'{robot_name}: I am at the top edge.'



def do_mazerun(robot_name, obstacles, command_arg):
    '''This function solves the mazerun using the mazerunner algorithm depending on which command_arg it should take.
    e.g:
    * If it is commanded to only mazerun, then the alternative route it will take will be the top route.
    * If it is commanded to take the bottom/top/left/right route it will follow the path given with the given directions as well.
    '''
    print(f'{robot_name}: starting maze run..')
    if command_arg == 'bottom':
        path = block.safe_path('news', command_arg, obstacles)
        do_maze_runner(robot_name, obstacles, path)
    elif command_arg == 'top' or command_arg == '':
        path = block.safe_path('swen', command_arg, obstacles)
        do_maze_runner(robot_name, obstacles, path)
        print(world.do_forward(robot_name, 4, obstacles[0])[1])
        command_arg = 'top'
    elif command_arg == 'left':
        path = block.safe_path('esnw', command_arg, obstacles)
        do_maze_runner(robot_name, obstacles, path)
    elif command_arg == 'right':
        path = block.safe_path('wnse', command_arg, obstacles)
        do_maze_runner(robot_name, obstacles, path)
        print(world.do_forward(robot_name, 4, obstacles[0])[1])
    return True, f'{robot_name}: I am at the {command_arg.lower()} edge.'


def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments, blocks):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name, blocks)
        if not silent:
            print(command_output)
            world.show_position(robot_name, world.position_x, world.position_y)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def call_command(command_name, command_arg, robot_name, blocks):
    '''Calls the command that the user inputed.
    '''
    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return world.do_forward(robot_name, int(command_arg), blocks[0])
    elif command_name == 'back':
        return world.do_back(robot_name, int(command_arg),blocks[0])
    elif command_name == 'right':
        return world.do_right_turn(robot_name)
    elif command_name == 'left':
        return world.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return do_sprint(robot_name, int(command_arg),blocks[0])
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg,blocks[0])
    elif command_name == 'mazerun':
        return do_mazerun(robot_name, blocks, command_arg)
    return False, None
    
    


def handle_command(robot_name, command, blocks):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name, blocks)

    print(command_output)
    world.show_position(robot_name, world.position_x, world.position_y)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)


def robot_start():
    """This is the entry point for starting my robot"""

    global history
    world.reset()
    
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    blocks = block.get_obstacles()
    obstacle_size = 4
    world.show_obstacles(blocks[0],robot_name, obstacle_size)
    
    history = []

    command = get_command(robot_name)
    while handle_command(robot_name, command,blocks):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")

if __name__ == "__main__":
    robot_start()
