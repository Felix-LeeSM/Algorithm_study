# DFS를 기준으로 풀이하였다.
# 채점결과 틀렸다.

'''
import sys
import collections
N = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(N):
    edge = sys.stdin.readline().strip().split()
    if len(edge) > 1:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
stack = ['1']
visited = []
while stack:
    node = stack.pop()
    if node in visited:
        continue
    else:
        visited.append(node)
        for i in graph[node]:
            stack.append(i)
print(len(visited)-1)
'''

import sys
import collections
N = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(edges):
    edge = sys.stdin.readline().strip().split()
    if len(edge) > 1:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
stack = ['1']
visited = []
while stack:
    print('stack :', stack)
    node = stack.pop()
    print('node :', node)
    print('visitied :',visited)
    if node in visited:
        continue
    else:
        visited.append(node)
        for i in graph[node]:
            stack.append(i)
print(len(visited)-1)

# 노드의 갯수를 따로 입력으로 준다. N개의 edge가 존재하는 것이 아니었다.
# 문제를 잘 읽도록 하자..