def main():
    with open("input") as f_:
        map_ = list(map(int, list(f_.read().strip())))

    if len(map_) % 2 == 0:
        map_ = map_[:-1]
    last_id = len(map_) // 2

    left, right = 0, len(map_) - 1
    file_id, position = 0, 0
    result = 0

    while left <= right:
        if left % 2 != 0:
            # we have free blocks, so we can move
            # file blocks
            assert right % 2 == 0

            n_free_blocks = map_[left]
            n_file_blocks = map_[right]

            if n_free_blocks >= n_file_blocks:
                # enough free blocks
                for _ in range(n_file_blocks):
                    result += last_id * position
                    position += 1
                map_[right] = 0
                map_[left] = n_free_blocks - n_file_blocks
                if map_[left] == 0:
                    left += 1
                right -= 2
                last_id -= 1
            else:
                # not enough free blocks
                for _ in range(n_free_blocks):
                    result += last_id * position
                    position += 1
                map_[right] = n_file_blocks - n_free_blocks
                assert map_[right] > 0
                map_[left] = 0
                left += 1
        else:
            n_file_blocks = map_[left]
            for _ in range(n_file_blocks):
                result += file_id * position
                position += 1
            file_id += 1
            left += 1

    print(result)


if __name__ == "__main__":
    main()
