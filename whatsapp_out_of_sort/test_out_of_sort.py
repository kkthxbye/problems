from unittest import TestCase

from whatsapp_out_of_sort import find_foo


class Test(TestCase):

    def test_provided(self):
        self.assertEqual((1, 3), find_foo([3, 7, 5, 6, 9]))

    def test_sorted(self):
        self.assertEqual((None, None), find_foo([3, 5, 6, 7, 9]))

    def test_split(self):
        self.assertEqual((0, 4), find_foo([5, 3, 6, 8, 7, 9]))
