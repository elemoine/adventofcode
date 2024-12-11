stones = "2 77706 5847 9258441 0 741 883933 12"
stones = stones.strip().split(" ")

for _ in range(25):
    new = []
    for s in stones:
        if s == "0":
            new.append("1")
        elif len(s) % 2 == 0:
            s1 = s[: len(s) // 2]
            s2 = s[len(s) // 2 :]
            s2 = s2.lstrip("0")
            if len(s2) == 0:
                s2 = "0"
            new.append(s1)
            new.append(s2)
        else:
            new.append(str(int(s) * 2024))
    stones = new

print(len(stones))
