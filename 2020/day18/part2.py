import re


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
    if m := re.match(r"^(.+)\*(.+)$", s):
        return _calc(m.group(1)) * _calc(m.group(2))
    if m := re.match(r"^(\d+)\+(.+)$", s):
        return int(m.group(1)) + _calc(m.group(2))
    return int(s)


def calc(s):
    return _calc(s.replace(" ", ""))


def main():

    r = calc("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    assert r == 1445
    r = calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    assert r == 669060
    r = calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    assert r == 23340

    with open("input") as f:
        expressions = [e.strip() for e in f]
    r = sum(map(calc, expressions))
    print(r)


if __name__ == "__main__":
    main()
