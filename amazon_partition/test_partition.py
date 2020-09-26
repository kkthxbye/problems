# Given a pivot x, and a list lst, partition the list into three parts.
# •	The first part contains all elements in lst that are less than x
# •	The second part contains all elements in lst that are equal to x
# •	The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10],
# one partition may be [9, 3, 5, 10, 10, 12, 14].


from unittest import TestCase

from amazon_partition import sort_partitions


class Test(TestCase):

    def test_empty(self):
        self.assertEqual([], sort_partitions(x=[], n=1))

    def test_provided(self):
        self.assertEqual(
            [9, 3, 5, 10, 10, 12, 14],
            sort_partitions(x=[9, 12, 3, 5, 14, 10, 10], n=10)
        )
