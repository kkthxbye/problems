from unittest import TestCase

from google_pairs import car, cdr, cons


class Test(TestCase):

    def test_pairs(self):
        self.assertEqual(3, car(cons(3, 4)))
        self.assertEqual(4, cdr(cons(3, 4)))
