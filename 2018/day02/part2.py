def main():
    with open("input") as f:
        ids = [l.strip() for l in f]
    len_ = len(ids[0])
    for i in range(len_):
        for j in range(0, len(ids)):
            s1 = ids[j][:i]
            s2 = ids[j][i + 1:]
            for k in range(j + 1, len(ids)):
                if s1 == ids[k][:i] and s2 == ids[k][i + 1:]:
                    print(s1 + s2)


if __name__ == "__main__":
    main()
