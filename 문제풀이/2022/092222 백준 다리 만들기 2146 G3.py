'''
다리 만들기 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	192 MB	31778	11495	7170	33.264%
문제
여러 섬으로 이루어진 나라가 있다. 
이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다.
하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다. 
그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 
그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 
이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 
다음은 세 개의 섬으로 이루어진 나라의 지도이다.



위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 
이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 
다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.



물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 
위의 경우가 놓는 다리의 길이가 3으로 가장 짧다
(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 
그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 
항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.

예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
'''

# https://www.acmicpc.net/problem/2146

from collections import deque
from sys import stdin
input = stdin.readline


def in_board(x, y, n):
    return 0 <= x < n and 0 <= y < n


def trial():
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    cur = -1
    queue = deque()

    visited = [[0]*n for _ in range(n)]
    queues = [deque() for _ in range(5001)]
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queue.append((i, j))
                board[i][j] = cur
                visited[i][j] = 1

                while queue:
                    x, y = queue.popleft()
                    par = False
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if in_board(nx, ny, n):
                            if not visited[nx][ny] and board[nx][ny]:
                                visited[nx][ny] = 1
                                board[nx][ny] = cur
                                queue.append((nx, ny))

                            elif not board[nx][ny]:
                                par = True

                    if par:
                        queues[cur].append((x, y, 0))
                cur -= 1
    while True:
        for island in range(cur+1, 0):
            queue = queues[island]
            ran = queue[0][-1]

            while queue:
                x, y, dist = queue.popleft()
                if dist > ran:
                    queue.appendleft((x, y, dist))
                    break

                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if in_board(nx, ny, n):
                        # 방문한 적이 없으면, board는 비어있어
                        if not board[nx][ny] and not visited[nx][ny]:
                            board[nx][ny] = island
                            visited[nx][ny] = 1
                            queue.append((nx, ny, dist+1))
                        # 방문한 적이 있는데, 다른 친구야
                        elif board[nx][ny] and board[nx][ny] != island:
                            # [x][y]까지 dist가 소요되었음
                            # [nx][ny]까지 만약 board[nx][ny] > island라면,
                            # 즉, island는 -3이고 board[nx][ny] = -1이라면,
                            # i가 먼저 연산하여 도달한 것이니까 [nx][ny]까지도 dist가 소요되었을 것이야
                            if board[nx][ny] > island:
                                return dist*2
                            if board[nx][ny] < island:
                                return dist*2 + 1


print(trial())
