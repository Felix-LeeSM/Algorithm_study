'''
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 NXM 크기의 직사각형으로 나타낼 수 있으며, 1X1크기의 정사각형 칸으로 나누어져 있다. 
각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 
지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.

2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 
d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 
빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.
'''
'''
import sys
read = sys.stdin.readline

row, col = map(int, read().split())
board = []
x, y, d = map(int, read().split())
for _ in range(row):
    board.append(list(map(int, read().split())))
vector = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 왼쪽으로 돈다. >> dir -= 1
def operator():
    stack = [(x, y)]
    rotation = 0
    dir = d
    cnt = 1
    board[x][y] = 2
    while True:
        i, j = stack.pop()
        print(i, j)
        rotation = 0
        while rotation < 5:
            rotation += 1
            dir -= 1
            dir %= 4
            ni, nj = i + vector[dir][0], j + vector[dir][1]
            if not (0 <= ni < row and 0 <= nj < col):
                continue
            if board[ni][nj] == 0:
                break

        else:
            bi, bj = i - vector[dir-2][0], j + vector[dir-2][1]
            if 0 <= bi < row and 0 <= bj < col and board[bi][bj] != 1:
                stack.append((bi, bj))
                dir -= 2
                dir %= 4
                continue
            else:
                return cnt
            
        cnt += 1
        board[ni][nj] = 2
        stack.append((ni, nj))

print(operator())
for i in board:
    print(i)
def dfs():
    cnt = 0
    stack = list()
    stack.append((x, y))
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + vector[k][0]
            nj = j + vector[k][1]
            if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == 0:
                board[ni][nj] = 1
                stack.append((ni, nj))
                cnt += 1
'''
# https://www.acmicpc.net/problem/14503
i, j = map(int, input().split())
x, y, d = map(int, input().split())
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
board = [list(map(int, input().split())) for _ in range(i)]
dirty = [[1]*j for _ in range(i)]
a = 0
ans = 0
while True:
    if dirty[x][y]:
        dirty[x][y] = 0
        ans += 1
    while a < 4:
        d = (d-1) % 4
        a += 1
        nx, ny = x+dx[d], y+dy[d]
        if not board[nx][ny] and dirty[nx][ny]:
            x, y = nx, ny
            a = 0
            break
    else:
        nx, ny = x-dx[d], y-dy[d]
        if not board[nx][ny]:
            x, y = nx, ny
            a = 0
        else:
            print(ans)
            break
