from typing import FrozenSet, List, Tuple, Optional, Set
from itertools import combinations, product, permutations, chain
from unittest import TestCase, main

layout: List[List[Optional[int]]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None],
]


def find_pos(num: int) -> Optional[Tuple[int, int]]:
    return next(
        (
            (x, y)
            for y, row in enumerate(layout)
            for x, value in enumerate(row)
            if value == num
        ),
        None,
    )


def possibilities(num: int) -> FrozenSet[int]:
    moves_offsets = chain(
        *[list(product(*x)) for x in permutations([[-2, 2], [-1, 1]], 2)]
    )
    if not (coordinates := find_pos(num)):
        return frozenset()
    start_x, start_y = coordinates
    return frozenset(
        value
        for x, y in ((start_x + x, start_y + y) for x, y in moves_offsets)
        if all(
            (
                0 <= y < len(layout),
                0 <= x < len(layout[y]),
            )
        )
        and (value := layout[y][x]) is not None
    )


class Test(TestCase):

    def test_possibilities(self):
        self.assertEqual({6, 8}, possibilities(1))
        self.assertEqual(set(), possibilities(5))
        self.assertEqual({0, 3, 9}, possibilities(4))


if __name__ == "__main__":
    main()
