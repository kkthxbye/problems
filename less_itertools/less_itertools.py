from itertools import tee
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')


def is_empty(iterable: Iterable):
    """
    Check if iterable is empty without consuming.

    >>> is_empty(x for x in range(0))[0]
    True

    >>> gen = (x for x in range(1))
    >>> empty, unconsumed_gen = is_empty(gen)
    >>> empty
    False
    >>> next(unconsumed_gen)
    0
    """
    it1, it2 = tee(iterable)
    try:
        next(it1)
        return False, it2
    except StopIteration:
        return True, it2


def vectorize(item: T, predicates: Iterable[Callable[[T], bool]]):
    """
    Map an item into a tuple where first true predicate holds an item.

    Short-curcuits, e.g.:
    >>> x = vectorize(6, [
    ...     lambda x: x % 4 == 0,
    ...     lambda x: x % 3 == 0,
    ...     lambda x: x % 2 == 0,
    ... ])
    (None, 6, None)
    """
    valid = next((i for i, p in enumerate(predicates) if p(item)), None)
    return tuple(item if i == valid else None for i, _ in enumerate(predicates))


def n_predicate_partition(predicates: Iterable[Callable[[T], bool]], iterable: Iterable[T]):
    """
    Partition an Iterable into a tuple of len(predicate) sub-iterables
    whose values correspond to a specific predicate.

    Short-circuited, meaning the order of predicates matters, e.g.:
    >>> for x in n_predicate_partition([
    ...     lambda x: x % 4 == 0,
    ...     lambda x: x % 2 == 0,
    ... ], range(10)):
    ... print(list(x))
    [0, 4, 8]
    [2, 6]

    >>> for x in n_predicate_partition([
    ...     lambda x: x % 2 == 0,
    ...     lambda x: x % 4 == 0,
    ... ], range(10)):
    ... print(list(x))
    [0, 2, 4, 6, 8]
    []
    """
    empty, iterable = is_empty(iterable)
    if empty:
        return tuple([] for _ in predicates)

    return (
        (x for x in chain if x is not None)
        for chain in zip(
            *(vectorize(item, predicates) for item, predicates in ((x, tuple(p for p in predicates)) for x in iterable))
        )
    )


def partition(predicate: Callable[[T], bool], iterable: Iterable[T]):
    """
    Partition an iterable into a tuple of iterables of "True" / "False" for a given predicate.

    >>> for x in partition(lambda x: x % 2 == 0, range(10)):
    ...     print(list(x))
    [0, 2, 4, 6, 8]
    [1, 3, 5, 7, 9]
    """
    return n_predicate_partition([predicate, lambda _: True], iterable)
