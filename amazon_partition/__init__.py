from typing import List, Callable, Iterable, Tuple
from operator import eq, gt, lt
from functools import partial

from itertools import tee, chain


def partition_multiple(predicates: List[Callable[..., bool]],
                       iterable: Iterable) -> Tuple[Iterable, ...]:
    """
    Partition items into n iterables with each one
    only having items true to the corresponding condition.

    partition_multiple([
        lambda x: x > 6,
        lambda x: x < 4
    ], range(10)) --> 7 8 9   and  0 1 2 3
    """
    return tuple(filter(predicate, t) for predicate, t
                 in zip(predicates, tee(iterable, len(predicates))))


def sort_partitions(x: Iterable[int], n: int) -> List[int]:
    return list(chain(*partition_multiple(predicates=[
        partial(f, n) for f in [gt, eq, lt]
    ], iterable=x)))
