# 번호가 작은 node부터 탐사해야 한다는 문제가 있다.
# stack의 경우, 뒤에서부터 연산에 이용되므로 stack에 append할 때 거꾸로 넣어 주어야 한다.

import sys
import collections

nodes, edges, root = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(edges):
    edge = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in graph.keys():
    graph[i].sort()

dfs_visited = list()
bfs_visited = list()

stack = list()
stack.append(root)

queue = collections.deque()
queue.append(root)

while stack:
    now = stack.pop()
    if now in dfs_visited:
        continue
    dfs_visited.append(now)
    for link in graph[now][::-1]:
        if link not in dfs_visited:
            stack.append(link)

while queue:
    now = queue.popleft()
    if now in bfs_visited:
        continue
    bfs_visited.append(now)
    for link in graph[now]:
        if link not in bfs_visited:
            queue.append(link)

for i in dfs_visited:
    print(i, end=' ')
print()
for i in bfs_visited:
    print(i, end=' ')