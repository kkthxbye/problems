from unittest import TestCase

from uber_product_except_itself import product_others


class Test(TestCase):

    def test_product(self):
        for input, expected in [
            ([], []),
            ([1], [1]),
            ([2], [1]),
            ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
            ([3, 2, 1], [2, 3, 6]),
        ]:
            with self.subTest(i=input):
                self.assertEqual(expected, product_others(input))
