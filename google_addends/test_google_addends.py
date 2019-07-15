from unittest import TestCase

from google_addends import adds_up_to


class Test(TestCase):

    def test_foo(self):
        for addends, target, outcome in [
            ([], 1, False),
            ([], 0, False),
            ([0, 0], 0, True),
            ([1], 1, False),
            ([1, 0], 1, True),
            ([10, 15, 3, 7], 17, True),
            ([3, 7, 10, 15, 20], 35, True),
            ([10, 15, 3, 7], 28, False),
        ]:
            with self.subTest(i=(addends, target)):
                self.assertEqual(outcome, adds_up_to(addends, target))
