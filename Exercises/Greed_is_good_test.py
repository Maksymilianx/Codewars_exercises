import unittest

from Exercises.Greed_is_good import score


class TestGreedIsGood(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(score([1,1,1,1,5]),1150)
        self.assertEqual(score([1,5,1,5,1]),1100)
        self.assertEqual(score([5,5,5,2,2]),500)
        self.assertEqual(score([5,5,5,1,1]),700)
        self.assertEqual(score([2,2,2,1,1]),400)
        self.assertEqual(score([2,2,2,2,2]),200)
        self.assertEqual(score([2,5,2,4,2]),250)
        self.assertEqual(score([1,1,2,2,2]),400)
        self.assertEqual(score([3,3,3,5,5]),400)
        self.assertEqual(score([6,1,6,1,6]),800)
        self.assertEqual(score([2,2,4,4,4]),400)
        self.assertEqual(score([1,1,1,1,1]),1200)

    def test_input_value(self):
        self.assertRaises(TypeError, score, list)
        self.assertRaises(TypeError, score, int)
        self.assertRaises(TypeError, score, str)
