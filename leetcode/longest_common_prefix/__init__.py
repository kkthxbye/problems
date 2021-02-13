from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    result = []
    for c in zip(*strings):
        if len(frozenset(c)) == 1:
            result.append(c[0])
        else:
            break
    return ''.join(result)


print(longest_common_prefix(["flower", "flow", "flight"]))
