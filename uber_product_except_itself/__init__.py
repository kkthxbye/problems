from typing import Sequence
from functools import reduce

def product_except_inself(items: Sequence[int]) -> Sequence[int]:
    """
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in
    the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5],
    the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1],
    the expected output would be [2, 3, 6].
    """
    return [reduce(
        lambda x, y: x * y,
        (x for j, x in enumerate(items) if j != i),
        1
    ) for i in range(len(items))]