def lengthOfLongestSubstring(s: str) -> int:
    current = []
    longest = 0
    for c in s:
        if c not in current:
            current += c
            if len(current) > longest:
                longest = len(current)
        else:
            current = current[current.index(c) + 1:] + [c]
    return longest


# print(lengthOfLongestSubstring("aab"))
# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("aabaab!bb"))
