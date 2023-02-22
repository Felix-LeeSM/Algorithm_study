'''
로봇 청소기 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	8313	2696	1766	30.501%
문제
오늘은 직사각형 모양의 방을 로봇 청소기를 이용해 청소하려고 한다. 
이 로봇 청소기는 유저가 직접 경로를 설정할 수 있다.

방은 크기가 1×1인 정사각형 칸으로 나누어져 있으며, 로봇 청소기의 크기도 1×1이다. 
칸은 깨끗한 칸과 더러운 칸으로 나누어져 있으며, 로봇 청소기는 더러운 칸을 방문해서 깨끗한 칸으로 바꿀 수 있다.

일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다. 

로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 또, 로봇은 같은 칸을 여러 번 방문할 수 있다.

방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트케이스로 이루어져 있다.

각 테스트 케이스의 첫째 줄에는 방의 가로 크기 w와 세로 크기 h가 주어진다. 
(1 ≤ w, h ≤ 20) 
둘째 줄부터 h개의 줄에는 방의 정보가 주어진다. 
방의 정보는 4가지 문자로만 이루어져 있으며, 각 문자의 의미는 다음과 같다.

.: 깨끗한 칸
*: 더러운 칸
x: 가구
o: 로봇 청소기의 시작 위치
더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각각의 테스트 케이스마다 더러운 칸을 모두 깨끗한 칸으로 바꾸는 이동 횟수의 최솟값을 한 줄에 하나씩 출력한다. 
만약, 방문할 수 없는 더러운 칸이 존재하는 경우에는 -1을 출력한다.

예제 입력 1 
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
예제 출력 1 
8
49
-1
'''

# https://www.acmicpc.net/problem/4991

from collections import deque
from heapq import heappop, heappush
from sys import stdin


def input():
    return stdin.readline().rstrip()


class inf(int):
    def __new__(self):
        return super(inf, self).__new__(self, 9223372036854775807)

    def __repr__(self):
        return 'inf'


INF = inf()


def inBoard(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def solution():
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        return None

    board = []
    dirts = [[0]*m for _ in range(n)]
    dirtCoords = [None]
    dirtNum = 1
    for i in range(n):
        line = input()
        temp = []
        for j, box in enumerate(line):
            if box == 'o':
                coord = (i, j)
                dirtCoords[0] = (i, j, 0)

            if box == 'x':
                temp.append(0)
            elif box == '*':
                dirts[i][j] = 1
                dirtCoords.append((i, j, dirtNum))
                temp.append(-dirtNum)
                dirtNum += 1
            else:
                temp.append(1)
        board.append(temp)

    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    dirtDists = [[INF]*dirtNum for _ in range(dirtNum)]
    for i, j, no in dirtCoords:
        queue = deque([(i, j, 0)])
        visited = [[0]*m for _ in range(n)]
        visited[i][j] = 1

        while queue:
            x, y, dist = queue.popleft()
            if board[x][y] < 0:
                dirtNum = -board[x][y]
                dirtDists[dirtNum][no] = dirtDists[no][dirtNum] = dist
            elif (x, y) == coord:
                dirtDists[0][no] = dirtDists[no][0] = dist

            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if inBoard(nx, ny, n, m) and board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist+1))

    dirtNum = len(dirtDists)
    goal = 2**dirtNum - 1
    queue = [(0, 0, 1)]
    while queue:
        dist, node, visited = heappop(queue)
        if visited == goal:
            return dist
        for i in range(1, dirtNum):
            if not visited & 2**i and dirtDists[node][i] != INF:
                heappush(queue, (dist+dirtDists[node][i], i, visited | 2**i))
    return -1


while True:
    ans = solution()
    if ans:
        print(ans)
        continue
    break
