'''
문제
V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 
마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 
돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 
사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 
두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.

입력
첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 
다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. 
a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a → b임에 주의) 
거리는 10,000 이하의 자연수이다. (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

출력
첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 
운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3 4
1 2 1
3 2 1
1 3 5
2 3 2
예제 출력 1 
3
'''
# 인터넷을 참조한 플로이드 워셜 알고리즘 이용 풀이
# https://tooo1.tistory.com/312
# python3으로 제출 시, 시간 초과.
# pypy3으로 제출하여야 성공할 수 있다.

import sys
INF = sys.maxsize

nodes, edges = map(int, sys.stdin.readline().split())
board = [[INF]*(nodes+1) for _ in range(nodes+1)]

for _ in range(edges):
    dep, arr, cost = map(int, sys.stdin.readline().split())
    board[dep][arr] = cost
for v in range(1, nodes+1):  # 거쳐가는 노드
    for s in range(1, nodes+1):  # 시작하는 노드
        for e in range(1, nodes+1):  # 도착하느 노드
            board[s][e] = min(board[s][e], board[s][v] + board[v][e])
inter = INF
for i in range(1, nodes+1):
    inter = min(inter, board[i][i])
if inter == INF:
    print(-1)
else:
    print(inter)


'''
# 내가 작성한 틀린 풀이

import collections

graph = collections.defaultdict(list)
nodes, edges = map(int, sys.stdin.readline().split())

for _ in range(edges):
    s, e, d = map(int, sys.stdin.readline().split())
    graph[s-1].append((e-1, d))


def dfs(now, cost, order):
    for e, d in graph[now]:
        if e in order:
            idx = order.index(0)
            if idx == 0:
                ret.append(cost[-1])
            else:
                needless = cost[order.index(e)-1]
                ret.append(cost[-1]-needless)
        else:
            order.append(e)
            cost.append(cost[-1]+d)
            dfs(e, cost, order)

ret = []
for i in range(nodes):
    dfs(i, [0], [i])

print(min(ret))
'''
