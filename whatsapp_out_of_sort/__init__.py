from typing import Iterable, Tuple, Optional
from collections import namedtuple

Item = namedtuple('Item', ['index', 'value'])


def find_foo(iterable: Iterable) -> Tuple[Optional[int], Optional[int]]:
    """
    Given an array of integers out of order,
    determine the bounds of the smallest window that must be sorted
    in order for the entire array to be sorted.
    For example, given [3, 7, 5, 6, 9], you should return (1, 3).
    """
    start, end = None, None
    indexed = list(map(lambda x: Item(*x), enumerate(iterable)))
    for prev, following in zip(indexed, indexed[1:]):
        if start is None and prev.value > following.value:
            start = prev.index
        if start is not None and following.value > iterable[start]:
            end = prev.index
    return (start, end)
