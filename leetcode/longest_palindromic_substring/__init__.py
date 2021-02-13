from typing import Optional, Tuple


def is_palindromic(s: str) -> bool:
    return s == s[::-1]


def expand(s: str, start: int, end: int) -> Tuple[int, int]:
    while start > 0 and end < len(s) and s[start - 1] == s[end]:
        start -= 1
        end += 1
    return start, end


def longest_palindromic_substring(s: str) -> Optional[str]:
    start, end = max(
        (expand(s, start, end)
         for start in range(len(s))
         for end in (start, start + 1)),
        key=lambda x: x[1] - x[0],
    )
    return s[start:end]
