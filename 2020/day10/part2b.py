def read_ratings(inputfile):
    with open(inputfile) as f:
        return set(int(line) for line in f)


def count(ratings, current, target, cache={}):
    if current not in ratings:
        return 0
    for i in (1, 2, 3):
        if current + i == target:
            return 1
    if current in cache:
        return cache[current]
    r = sum(count(ratings, current + i, target) for i in (1, 2, 3))
    cache[current] = r
    return r


def main():
    ratings = read_ratings("input")
    ratings.add(0)
    target = max(ratings) + 3
    c = count(ratings, 0, target)
    print(c)


if __name__ == "__main__":
    main()
