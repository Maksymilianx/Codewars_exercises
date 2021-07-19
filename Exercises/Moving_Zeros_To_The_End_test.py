import unittest

from Moving_Zeros_To_The_End import *


class TestMovingZerosToTheEnd(unittest.TestCase):
    def test_volume_case1(self):
        result = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
        self.assertListEqual(move_zeros(expected), result)

    def test_volume_case2(self):
        result = [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        expected = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
        self.assertListEqual(move_zeros(expected), result)

    def test_volume_case3(self):
        result = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
        self.assertListEqual(move_zeros(expected), result)
