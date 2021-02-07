from typing import List

def shortest_to_char(s: str, c: str) -> List[int]:
    targets = [index for index, value in enumerate(s) if value == c]
    distances = []
    previous = None
    for target in targets:
        if previous is None:
            distances.extend(reversed(range(target + 1)))
            previous = target
        else:
            length = target - previous
            print(f'{length=}')
            left_filler = range(1, length // 2 + 1)
            right_filler = range(length - len(left_filler) - 1, -1, -1)
            print(f'{list(left_filler)=}, {list(right_filler)=}')
            distances.extend(sum((list(x) for x in [
                left_filler,
                right_filler,
            ]), []))
            previous = target
    distances.extend(range(1, len(s) - len(distances) + 1))
    return distances

# [3,2,1,0,1,0,0,1,2,2,1,0]
# print(shortest_to_char('loveleetcode', 'e'))
