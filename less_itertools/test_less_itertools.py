import pytest
from less_itertools.less_itertools import vectorize, n_predicate_partition, partition


@pytest.mark.parametrize(
    "item, predicates, expected",
    [
        (5, [lambda x: x < 0, lambda x: x == 5, lambda x: x > 10], (None, 5, None)),
        (4, [lambda x: x % 2 == 0, lambda x: True], (4, None)),
        (42, [lambda x: x < 0, lambda x: x > 100], (None, None)),
        (42, [], ()),
    ],
)
def test_vectorize(item, predicates, expected):
    assert vectorize(item, predicates) == expected


@pytest.mark.parametrize(
    "predicates, iterable, expected",
    [
        ([lambda x: x % 4 == 0, lambda x: x % 2 == 0], range(10), ([0, 4, 8], [2, 6])),
        ([lambda x: x % 2 == 0, lambda x: x % 4 == 0], range(10), ([0, 2, 4, 6, 8], [])),
        ([lambda x: True, lambda x: True], (x for x in range(3)), ([0, 1, 2], [])),
        ([lambda x: x > 0, lambda x: x < 0], [], ([], [])),
    ],
)
def test_n_predicate_partition(predicates, iterable, expected):
    result = tuple(map(list, n_predicate_partition(predicates, iterable)))
    assert result == expected


@pytest.mark.parametrize(
    "predicate,iterable,expected",
    [
        (lambda x: x % 2 == 0, range(10), ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])),
        (lambda x: True, [1, 2, 3], ([1, 2, 3], [])),
        (lambda x: False, [1, 2, 3], ([], [1, 2, 3])),
    ],
)
def test_partition(predicate, iterable, expected):
    result = tuple(map(list, partition(predicate, iterable)))
    assert result == expected
