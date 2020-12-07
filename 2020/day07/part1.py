import re

PATTERN_PART1 = r"^([\w\s]+)\sbags$"
PATTERN_PART2 = r"^(\d+)\s([\w\s]+)\sbags?$"


def parserule(rule):
    rule = rule.strip().rstrip(".")
    part1, part2 = tuple(r.strip() for r in rule.split("contain"))
    m = re.match(PATTERN_PART1, part1)
    color = m.group(1)
    contents = []
    for elt in part2.split(","):
        elt = elt.strip()
        if elt == "no other bags":
            break
        m = re.match(PATTERN_PART2, elt)
        contents.append((int(m.group(1)), m.group(2)))
    return color, tuple(contents)


def creategraph(inputfile):
    graph = {}
    with open(inputfile) as f:
        for rule in f:
            color, contents = parserule(rule)
            graph[color] = contents
    return graph


def search(color, graph, start):
    assert start in graph
    if start == color or not graph[start]:
        return 0
    for _, c in graph[start]:
        if c == color:
            return 1
        r = search(color, graph, c)
        if r == 1:
            return 1
    return 0


def main():
    graph = creategraph("input")
    print(sum(search("shiny gold", graph, color) for color in graph))


if __name__ == "__main__":
    main()
