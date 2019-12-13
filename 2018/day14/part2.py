def createnew(scoreboard, elf1, elf2):
    combined = str(scoreboard[elf1] + scoreboard[elf2])
    assert len(combined) in (1, 2)
    for score in combined:
        s = int(score)
        assert s >= 0 and s <= 9
        scoreboard.append(s)
    elf1 = (elf1 + scoreboard[elf1] + 1) % len(scoreboard)
    elf2 = (elf2 + scoreboard[elf2] + 1) % len(scoreboard)
    return scoreboard, elf1, elf2


def search(scoreboard, sequence):
    seqlen = len(sequence)
    count = 0
    elf1 = 0
    elf2 = 1
    while True:
        if len(scoreboard) >= seqlen:
            assert len(scoreboard[-seqlen:]) == seqlen
            if scoreboard[-seqlen:] == sequence:
                return len(scoreboard[:-seqlen])
            if len(scoreboard) > seqlen:
                assert len(scoreboard[-seqlen - 1:-1]) == seqlen
                if scoreboard[-seqlen - 1:-1] == sequence:
                    return len(scoreboard[:-seqlen - 1])
        scoreboard, elf1, elf2 = createnew(scoreboard, elf1, elf2)
        count += 1


if __name__ == "__main__":
    scoreboard = [3, 7]

    sequence = [5, 1, 5, 8, 9]
    numrecipes = search(list(scoreboard), sequence)
    assert numrecipes == 9

    sequence = [0, 1, 2, 4, 5]
    numrecipes = search(list(scoreboard), sequence)
    assert numrecipes == 5

    sequence = [9, 2, 5, 1, 0]
    numrecipes = search(list(scoreboard), sequence)
    assert numrecipes == 18

    sequence = [5, 9, 4, 1, 4]
    numrecipes = search(list(scoreboard), sequence)
    assert numrecipes == 2018

    sequence = [0, 3, 0, 1, 2, 1]
    numrecipes = search(list(scoreboard), sequence)
    print(numrecipes)
