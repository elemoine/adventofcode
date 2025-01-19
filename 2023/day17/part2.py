from heapq import heappop, heappush

with open("input") as f_:
    map_ = [list(map(int, list(row.strip()))) for row in f_]


DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

maxy = len(map_) - 1
maxx = len(map_[0]) - 1


q = [(0, (0, 0), (0, 1), 0)]

seen = set()
ans = 1e9

while q:
    h, p, d, n = heappop(q)

    if (p, d, n) in seen:
        continue

    seen.add((p, d, n))

    if p == (maxy, maxx):
        ans = min(ans, h)

    if n < 4:
        p_ = (p[0] + d[0], p[1] + d[1])
        if p_[0] >= 0 and p_[0] <= maxy and p_[1] >= 0 and p_[1] <= maxx:
            h_ = h + map_[p_[0]][p_[1]]
            heappush(q, (h_, p_, d, n + 1))
    else:
        for d_ in DIRECTIONS:
            n_ = 1
            if d_ == d:
                if n == 10:
                    continue
                n_ = n + 1
            elif d_ == (-d[0], -d[1]):
                continue
            p_ = (p[0] + d_[0], p[1] + d_[1])
            if p_[0] < 0 or p_[0] > maxy or p_[1] < 0 or p_[1] > maxx:
                continue
            h_ = h + map_[p_[0]][p_[1]]
            heappush(q, (h_, p_, d_, n_))


print(ans)
