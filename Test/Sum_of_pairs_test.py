from unittest import TestCase

from Exercises.Sum_of_pairs import *


class Test(TestCase):
    def test_volume_case1(self):
        self.assertListEqual(sum_pairs([1, 2, 3, 4, 5, 6], 6), [2, 4])
        self.assertListEqual(sum_pairs([1, 2, 3, 4, 5, 6], 4), [1, 3])
        self.assertListEqual(sum_pairs([1, 2, 3, 4, 5, 6], 5), [2, 3])
        self.assertListEqual(sum_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 7), [3, 4])
