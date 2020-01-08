from itertools import accumulate
from operator import mul
from typing import Sequence


def product_others(items: Sequence[int]) -> Sequence[int]:
    """
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in
    the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5],
    the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1],
    the expected output would be [2, 3, 6].
    """
    ltr, rtl = tuple(list(accumulate(x, mul))
                     for x in (items, reversed(items)))
    return [
        (ltr[i - 1] if i >= 1 else 1)
        * (rtl[-i - 2] if i < len(items) - 1 else 1)
        for i in range(len(items))
    ]
