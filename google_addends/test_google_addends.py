from unittest import TestCase

from google_addends import adds_up_to


class Test(TestCase):

    def test_foo(self):
        self.assertFalse(adds_up_to([], 1))
        self.assertFalse(adds_up_to([], 0))
        self.assertTrue(adds_up_to([0, 0], 0))
        self.assertFalse(adds_up_to([1], 1))
        self.assertTrue(adds_up_to([1, 0], 1))
        self.assertTrue(adds_up_to([10, 15, 3, 7], 17))
        self.assertTrue(adds_up_to([3, 7, 10, 15, 20], 35))
        self.assertFalse(adds_up_to([10, 15, 3, 7], 28))
