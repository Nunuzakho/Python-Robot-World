import unittest
from maze import obstacles

class TestCases(unittest.TestCase):

    def test_is_position_blocked(self):
        self.assertEqual(True, obstacles.is_position_blocked(1,1,[(1,1)]))
        self.assertEqual(True, obstacles.is_position_blocked(2,2,[(1,1)]))
        self.assertEqual(True, obstacles.is_position_blocked(3,3,[(1,1)]))
        self.assertEqual(True, obstacles.is_position_blocked(4,4,[(1,1)]))
        self.assertEqual(False, obstacles.is_position_blocked(5,5,[(1,1)]))
        self.assertEqual(False, obstacles.is_position_blocked(6,6,[(1,1)]))

    def test_is_path_blocked(self):
        self.assertEqual(True, obstacles.is_position_blocked(10, 10,[(10,10)]))
        self.assertEqual(True, obstacles.is_position_blocked(20, 20,[(20,20)]))
        self.assertEqual(True, obstacles.is_position_blocked(200, 50,[(200,50)]))
        
        


if __name__ == '__main__':
    unittest.main()