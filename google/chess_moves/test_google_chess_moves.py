from typing import FrozenSet, List, Optional
from itertools import product, permutations, chain
from unittest import TestCase, main

layout: List[List[Optional[int]]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None],
]


def possibilities(num: int) -> FrozenSet[int]:
    coordinates = next(
        (
            (x, y)
            for y, row in enumerate(layout)
            for x, value in enumerate(row)
            if value == num
        ),
        None,
    )
    if coordinates is None:
        return frozenset()
    start_x, start_y = coordinates
    return frozenset(
        value
        for x, y in (
            (start_x + x, start_y + y)
            for x, y in chain.from_iterable(
                (product(*x)) for x in permutations([[-2, 2], [-1, 1]], 2)
            )
        )
        if all(
            (
                0 <= y < len(layout),
                0 <= x < len(layout[0]),
            )
        )
        and (value := layout[y][x]) is not None
    )


class Test(TestCase):

    def test_possibilities(self):
        self.assertEqual({6, 8}, possibilities(1))
        self.assertEqual(frozenset(), possibilities(5))
        self.assertEqual({0, 3, 9}, possibilities(4))
        self.assertEqual({1, 3}, possibilities(8))


if __name__ == "__main__":
    main()
