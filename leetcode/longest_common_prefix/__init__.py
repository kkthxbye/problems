from itertools import groupby
from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    result = []
    for c in zip(*strings):
        unique = groupby(c)
        if next(unique, True) and not next(unique, False):
            result.append(c[0])
        else:
            break
    return ''.join(result)


print(longest_common_prefix(["flower", "flow", "flight"]))
