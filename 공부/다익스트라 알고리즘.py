from heapq import heappop, heappush
from sys import maxsize as INF


def dijkstra_pq(N: int, graph: list[list[int]], start: int, end: int) -> int:
    dists = [INF] * N
    dists[start] = 0

    pq = [(0, start)]
    while pq:
        acc, cur = heappop(pq)
        if cur == end:
            return acc

        if dists[cur] < acc:
            continue

        for nxt, dist in graph[cur]:
            if dists[nxt] > acc + dist:
                dist[nxt] = acc+dist
                heappush(pq, (acc+dist, nxt))

    return INF
