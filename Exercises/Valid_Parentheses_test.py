from Valid_Parentheses import valid_parentheses

from unittest import TestCase


class Test(TestCase):
    def test_volume_case1(self):
        self.assertEqual(valid_parentheses("(()())"), True)
        self.assertEqual(valid_parentheses("(()()))))"), False)
        self.assertEqual(valid_parentheses("(((((((()"), False)
        self.assertEqual(valid_parentheses("((()))((()))"), True)
