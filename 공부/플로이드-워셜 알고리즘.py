from pprint import pprint
from collections import defaultdict
import sys

INF = sys.maxsize

# 플루이드 워셜
'''
<<입출력 예시>>
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력:
[[0, 4, 8, 6], [3, 0, 7, 9], [5, 9, 0, 4], [7, 11, 2, 0]]
'''


def floyd_warshall(graph):
    N = len(graph)
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for idx in range(1, N + 1):
        dist[idx][idx] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    for row in range(len(dist)):
        dist[row] = [i if i != INF else 0 for i in dist[row]][1:]
    del dist[0]
    return dist


input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

pprint(floyd_warshall(graph))


# 정확한 순위 문제
'''
<<입출력 예시>>
6 6
1 5
3 4
4 2
4 6
5 2
5 4

출력 : 1
```
'''
N, M = map(int, input().split())
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for idx in range(1, N + 1):
    dist[idx][idx] = 0

for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

result = 0
for cur in range(1, N + 1):
    cnt = 0
    # 현재 노드(cur)를 기준으로,
    # 다른 노드(node)로 갈 방법이 있는지 센다.
    for node in range(1, N + 1):
        if dist[cur][node] != INF or dist[node][cur] != INF:
            cnt += 1
    # 모든 노드에 대해 갈 수 있다면 순위를 아는 것.
    if cnt == N:
        result += 1
print(result)
