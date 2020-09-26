from typing import Optional, Set

from collections import defaultdict
from itertools import chain


def shortest_contains_all(s: str, chars: Set[str]) -> Optional[str]:
    seen = defaultdict(list)
    for i, c in enumerate(s):
        if c in chars:
            seen[c].append(i)
            choices_available = dict(filter(
                lambda x: len(x[1]) > 1, seen.items()
            ))
            if choices_available:
                for choice_char, choice_indices in choices_available.items():
                    outermost = choice_indices[0]
                    global_lbound = min(x for x in chain(*(x for x in seen.values()))
                                        if x != outermost)
                    if i - global_lbound < i - outermost:
                        seen[choice_char] = [next(iter(x for x in choice_indices if x >= global_lbound))]

    if len(seen) != len(chars):
        return None

    return s[min(chain(*seen.values())):max(chain(*seen.values())) + 1]
