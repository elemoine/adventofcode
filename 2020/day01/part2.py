def main():
    with open("input") as f:
        entries = [int(entry.strip()) for entry in f]
        for i in range(len(entries)):
            for j in range(len(entries)):
                for k in range(len(entries)):
                    if entries[i] + entries[j] + entries[k] == 2020:
                        return entries[i] * entries[j] * entries[k]


if __name__ == "__main__":
    print(main())
