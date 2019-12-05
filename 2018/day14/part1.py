def createnew(scoreboard, elf1, elf2):
    combined = str(scoreboard[elf1] + scoreboard[elf2])
    for score in combined:
        scoreboard.append(int(score))
    elf1 = (elf1 + scoreboard[elf1] + 1) % len(scoreboard)
    elf2 = (elf2 + scoreboard[elf2] + 1) % len(scoreboard)
    return scoreboard, elf1, elf2


def scores(numrecipies):
    scoreboard = [3, 7]
    elf1 = 0
    elf2 = 1
    while len(scoreboard) < numrecipies + 10:
        scoreboard, elf1, elf2 = createnew(scoreboard, elf1, elf2)
    s = scoreboard[numrecipies:numrecipies + 10]
    assert len(s) == 10
    return s


def main():
    s = scores(5)
    assert s == [0, 1, 2, 4, 5, 1, 5, 8, 9, 1]
    s = scores(9)
    assert s == [5, 1, 5, 8, 9, 1, 6, 7, 7, 9]
    s = scores(18)
    assert s == [9, 2, 5, 1, 0, 7, 1, 0, 8, 5]
    s = scores(2018)
    assert s == [5, 9, 4, 1, 4, 2, 9, 8, 8, 2]
    s = scores(30121)
    print("".join(map(str, s)))


if __name__ == "__main__":
    main()
