from os.path import dirname, join
from unittest import TestCase
from io import StringIO

from uber_voting import top


class TestUberVoting(TestCase):

    def test_two(self):
        self.assertEqual(['1', '2'], top(
            in_file=StringIO("""\
1,1
2,2
3,1
4,1
5,2
10,1"""),
            n=3,
        ))

    def test_votes_twice(self):
        with self.assertRaisesRegex(Exception, r'5'):
            top(in_file=StringIO("""\
1,1
2,2
5,1
5,2
"""))

