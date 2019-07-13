from itertools import permutations
from typing import List
from math import floor

def num_ways(n: int) -> int:
    """
    n = 2:
        2
        1 1

    n = 4:
        2 2
        2 1 1 (1 1 2) (1 2 1)
        1 1 1 1

    n = 5:
        2 2 1
        2 1 1 1
        1 1 1 1 1
    """
    return sum(len(set(permutations(x))) for x in find_terms_combinations(n))

def find_terms_combinations(n: int) -> List[List[int]]:
    start = [2] * floor(n / 2) if n > 1 else []
    if n % 2:
        start.append(1)
    variants = find_terms(start)
    return variants

def find_terms(addends: List[int]) -> List[List[int]]:
    terms = [addends]
    if all(x == 1 for x in addends):
        return terms

    addends = addends.copy()
    addends.remove(2)
    addends.extend([1, 1])
    terms.extend(find_terms(addends))
    return terms


def test_num_ways():
    assert num_ways(1) == 1
    assert num_ways(2) == 2
    assert num_ways(3) == 3
    assert num_ways(4) == 5
    assert num_ways(5) == 8
    assert num_ways(6) == 13

test_num_ways()
