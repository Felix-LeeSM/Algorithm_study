# https://www.acmicpc.net/problem/26106
from collections import defaultdict
from heapq import heappush as hpush, heappop as hpop
from sys import stdin, maxsize

input = stdin.readline

edge, node, forbidden = map(int, input().split())
fr, to = map(int, input().split())

graph = defaultdict(list)
forbidden_set = set()

for _ in range(edge):
    a_node, b_node, dist = map(int, input().split())
    graph[a_node].append((b_node, dist))

for _ in range(forbidden):
    forb = tuple(map(int, input().split()))
    forbidden_set.add(forb)


hq = [(0, fr, None)]
dists = defaultdict(lambda: defaultdict(lambda: maxsize))


while hq:
    dist, cur, prev = hpop(hq)
    if cur == to:
        print(dist)
        exit(0)

    for nxt, nxt_dist in graph[cur]:
        if (prev, cur, nxt) in forbidden_set:
            continue

        if dists[cur][nxt] > dist + nxt_dist:
            dists[cur][nxt] = dist + nxt_dist
            hpush(hq, (dists[cur][nxt], nxt, cur))

print(-1)
exit(0)
