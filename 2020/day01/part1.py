def main():
    with open("input") as f:
        entries = [int(entry.strip()) for entry in f]
        for i in range(len(entries)):
            for j in range(len(entries)):
                if entries[i] + entries[j] == 2020:
                    return entries[i] * entries[j]


if __name__ == "__main__":
    print(main())
