import unittest

from Exercises.Next_bigger_number_with_the_same_digits import *


class NextBigger(unittest.TestCase):
    def test_volume_case1(self):
        self.assertEqual(next_bigger(12), 21)

    def test_volume_case2(self):
        self.assertEqual(next_bigger(21), -1)

    def test_volume_case3(self):
        self.assertEqual(next_bigger(11), -1)

    def test_volume_case4(self):
        self.assertEqual(next_bigger(0), -1)

    def test_volume_case5(self):
        self.assertEqual(next_bigger(1234), 1243)
