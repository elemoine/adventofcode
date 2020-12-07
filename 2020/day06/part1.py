def main():
    with open("input") as f:
        data = f.read().split("\n\n")
    groups = ["".join(g.split("\n")) for g in data]
    r = sum(len(set(g)) for g in groups)
    print(r)


if __name__ == "__main__":
    main()
