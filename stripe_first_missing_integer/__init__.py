from typing import Optional, Sequence


def find_first_missing(ints: Sequence[int]) -> Optional[int]:
    """Find the lowest positive integer that does not exist in the array."""
    positive_ints = set(i for i in ints if i >= 0)
    return next((x for x in range(1, len(ints) + 1)
                 if x not in positive_ints), None)
