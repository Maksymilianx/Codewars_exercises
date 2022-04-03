import unittest

from Exercises.Multiples_of_3_or_5 import *


class TestMultiplesOf3Or5(unittest.TestCase):
    def test_volume_case1(self):
        self.assertEqual(solution(10), 23)

    def test_volume_case2(self):
        self.assertEqual(another_solution(10), 23)
