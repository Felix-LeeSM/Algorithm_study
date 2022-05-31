'''
문제
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. 
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

예제 입력 1 
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
예제 출력 1 
10
'''

# 플루이드 워셜 알고리즘 때리면 시간초과가 난다
# 플루이드 워셜은 정말 모든 걸 다 해봐야 할 때 쓰는 알고리즘인듯?

import heapq
import sys
def input(): return sys.stdin.readline().rstrip()


n, m, x = map(int, input().split())  # 마을(학생), 도로, 파티 마을
inf = float('inf')
board = [[inf]*(n+1) for _ in range(n+1)]
graph = {key: [] for key in range(1, n+1)}
for i in range(m):
    s, e, t = map(int, input().split())
    board[s][e] = t
    graph[s].append((e, t))
from_x = [inf]*(n+1)
from_x[x] = 0
que = [(0, x)]
while que:
    d, fr = heapq.heappop(que)
    for to, dist in graph[fr]:
        if from_x[to] > d+dist:
            from_x[to] = d+dist
            heapq.heappush(que, (d+dist, to))

to_x = [inf]*(n+1)
to_x[x] = 0
for i in range(1, n+1):
    line = [inf]*(n+1)
    if i == x:
        continue
    que = [(0, i)]
    while que:
        d, fr = heapq.heappop(que)
        if fr == x:
            to_x[i] = d
            break
        for to, dist in graph[fr]:
            if line[to] > d+dist:
                line[to] = d+dist
                heapq.heappush(que, (d+dist, to))

costs = [to_x[i]+from_x[i] for i in range(1, n+1)]
print(max(costs))
