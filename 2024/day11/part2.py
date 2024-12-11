stones = ""
stones = list(map(int, stones.strip().split(" ")))

cache = {}


def _change(stone):
    if stone == 0:
        return [1]
    elif len((stone_ := str(stone))) % 2 == 0:
        stone1 = stone_[: len(stone_) // 2]
        stone2 = stone_[len(stone_) // 2 :]
        return [int(stone1), int(stone2)]
    else:
        return [stone * 2024]


def change(stone, iter_):
    k = (stone, iter_)
    if k in cache:
        return cache[k]
    if iter_ == 1:
        v = cache[k] = len(_change(stone))
    elif stone == 0:
        v = cache[k] = change(1, iter_ - 1)
    elif len(str(stone)) % 2 == 0:
        v = cache[k] = sum(change(s, iter_ - 1) for s in _change(stone))
    else:
        v = cache[k] = change(stone * 2024, iter_ - 1)
    return v


print(sum(change(stone, 75) for stone in stones))
