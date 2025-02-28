from heapq import heappush, heappop
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        queue = [(0, 0)]
        dists = [float("inf")] * n
        dists[0] = 0

        cnts = [0] * n
        cnts[0] = 1

        while queue:
            dist, node = heappop(queue)

            for neighbor, distance in graph[node]:
                if dists[neighbor] > dist + distance:
                    dists[neighbor] = dist + distance
                    cnts[neighbor] = cnts[node]
                    heappush(queue, neighbor)
                elif dists[neighbor] == dist + distance:
                    cnts[neighbor] = (cnts[neighbor] + cnts[node]) % mod

        return cnts[-1]
