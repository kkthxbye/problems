from typing import List, Tuple, Optional, Set
from itertools import combinations, product, permutations, chain
from unittest import TestCase, main

layout: List[List[Optional[int]]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None],
]


def possibilities(num: int) -> Set[int]:
    moves_offsets = chain(*[list(product(*x))
                            for x in permutations([[-2, 2], [-1, 1]], 2)])
    start_x, start_y = find_pos(num)
    targets = ((start_x + x, start_y + y) for x, y in moves_offsets)
    valid = [(x, y) for x, y in targets if all((
        0 <= x < len(layout),
        0 <= y < len(layout[x]),
    )) and layout[x][y] is not None]

    return set(layout[x][y] for x, y in valid)


def find_pos(num: int) -> Optional[Tuple[int, int]]:
    for x, row in enumerate(layout):
        for y, value in enumerate(row):
            if value == num:
                return (x, y)
    return None


class Test(TestCase):

    def test_possibilities(self):
        self.assertEqual({6, 8}, possibilities(1))
        self.assertEqual(set(), possibilities(5))
        self.assertEqual(set(), possibilities(4))

if __name__ == '__main__':
    main()
