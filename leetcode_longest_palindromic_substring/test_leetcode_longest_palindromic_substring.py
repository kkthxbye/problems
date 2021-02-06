from unittest import TestCase

from leetcode_longest_palindromic_substring import longest_palindromic_substring


class Test(TestCase):

    def test_base(self):
        self.assertEqual('bab', longest_palindromic_substring('babad'))

    def test_middle(self):
        self.assertEqual('bb', longest_palindromic_substring('cbbd'))

    def test_single_char(self):
        self.assertEqual('a', longest_palindromic_substring('a'))

    def test_start(self):
        self.assertEqual('a', longest_palindromic_substring('ac'))
