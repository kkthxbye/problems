from unittest import TestCase

from google_r_g_b import sort_r_g_b

class Test(TestCase):

    def test_foo(self):
        self.assertEqual(
            ['R', 'R', 'R', 'G', 'G', 'B', 'B'],
            sort_r_g_b(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
        )
