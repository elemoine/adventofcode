def read_ratings(inputfile):
    with open(inputfile) as f:
        return [int(line) for line in f]


def main():
    ratings = read_ratings("input")
    ratings.sort()
    max_ = ratings.pop()
    ratings.reverse()
    ratings.append(0)
    d = {max_: 1}
    for r in ratings:
        d[r] = d.get(r + 1, 0) + d.get(r + 2, 0) + d.get(r + 3, 0)
    print(d[0])


if __name__ == "__main__":
    main()
