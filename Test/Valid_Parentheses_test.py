from unittest import TestCase

from Exercises.Valid_Parentheses import valid_parentheses


class Test(TestCase):
    def test_volume_case1(self):
        self.assertEqual(valid_parentheses("(()())"), True)
        self.assertEqual(valid_parentheses("(()()))))"), False)
        self.assertEqual(valid_parentheses("(((((((()"), False)
        self.assertEqual(valid_parentheses("((()))((()))"), True)
