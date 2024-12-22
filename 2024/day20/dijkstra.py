import sys
from heapq import heapify, heappop, heappush


def shortest_distances(graph, source):
    distances = {node: sys.maxsize for node in graph}
    distances[source] = 0

    pq = [(0, source)]
    heapify(pq)

    visited = set()

    while pq:
        dist, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            td = dist + weight
            if td < distances[neighbor]:
                distances[neighbor] = td
                heappush(pq, (td, neighbor))

    predecessors = {node: None for node in graph}
    for node, distance in distances.items():
        for neighbor, weight in graph[node].items():
            if distances[neighbor] == distance + weight:
                predecessors[neighbor] = node

    return distances, predecessors


def shortest_path(graph, source, target):
    _, predecessors = shortest_distances(graph, source)
    path = []
    current = target
    while current:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path
