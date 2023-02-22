'''
벽 부수고 이동하기 4 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	12975	3634	2572	25.445%
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

벽을 부수고 이동할 수 있는 곳으로 변경한다.
그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.

출력
맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고, 
벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.

예제 입력 1 
3 3
101
010
101
예제 출력 1 
303
050
303

예제 입력 2 
4 5
11001
00111
01010
10101
예제 출력 2 
46003
00732
06040
50403
'''
# https://www.acmicpc.net/problem/16946

from collections import deque
from sys import stdin
input = stdin.readline


n, m = map(int, input().split())
board = [[i == '0' for i in list(input().rstrip())] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
answer = [[0]*m for _ in range(n)]
groupArea = [0]*(n*m+1)

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
group = 1
queue = deque([])


def inBoard(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


for i in range(n):
    for j in range(m):
        if not board[i][j]:
            visited[i][j] = group
            groupArea[group] += 1
            group += 1

        elif not visited[i][j]:
            queue.append((i, j))
            groupArea[group] += 1
            visited[i][j] = group

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if inBoard(nx, ny, n, m) and board[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = group
                        groupArea[group] += 1
                        queue.append((nx, ny))

            group += 1

for i in range(n):
    for j in range(m):
        if not board[i][j]:
            groups = set()
            for d in range(4):
                ni, nj = i+dx[d], j+dy[d]
                if inBoard(ni, nj, n, m) and board[ni][nj]:
                    groups.add(visited[ni][nj])
            for eachGroup in groups:
                answer[i][j] += groupArea[eachGroup]
            answer[i][j] += 1
            answer[i][j] %= 10

for line in answer:
    print(*line, sep='')
