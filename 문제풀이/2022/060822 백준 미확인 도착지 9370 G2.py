'''
문제
(취익)B100 요원, 요란한 옷차림을 한 서커스 예술가 한 쌍이 한 도시의 거리들을 이동하고 있다. 
너의 임무는 그들이 어디로 가고 있는지 알아내는 것이다. 
우리가 알아낸 것은 그들이 s지점에서 출발했다는 것, 그리고 목적지 후보들 중 하나가 그들의 목적지라는 것이다. 
그들이 급한 상황이기 때문에 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다. 이상이다. (취익)

어휴! (요란한 옷차림을 했을지도 모를) 듀오가 어디에도 보이지 않는다. 
다행히도 당신은 후각이 개만큼 뛰어나다. 
이 후각으로 그들이 g와 h 교차로 사이에 있는 도로를 지나갔다는 것을 알아냈다.

이 듀오는 대체 어디로 가고 있는 것일까?



예제 입력의 두 번째 케이스를 시각화한 것이다. 
이 듀오는 회색 원에서 두 검은 원 중 하나로 가고 있고 점선으로 표시된 도로에서 냄새를 맡았다. 
따라서 그들은 6으로 향하고 있다.

입력
첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다

첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다.
각각 교차로, 도로, 목적지 후보의 개수이다.
두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. 
s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. 
a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.
그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 
이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.
교차로 사이에는 도로가 많아봐야 1개이다. 
m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 
또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.

출력
테스트 케이스마다

입력에서 주어진 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력한다.
예제 입력 1 
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6
예제 출력 1 
4 5
6
'''

# https://www.acmicpc.net/problem/9370

import heapq
import sys
input = sys.stdin.readline
T = int(input())
INF = float('inf')
total = []

for each_case in range(T):
    nodes, roads, candidates = map(int, input().split())
    departure, g, h = map(int, input().split())
    graph = [[] for _ in range(nodes+1)]
    for _ in range(roads):
        s, e, d = map(int, input().split())
        graph[s].append((e, d))
        graph[e].append((s, d))
    arrivals = [int(input()) for _ in range(candidates)]

    for e, d in graph[g]:
        if e == h:
            mustGo = d
            break

    dists = [INF]*(nodes+1)
    dists[departure] = 0
    queue = [(0, departure)]
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        for node, dist in graph[cur_node]:
            if dists[node] > dist+cur_dist:
                dists[node] = dist+cur_dist
                heapq.heappush(queue, (dist+cur_dist, node))

    fromH = [INF]*(nodes+1)
    fromH[h] = 0
    queue = [(0, h)]
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        for node, dist in graph[cur_node]:
            if fromH[node] > dist+cur_dist:
                fromH[node] = dist+cur_dist
                heapq.heappush(queue, (dist+cur_dist, node))

    fromG = [INF]*(nodes+1)
    fromG[g] = 0
    queue = [(0, g)]
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        for node, dist in graph[cur_node]:
            if fromG[node] > dist+cur_dist:
                fromG[node] = dist+cur_dist
                heapq.heappush(queue, (dist+cur_dist, node))

    answer = []
    for arrival in arrivals:
        if dists[arrival] != INF and dists[arrival] == min(dists[h]+mustGo+fromG[arrival],
                                                           dists[g]+mustGo+fromH[arrival]):
            answer.append(arrival)
    answer.sort()
    total.append(answer)
for each in total:
    print(*each)

'''
float('inf') + 3 == float('inf')임을 고려하지 못해서 오래 걸렸다.
초기화할 때 float('inf')를 자주 쓰는데, 문제의 목적에 따라서 이 부분을 고려해야 한다.
'''