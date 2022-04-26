'''
문제
뱀과 사다리 게임을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다. 게임은 크기가 10×10이고, 
총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. 예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, 
i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 도착한 칸이 사다리면, 
사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다. 즉, 사다리를 이용해 이동한 칸의 번호는 
원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 
동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

예제 입력 1 
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
예제 출력 1 
3

5를 굴려 6으로 이동한다.
6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
2를 굴려 100으로 이동한다.



예제 입력 2 
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
예제 출력 2 
5

5를 굴려 6으로 이동하고, 사다리를 이용해 80으로 이동한다. 
6을 굴려 86으로
6을 또 굴려 92로
6을 또 굴려 98로 이동하고
2를 굴려 100으로 이동한다.
'''


import sys
import collections
input = sys.stdin.readline

L, S = map(int, input().split())
shortcut = dict()
visited = set()
for _ in range(L+S):
    start, end = map(int, input().split())
    shortcut[start] = end
queue = collections.deque([(0, 1)])
while queue:
    cnt, position = queue.popleft()
    if position in visited:
        continue
    visited.add(position)
    if position == 100:
        print(cnt)
        break
    for i in range(1, 7):
        if position+i in shortcut:
            queue.append((cnt+1, shortcut[position+i]))
        else:
            queue.append((cnt+1, position+i))

# Python3의 경우 88ms, Pypy3의 경우 140ms가 소요되었다.

'''
import collections
import sys
input = sys.stdin.readline

L, S = map(int, input().split())
shortcut = collections.defaultdict(int)
visited = {1}
for _ in range(L+S):
    start, end = map(int, input().split())
    shortcut[start] = end
queue = collections.deque([(0, 1)])
while queue:
    cnt, position = queue.popleft()
    visited.add(position)
    if position == 100:
        print(cnt)
        break
    for i in range(1, 7):
        n_position = shortcut[position+i] or position+i
        if n_position in visited:
            continue
        n_cnt = cnt+1
        queue.append((n_cnt, n_position))


Pypy3으로 제출하여 868ms를 소요하였으며, Python3로 제출하였을 때에는 시간 초과였다.
'''

# 백트레킹을 시도할 때, 어떤 부분에서 검증을 거치느냐도 크게 작용하는 것을 알게 되었다.
