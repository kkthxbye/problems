from unittest import TestCase

from uber_product_except_itself import product_others


class Test(TestCase):

    def test_product(self):
        self.assertFalse(product_others([]))
        self.assertEqual([1], product_others([1]))
        self.assertEqual([1], product_others([2]))
        self.assertEqual([120, 60, 40, 30, 24], product_others([1, 2, 3, 4, 5]))
        self.assertEqual([2, 3, 6], product_others([3, 2, 1]))
