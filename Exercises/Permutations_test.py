from unittest import TestCase

from Exercises.Permutations import permutations


class Test(TestCase):
    def test_permutations1(self):
        expected = 'a'
        result = ['a']
        self.assertListEqual(permutations(expected), result)

    def test_permutations2(self):
        expected = 'ab'
        result = ['ab', 'ba']
        self.assertListEqual(permutations(expected), result)

    def test_permutations3(self):
        expected = 'aabb'
        result = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        self.assertListEqual(permutations(expected), result)