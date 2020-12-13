def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines[1].strip()


def main():
    buses = read_input("input")
    buses = buses.split(",")
    buses = [(int(id_), pos) for pos, id_ in enumerate(buses) if id_ != "x"]
    ref_id, ref_pos = buses[0]
    n, step = 0, 1
    for _id, _pos in buses[1:]:
        while True:
            n += step
            ts = ref_id * n - ref_pos
            if (ts + _pos) % _id == 0:
                step *= _id  # this is the key, and the hard part of this puzzle
                break
    print(ts)


if __name__ == "__main__":
    main()
