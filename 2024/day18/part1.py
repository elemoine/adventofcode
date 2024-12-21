import sys

with open("input") as f_:
    byte_pos = [tuple(map(int, row.strip().split(","))) for row in f_]

num_bytes = 1024
max_ = 70

byte_positions = set(byte_pos[:num_bytes])

start = (0, 0)
exit_ = (max_, max_)

stack: list[tuple[int, int, int]] = [(start[0], start[1], 0)]

shortest = sys.maxsize
visited = {}

while stack:
    x, y, d = stack.pop()
    pos = (x, y)

    if pos == exit_:
        shortest = min(shortest, d)

    if pos in byte_positions:
        continue

    if pos[0] < 0 or pos[0] > max_ or pos[1] < 0 or pos[1] > max_:
        continue

    if pos in visited and d >= visited[pos]:
        continue

    visited[pos] = d

    for dir_ in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        next_ = (pos[0] + dir_[0], pos[1] + dir_[1], d + 1)
        stack.append(next_)


print(shortest)
