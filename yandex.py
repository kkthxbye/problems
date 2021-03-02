from sys import stdin, stdout
from typing import List

# stdout.write(str(sum(int(x) for x in stdin.read().split(' '))))


["eat", "tea", "tan", "ate", "nat", "bat", "aab", "baa"]


[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]


def group(words):
    symbols_words_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in symbols_words_map:
            symbols_words_map[sorted_word] = []
        symbols_words_map[sorted_word].append(word)
    return symbols_words_map.values()


# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

# A4B3C2XYZD4E3F3A6B28

def pack(s, length):
    if length > 1:
        s += str(length)
    return s


def rle(s):
    if len(s) < 1:
        return ''
    current_length = 1
    result = ''
    current_char = s[0]
    for c in s[1:]:
        if c == current_char:
            current_length += 1
        else:
            result += pack(current_char, current_length)
            current_length = 1
            current_char = c
    result += pack(current_char, current_length)
    return result


# a = {
#    'b' : 4,
#    'c' : {
#        'd': 3,
#        'e': 5,
#     }
# }

# [
# ('b', 4),
# ('c.d', 3),
# ('c.e', 5),
# ]
# if not prefix:


def flatten(d, prefix=None):
    n = {}
    for key, value in d.items():
        flattened = '.'.join([prefix, key]) if prefix is not None else key
        if isinstance(value, dict):
            n.update(flatten(value, flattened))
        else:
            n[flattened] = value
    return n


flatten(d)


# key points:

# No communication in DMs. in fact represents a larger problem of lack of documentation.
# No long standups.

# Issue external (google, wiki, stackoverflow, blogs, papers) / internal (docs, chats)

def twoSum(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    sorted_numbers = sorted(nums)
    solution = None
    while left != right:
        candidates = [sorted_numbers[left], sorted_numbers[right]]
        candidate_sum = sum(candidates)
        if candidate_sum == target:
            solution = [index for index, x in enumerate(nums) if x in candidates]
            break
        if candidate_sum < target:
            left += 1
        if candidate_sum > target:
            right -= 1
    return solution


print(twoSum(nums=[3, 3], target=6))
