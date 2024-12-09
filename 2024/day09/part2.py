from collections import defaultdict


def main():
    with open("input") as f_:
        map_ = list(map(int, list(f_.read().strip())))

    if len(map_) % 2 == 0:
        map_ = map_[:-1]

    file_id = len(map_) // 2
    right = len(map_) - 1

    records = defaultdict(list)

    while right >= 0:
        if right % 2 != 0:
            if map_[right]:
                records[right].append((map_[right], -1))
            right -= 1
            continue
        n_file_blocks = map_[right]
        left = 1
        while left < right:
            n_free_blocks = map_[left]
            if n_free_blocks >= n_file_blocks:
                map_[right] = 0
                map_[left] = n_free_blocks - n_file_blocks
                assert left % 2 != 0
                records[left].append((n_file_blocks, file_id))
                records[right].append((n_file_blocks, -1))
                break
            left += 2
        else:
            records[right].append((n_file_blocks, file_id))
        right -= 1
        file_id -= 1

    r, location = 0, 0
    for k in sorted(records.keys()):
        for n, file_id in records[k]:
            for _ in range(n):
                if file_id >= 0:
                    r += location * file_id
                location += 1
    print(r)


if __name__ == "__main__":
    main()
