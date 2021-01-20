from logging import getLogger
from typing import FrozenSet, List

logger = getLogger(__name__)


def adds_up_to_n(options: List[int], target: int) -> FrozenSet[FrozenSet[int]]:
    """
    Find all unique triplets in the array sum of which is equal x.

    Notice that the solution set must not contain duplicate triplets.
    """
    addends = []
    logger.debug('%s', options)
    for i, v in enumerate(options[:-2]):
        left, right = i + 1, len(options) - 1
        local_target = target - v
        for _ in range(len(options) - i + 1):
            logger.debug('[%s]', ', '.join('?'.join(
                symbol for symbol, index in [('I', i), ('L', left), ('R', right)] if index == p
            ).rjust(len(str(options[p]))) or ' ' for p in range(len(options))))
            candidates = [options[left], options[right]]
            candidates_sum = sum(candidates)
            if candidates_sum == local_target:
                triplet = [v, *candidates]
                logger.debug('Adding %s', triplet)
                addends.append(frozenset(triplet))
                left += 1
                right -= 1
            if candidates_sum < local_target:
                left += 1
            if candidates_sum > local_target:
                right -= 1
            if left >= right:
                break
    return frozenset(addends)
