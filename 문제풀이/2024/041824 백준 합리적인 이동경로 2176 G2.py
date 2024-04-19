# https://www.acmicpc.net/problem/2176
from sys import stdin
from heapq import heappush as hpush, heappop as hpop
input = stdin.readline

nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes + 1)]
for _ in range(edges):
    n1, n2, dist = map(int, input().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

# 1 -> 2
queue = [(0, 2)]
distances = [float('inf')] * (nodes + 1)
distances[2] = 0

while queue:
    dist, node = hpop(queue)
    for next_node, next_dist in graph[node]:
        if distances[next_node] > dist + next_dist:
            distances[next_node] = dist + next_dist
            hpush(queue, (dist + next_dist, next_node))


dp = [-1] * (nodes + 1)
dp[2] = 1


def to_2(node):

    if dp[node] != -1:
        return dp[node]

    dp[node] = 0
    for next_node, _ in graph[node]:
        if distances[node] > distances[next_node]:
            dp[node] += to_2(next_node)
    return dp[node]


print(to_2(1))
