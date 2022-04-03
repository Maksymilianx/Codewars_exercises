import unittest

from Exercises.Barista_Problem import barista


class TestBaristaProblem(unittest.TestCase):
    def test_volume_case1(self):
        self.assertEqual(barista([2, 10, 5, 3, 9]), 85)

    def test_volume_case2(self):
        self.assertEqual(barista([4, 3, 2]), 22)

    def test_volume_case3(self):
        self.assertEqual(barista([20, 5]), 32)

    def test_volume_case4(self):
        self.assertEqual(barista([20, 5, 4, 3, 1, 5, 7, 8]), 211)

    def test_volume_case5(self):
        self.assertEqual(barista([5, 4, 3, 2, 1]), 55)
