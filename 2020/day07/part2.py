from part1 import creategraph


def countbags(color, graph):
    cnt = 0
    for n, c in graph[color]:
        cnt += n + n * countbags(c, graph)
    return cnt


def main():
    graph = creategraph("input")
    print(countbags("shiny gold", graph))


if __name__ == "__main__":
    main()
