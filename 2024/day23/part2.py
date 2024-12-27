# inspired by https://www.reddit.com/r/adventofcode/comments/1hkgj5b/comment/m3qfvak/

import itertools
from collections import Counter, defaultdict

with open("input") as f_:
    pairs = [set(row.strip().split("-")) for row in f_]

adjacency_list = defaultdict(set)


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


for c1, c2 in pairs:
    adjacency_list[c1].add(c2)
    adjacency_list[c2].add(c1)


r = [
    "".join(sorted(ps))
    for c, n in adjacency_list.items()
    for ps in powerset(set([c]) | n)
]

s = max((e for e, n in Counter(r).items() if n == len(e) // 2), key=len)

print(",".join(s[i : i + 2] for i in range(0, len(s), 2)))
