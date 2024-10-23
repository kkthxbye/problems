from itertools import groupby, takewhile
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    return ''.join(c for _, c in takewhile(
        lambda x: next(x[0], True) and not next(x[0], False),
        ((groupby(chars), chars[0]) for chars in zip(*strs))
    ))

print(longest_common_prefix(["flower", "flow", "flight"]))
