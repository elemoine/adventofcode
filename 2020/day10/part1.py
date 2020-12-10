from collections import Counter


def read_ratings(inputfile):
    with open(inputfile) as f:
        return set(int(line) for line in f)


def test_adapters(ratings):
    count = Counter()
    c = 0
    while ratings:
        for v in range(c + 1, c + 4):
            if v in ratings:
                break
        else:
            raise Exception("No proper rating found")
        ratings.remove(v)
        count[v - c] += 1
        c = v
    return count


def main():
    ratings = read_ratings("input")
    ratings.add(max(ratings) + 3)
    distribution = test_adapters(ratings)
    print(distribution[1] * distribution[3])


if __name__ == "__main__":
    main()
