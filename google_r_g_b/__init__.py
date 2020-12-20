from typing import Sequence


def sort_r_g_b(a: Sequence[str]) -> Sequence[str]:
    r_offset = 0
    i = 0
    g_offset = len(a) - 1
    while i < g_offset + 1:
        if a[i] == 'R':
            a[i], a[r_offset] = a[r_offset], a[i]
            r_offset += 1
        elif a[i] == 'B':
            a[i], a[g_offset] = a[g_offset], a[i]
            g_offset -= 1
        elif a[i] == 'G':
            i += 1
    return a
