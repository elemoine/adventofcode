import itertools


locks, keys = [], []

with open("input") as f_:
    lock, key = None, None
    for row in f_:
        row = row.strip()
        if not row:
            if lock:
                locks.append(tuple(lock))
            elif key:
                keys.append(tuple(key))
            lock, key = None, None
        elif not lock and not key:
            if row == "#####":
                lock = [0] * 5
            elif row == ".....":
                key = [5] * 5
            else:
                assert False
        elif lock:
            for i in range(5):
                lock[i] += row[i] == "#"
        elif key:
            for i in range(5):
                key[i] -= row[i] == "."
    if lock:
        locks.append(tuple(lock))
    elif key:
        keys.append(tuple(key))


print(
    sum(
        1
        for lock, key in itertools.product(locks, keys)
        if all(lock[i] + key[i] <= 5 for i in range(5))
    )
)
