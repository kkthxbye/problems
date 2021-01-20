from typing import List


def adds_up_to(addends: List, target: int) -> bool:
    """
    Given a list of numbers and a number k,
    return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17,
    return true since 10 + 7 is 17.
    """
    if not addends or len(addends) <= 1:
        return False

    possible = sorted([a for a in addends if a <= target])
    left, right = iter(possible), iter(reversed(possible))
    low, high = next(left), next(right)
    for _ in range(len(possible)):
        result = low + high
        if result == target:
            return True
        if result < target:
            low = next(left)
        if result > target:
            high = next(right)

    return False



