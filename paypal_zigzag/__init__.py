from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple
# P     I     N
# A   L S   I G
# Y A   H R
# P     I


t = [(6, 6), (4, 2), (2, 4), (6, 6)]

# P   A   H   N
# A P L S I I G
# Y   I   R
# t = [4, 2, 4]


def alternating_step(s: Iterable, step: Tuple[int, int]) -> Iterable:
    result = ''
    step_index = 0
    i = 0
    while i <= len(s) - 1:
        result += s[i]
        i += step[step_index]
        step_index = 1 if step_index == 0 else 0
    return result

# print(alternating_step([str(i) for i in range(10)], step=[1, 5]))


def zigzag(s: str, columns: int) -> str:
    return ''.join(alternating_step(s[start:], step=subt) for start, subt in enumerate(t))
    # for x in range(columns):

    # rows = tuple([] for _ in range(columns))
    # row_index, c = 0, 0
    # offset = 1
    # while c <= len(s) - 1:
    #     rows[row_index].append(s[c])
    #     if len(rows) > 1:
    #         if row_index == 0:
    #             offset = 1
    #         elif row_index == columns - 1:
    #             offset = -1
    #         row_index += offset
    #     c += 1
    # return ''.join(''.join(r) for r in rows)


# assert 'PAHNAPLSIIGYIR' == zigzag('PAYPALISHIRING', 3)
# assert 'PINALSIGYAHRPI' == zigzag('PAYPALISHIRING', 4)
# assert 'AB' == zigzag('AB', 1)
