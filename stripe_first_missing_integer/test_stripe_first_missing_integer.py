from unittest import TestCase

from stripe_first_missing_integer import find_first_missing


class Test(TestCase):

    def test_first_missing(self):
        for input, expected in [
            ([3, 4, -1, 1], 2),
            ([], None),
            ([-1, -2, 0], 1),
            ([1, 2, 0], 3)
        ]:
            with self.subTest(i=input):
                self.assertEqual(expected, find_first_missing(input))