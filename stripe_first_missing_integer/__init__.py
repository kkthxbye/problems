from typing import Iterable, Optional, Sequence


def find_first_missing(ints: Sequence[int]) -> Optional[int]:
    """Find the lowest positive integer that does not exist in the array."""
    positive_ints = set(i for i in ints if i >= 0)
    return next((x for x in range(1, len(ints) + 1)
                 if x not in positive_ints), None)

def smallest_free(array: Iterable[int]) -> int:
    # Since we don't care about negatives at all.
    # Set allows for O(1) lookups. Frozenset skips the overhead coming from a mutable set.
    positives = frozenset(x for x in array if x > 0)
    # Get the first one:
    return next(filter(
        # Which is missing from positive numbers.
        lambda x: x not in positives,
        # While iterating from 1 to the largest number in positives.
        # Including a n + 1 case (e.g. [1, 2, 3]).
        range(1, (max(positives) if positives else 0) + 2),
    ))
