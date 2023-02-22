'''
LCA 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	256 MB	16116	7002	4197	42.079%
문제
N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

예제 입력 1 
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15
예제 출력 1 
2
4
2
1
3
1
'''

from collections import deque
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize


def solution():
    NODES = int(input())
    temp = [[] for _ in range(NODES+1)]
    graph = [0 for _ in range(NODES+1)]
    visited = [0]*(NODES+1)

    for _ in range(NODES-1):
        one, ano = map(int, input().split())
        temp[one].append(ano)
        temp[ano].append(one)

    queue = deque([1])
    visited[1] = 1
    while queue:
        node = queue.popleft()
        for child in temp[node]:
            if not visited[child]:
                visited[child] = 1
                graph[child] = node
                queue.append(child)

    graph[1] = 1
    problems = int(input())
    answer = []

    for _ in range(problems):
        desc1, desc2 = map(int, input().split())
        answer.append(bfs(NODES, graph, desc1, desc2))

    return answer


def bfs(NODES, graph, desc1, desc2):
    visited = [0]*(NODES+1)

    while desc1 != 1:
        visited[desc1] = 1
        desc1 = graph[desc1]
    visited[1] = 1

    while True:
        if visited[desc2]:
            return desc2
        visited[desc2] = 1
        desc2 = graph[desc2]


for i in solution():
    print(i)
