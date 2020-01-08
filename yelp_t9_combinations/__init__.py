# %%
from unittest import TestCase
import itertools
from itertools import product

a = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}
list(''.join(x) for x in product(*(a.get(x, []) for x in "23")))
# %%


# input
phone = '23'
mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f']
}

output = ''.join(itertools.chain(*[mapping[key] for key in phone]))
print(output)

# %%


def merge(intervals):
    print(list(
        ((low, high), list(zip(*(
            (l, h) for l, h in intervals
            if high != h and low != l and min((high, h)) - max((low, l)) > 0
        )))) for low, high in intervals
    ))

    return [(
        min([current_low] + candidates_low),
        max([current_high] + candidates_high)
    ) for (current_low, current_high), (candidates_low, candidates_high) in (
        ((low, high), list(zip(*(
            (l, h) for l, h in intervals
            if high != h and low != l and min((high, h)) - max((low, l)) > 0
        ))) or ([], [])) for low, high in intervals
    )]

    # new_intervals = []
    # for i in intervals:
    #     low, high = i
    #     candidates = [(l, h) for l, h in intervals
    #                   if low <= l <= high or low <= h <= high
    #                   or l <= low <= h or l <= high <= h]
    #     new_interval = (
    #         min([low] + [l for l, _ in candidates]),
    #         max([high] + [h for _, h in candidates]),
    #     )
    #     print(new_interval)
    #     new_intervals.append(new_interval)
    # return new_intervals


class MergeTest(TestCase):

    def test(self):
        self.assertEqual(
            [(1, 3), (4, 10), (20, 25)],
            merge([(1, 3), (5, 8), (4, 10), (20, 25)])
        )
