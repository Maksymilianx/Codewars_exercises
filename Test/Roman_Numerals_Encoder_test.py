from unittest import TestCase

from Exercises.Roman_Numerals_Encoder import *


class Test(TestCase):
    def test_numerals_case1(self):
        self.assertEqual(solution(2021), "MMXXI")

    def test_numerals_case2(self):
        self.assertEqual(solution(1), "I")

    def test_numerals_case3(self):
        self.assertEqual(solution(0), "")
