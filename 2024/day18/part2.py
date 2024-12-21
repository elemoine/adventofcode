with open("input") as f_:
    byte_positions = [tuple(map(int, row.strip().split(","))) for row in f_]

start_byte = 2000  # Found by dichotomy
max_ = 70

start = (0, 0)
exit_ = (max_, max_)

for byte_ in range(start_byte, len(byte_positions)):
    bytes_ = set(byte_positions[:byte_ + 1])

    stack: list[tuple[int, int, int]] = [(start[0], start[1], 0)]
    visited = {}

    while stack:
        x, y, d = stack.pop()
        pos = (x, y)

        if pos == exit_:
            break

        if pos in bytes_:
            continue

        if pos[0] < 0 or pos[0] > max_ or pos[1] < 0 or pos[1] > max_:
            continue

        if pos in visited and d >= visited[pos]:
            continue

        visited[pos] = d

        for dir_ in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            next_ = (pos[0] + dir_[0], pos[1] + dir_[1], d + 1)
            stack.append(next_)
    else:
        print("Got it!", byte_positions[byte_])
        break
