import unittest
import robot
from io import StringIO
from unittest.mock import patch
import sys


class TestCases(unittest.TestCase):

    sys.stdout = StringIO()
    @patch("sys.stdin", StringIO("Hal\n"))
    def test_get_robot_name(self):
        robot_name = robot.get_robot_name()
        self.assertEqual(robot_name, "Hal")

    @patch("sys.stdin", StringIO("OFF\nHelp\nReplay\nopen\n"))
    def test_get_command(self):
        # global history
        self.assertEqual(robot.get_command("Hal"),"off")
        self.assertEqual(robot.get_command("Hal"),"help")
        self.assertEqual(robot.get_command("Hal"),"replay")

    def test_split_command_input(self):
        split_command = robot.split_command_input("off")
        self.assertEqual(split_command,('off', ''))
        split_command = robot.split_command_input("forward 2")
        self.assertEqual(split_command, ('forward',"2"))
        split_command = robot.split_command_input("forward")
        self.assertEqual(split_command, ('forward', ''))
        split_command = robot.split_command_input('replay reverse silent')
        self.assertEqual(split_command, ('replay', 'reverse silent'))

    def test_int_value(self):
        value = robot.is_int("3")
        self.assertEqual(value, True)
        value = robot.is_int("'")
        self.assertEqual(value, False)
        value = robot.is_int("silent")
        self.assertEqual(value, False)
    
    # def test_do_replay(self):
    #     command_output = robot.do_replay("Hal", ['sprint 10', 'forward 10', 'replay', 'replay reversed', 'replay reversed silent'], 'reversed', 'silent', '2', '')
    #     self.assertEqual(command_output,(True, " > Hal replayed 2 commands in reverse silently."))
    #     self.assertEqual(command_output,(True, " > Hal replayed 2 commands in reverse silently."))
    #     self.assertEqual(command_output,(True, " > Hal replayed 2 commands in reverse silently."))
    #     self.assertEqual(command_output,(True, " > Hal replayed 2 commands in reverse silently."))



    def test_do_help(self):
        help_output = robot.do_help()
        self.assertEqual(help_output, (True, """I can understand these commands:
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
"""))


if __name__ == '__main__':
    unittest.main()