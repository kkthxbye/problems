from typing import List


def find_substring(s: str, words: List[str]) -> List[int]:
    words_indices = {}
    words_offsets = {word: 0 for word in words}
    for index, char in enumerate(s):
        for word in words:
            word_offset = words_offsets[word]
            if word[word_offset] == char:
                if len(word) == word_offset + 1:
                    words_offsets[word] = 0
                    words_indices[index - len(word) + 1] = word
                else:
                    words_offsets[word] += 1
            else:
                words_offsets[word] = 0
    to_be_exhausted = set(words)
    indices = []
    last_index = 0
    print(f'{words_indices=}')
    for index, word in words_indices.items():
        print(f'{word=}')
        print(f'{to_be_exhausted=}')
        if word in to_be_exhausted and index == last_index + len(word):
            to_be_exhausted.remove(word)
            if not to_be_exhausted:
                indices.append(index - (len(words) - 1) * len(word))
                to_be_exhausted = set(w for w in words if w != word)
        else:
            to_be_exhausted = set(w for w in words if w != word)
        last_index = index
        print(f'{last_index=}')
        print('')

    return indices

# ""
# ["bar","foo","the"]
print(find_substring('barfoofoobarthefoobarman', words=['foo', 'bar', 'the']))
