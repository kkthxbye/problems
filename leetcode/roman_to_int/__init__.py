from collections import Counter

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(s: str) -> int:
    result = 0
    prev_accum = None
    i = 0
    while i < len(s):
        value = romans.get(s[i])
        if prev_accum is not None:
            if value > prev_accum:
                result += value - prev_accum
                prev_accum = None
                i += 1
            elif value == prev_accum:
                prev_accum += value
            result += prev_accum
        else:
            prev_accum = value
        i += 1
    return result




print(romanToInt('MCMXCIV'))
