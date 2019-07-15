from unittest import TestCase

from uber_product_except_itself import product_except_inself


class Test(TestCase):

    def test_product(self):
        self.assertFalse(product_except_inself([]))
        self.assertEqual([1], product_except_inself([1]))
        self.assertEqual([1], product_except_inself([2]))
        self.assertEqual([120, 60, 40, 30, 24], product_except_inself([1, 2, 3, 4, 5]))
        self.assertEqual([2, 3, 6], product_except_inself([3, 2, 1]))
