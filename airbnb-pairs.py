from unittest import TestCase
from typing import List, Tuple, Iterable, Callable
from itertools import product, combinations
from operator import add


def find_all_pairs(iter: Iterable[int],
                   target: int,
                   op: Callable = add) -> List[Tuple[int, int]]:
    return [(x, y) for x, y
            in combinations(unique_list(iter), 2)
            if op(x, y) == target]


def unique_list(iter: Iterable) -> List:
    seen: List = []
    for i in iter:
        if i not in seen:
            seen.append(i)
    return seen


class TestAirbnb(TestCase):
    def test_find_all_pairs(self):
        for iterable, target, expected in [
            ([1, 3, 2, 3, 2, 5, 46, 6, 7, 4], 5, [(1, 4), (3, 2)]),
            ([1, 3, 4, 2], 2, []),
            ([2, 3, 3], 5, [(2, 3)])
        ]:
            self.assertEqual(expected, find_all_pairs(iterable, target))


TestAirbnb().test_find_all_pairs()
