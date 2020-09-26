# Given a string and a set of characters,
# return the shortest substring
# containing all the characters in the set.
# For example, given the string "figehaeci"
# and the set of characters {a, e, i}, you should return "aeci".


from unittest import TestCase

from square_substring_mask import shortest_contains_all


class Test(TestCase):

    def test_empty(self):
        self.assertIsNone(shortest_contains_all('abc', chars={'d'}))

    def test_present(self):
        self.assertEqual('aeci', shortest_contains_all('figehaeci', chars={'a', 'e', 'i'}))

    def test_shortest(self):
        self.assertEqual('aeci', shortest_contains_all('faegeihaeci', chars={'a', 'e', 'i'}))

    def test_shortest_shared(self):
        self.assertEqual('bac', shortest_contains_all('abcbac', chars={'a', 'b', 'c'}))

    def test_shortest_shared_right(self):
        self.assertEqual('cbda', shortest_contains_all('abcbda', chars={'a', 'b', 'c', 'd'}))
