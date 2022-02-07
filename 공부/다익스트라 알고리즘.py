'''
하나의 정점으로부터 다른 모든 정점으로 이어지는 최단 거리를 기록하는 알고리즘
거리 배열과 방문 배열로 시작한다.
거리 = [0, inf, inf, inf, inf]
방문 = [True, False, False, False, False]

testcase 1
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
star node, end node, distance 순이다.
assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
'''
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b까지 c가 든다.

INF = int(1e9)

# 이 경우, n**2의 시간 복잡도.
# why? 미 방문 최소 거리 node를 매번 찾는 것이
# n의 시간 복잡도가 소요된다.


def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node()
        visited[cur] = True
        # 최단거리를 비교, 수정한다.
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist

# 이 경우, heqpq를 사용하여 visited가 필요없다.
# 필요하지 않은 연산은 무시되기 때문이다.


def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist
