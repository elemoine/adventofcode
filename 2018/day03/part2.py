from collections import defaultdict


def readclaims(inputfile):
    with open(inputfile) as f:
        lines = [l.strip() for l in f]
    claims = []
    for l in lines:
        tmp = l.split("@")
        assert len(tmp) == 2
        id_, values = tmp[0].strip(), tmp[1].strip()
        id_ = int(id_[1:])
        assert id_ == len(claims) + 1
        tmp = values.split(":")
        assert len(tmp) == 2
        pos, dim = tmp[0].strip(), tmp[1].strip()
        pos = pos.split(",")
        assert len(pos) == 2
        pos = tuple(map(int, pos))
        dim = dim.split("x")
        assert len(dim) == 2
        dim = tuple(map(int, dim))
        claims.append(pos + dim)
    return claims


if __name__ == "__main__":
    claims = readclaims("input")
    d = defaultdict(int)
    for c in claims:
        for x in range(c[0], c[0] + c[2]):
            for y in range(c[1], c[1] + c[3]):
                d[(x, y)] += 1
    for i, c in enumerate(claims):
        for x in range(c[0], c[0] + c[2]):
            for y in range(c[1], c[1] + c[3]):
                if d[(x, y)] > 1:
                    break
            else:
                continue
            break
        else:
            print("found it!", i + 1)
            break
