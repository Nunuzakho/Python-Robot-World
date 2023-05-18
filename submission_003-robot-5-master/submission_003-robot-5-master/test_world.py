import unittest
from maze import obstacles
# from maze import maze_it_up

from world.text.world import *


class TestCases(unittest.TestCase):

    def test_is_position_allowed(self):
        min_y, max_y = -200, 200
        min_x, max_x = -100, 100
        self.assertEqual(min_y, -200)
        self.assertEqual(max_y, 200)
        self.assertEqual(min_x, -100)
        self.assertEqual(max_x, 100)


    def test_do_forward(self):
        # reset()
        obstacles.random.randint = lambda x,a : 0

        output = do_forward("Hal", 10, [(0,12)])
        self.assertEqual((True, " > Hal moved forward by 10 steps."), output)


        output = do_forward("Hal", 10, [(0,10)])
        self.assertEqual((True, "Hal: Sorry, there is an obstacle in the way."), output)


        output = do_forward("Hal", 201, [(10,0)])
        self.assertEqual((True, "Hal: Sorry, I cannot go outside my safe zone."), output)


        reset()


    def test_do_back(self):
        reset()
        obstacles.random.randint = lambda x,a : 0
        
        output = do_back("Hal", -10, [(0,10)])
        self.assertEqual((True, " > Hal moved back by -10 steps."), output)

        output = do_back("Hal", -10, [(0,10)])
        self.assertEqual((True, 'Hal: Sorry, there is an obstacle in the way.'), output)

        output = do_back("Hal", -201, [(0,10)])
        self.assertEqual((True, "Hal: Sorry, I cannot go outside my safe zone."), output)
        reset()
    

    def test_do_right_turn(self):
        test_degress = do_right_turn("HAL")
        self.assertEqual((test_degress), (True, " > HAL turned right."))

    

    def test_do_left_turn(self):
        test_degress = do_left_turn("HAL")
        self.assertEqual((test_degress), (True, " > HAL turned left."))


if __name__ == '__main__':
    unittest.main()