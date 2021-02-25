from typing import List


def findLongestWord(s: str, d: List[str]) -> str:
    longest = ''
    for word in sorted(d, key=lambda x: (len(x), x), reverse=True):
        if len(word) < len(longest):
            break
        i = 0
        word_offset = 0
        while i + len(word) - word_offset - 1 < len(s) and word_offset < len(word):
            if s.find(word[word_offset], i + 1):
            # if s[i] == word[word_offset]:
                word_offset += 1
            i += 1
        if word_offset == len(word):
            longest = word
    return longest


# print(findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
# print(findLongestWord("abpcplea", ["a", "b", "c"]))
# print(findLongestWord("abce", ["abe", "abc"]))
# print(findLongestWord("aewfafwafjlwajflwajflwafj", ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]))
print(findLongestWord("aaa", ["aaa", "aa", "a"]))
