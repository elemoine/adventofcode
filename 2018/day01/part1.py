def main():
    with open("input") as f:
        seq = [int(l.strip()) for l in f]
    s = sum(seq)
    print(s)


if __name__ == "__main__":
    main()
