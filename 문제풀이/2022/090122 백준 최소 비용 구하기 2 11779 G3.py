'''
최소비용 구하기 2 성공스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	18166	6603	4616	36.559%
문제
n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 
항상 시작점에서 도착점으로의 경로가 존재한다.

입력
첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다.
그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 
버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.

예제 입력 1 
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
예제 출력 1 
4
3
1 3 5
'''

'''
1안 거쳐간 도시 수와 비용을 저장하여 후에 비교에 사용한다.
    조건에 맞는 도시가 적을 것을 기대한다.
    
from collections import defaultdict, deque
from heapq import heappop, heappush
from sys import stdin, maxsize

input = stdin.readline
INF = maxsize

nodes = int(input())
buses = int(input())

graph = defaultdict(list)

for _ in range(buses):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))

fr, to = map(int, input().split())

# 경유, 비용
dp = [[INF, INF] for _ in range(nodes+1)]
dp[fr] = [1, 0]
queue = [(0, fr, 1)]

while queue:
    cost_sum, node, been = heappop(queue)
    if node == to:
        break

    for city, cost in graph[node]:
        if dp[city][1] > cost+cost_sum:
            dp[city] = [been+1, cost+cost_sum]
            heappush(queue, (cost+cost_sum, city, been+1, ))

# been이 갯수, cost_sum이 최소 비용

queue = deque([(fr, 1, 0, [fr])])

while queue:
    node, cur_been, cur_cost, cities_been = queue.popleft()
    if node == to:
        break

    for city, cost in graph[node]:
        if dp[city][0] == cur_been+1 and dp[city][1] == cur_cost+cost:
            queue.append((city, cur_been+1, cur_cost +
                         cost, cities_been + [city]))

print(cost_sum)
print(been)
print(*cities_been)
'''

# paths 배열에서 이전 도시를 계속 갱신하며 저장한다.

from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

nodes = int(input())
buses = int(input())

graph = defaultdict(list)

for _ in range(buses):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))

fr, to = map(int, input().split())

# 경유, 비용
dists = [INF]*(nodes+1)
paths = [i for i in range(nodes+1)]
dists[fr] = 0
queue = [(0, fr, 1)]

while queue:
    cost_sum, node, been = heappop(queue)
    if node == to:
        break

    for city, cost in graph[node]:
        if dists[city] > cost+cost_sum:
            dists[city] = cost+cost_sum
            paths[city] = node
            heappush(queue, (cost+cost_sum, city, been+1, ))

# been이 갯수, cost_sum이 최소 비용

node = to
cities_been = [to]
while paths[node] != node:
    cities_been.append(paths[node])
    node = paths[node]
    pass

print(cost_sum)
print(been)
print(*reversed(cities_been))
