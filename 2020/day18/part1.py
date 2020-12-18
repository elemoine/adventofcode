import operator
import re


ops = {"+": operator.add, "*": operator.mul}


def _calc(s):
    while (i := s.find("(")) > -1:
        a = []
        for j in range(i + 1, len(s)):
            if s[j] == ")":
                if a:
                    a.pop()
                else:
                    break
            elif s[j] == "(":
                a.append("(")
        else:
            raise Exception("unbalanced brackets")
        s = s[:i] + str(_calc(s[i + 1:j])) + s[j + 1:]
    if m := re.match(r"^(.*)([\+\*])(\d+)$", s):
        op = ops[m.group(2)]
        n2 = int(m.group(3))
        return op(_calc(m.group(1)), n2)
    return int(s)


def calc(s):
    return _calc(s.replace(" ", ""))


def main():
    assert calc("1 + 2 * 3 * 4") == 36
    assert calc("1 + 2 * (3 * 4)") == 36
    assert calc("1 + (2 * 3) * 4") == 28
    assert calc("(1 + 2) * 3 * 4") == 36
    assert calc("1 + (2 * 3 * 4)") == 25
    assert calc("1 + (2 + 3 * 4)") == 21
    assert calc("1 + (2 * 3) + (4 * 5)") == 27
    assert calc("1 + (2 * (3 + 4) * 5)") == 71
    assert calc("2 * 3 + (4 * 5)") == 26
    assert calc("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

    with open("input") as f:
        expressions = [e.strip() for e in f]
    r = sum(map(calc, expressions))
    print(r)


if __name__ == "__main__":
    main()
