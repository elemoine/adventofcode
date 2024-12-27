from collections import defaultdict

with open("input") as f_:
    pairs = [set(row.strip().split("-")) for row in f_]

adjacency_list = defaultdict(set)

for c1, c2 in pairs:
    adjacency_list[c1].add(c2)
    adjacency_list[c2].add(c1)


cnt = 0
seen = set()
for c1, c2 in pairs:
    n1 = adjacency_list[c1]
    n2 = adjacency_list[c2]
    for c in n1 & n2:
        k = tuple(sorted((c1, c2, c)))
        if k in seen:
            continue
        seen.add(k)
        cnt += any(c_.startswith("t") for c_ in (c1, c2, c))

print(cnt)
