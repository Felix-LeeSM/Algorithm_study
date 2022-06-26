'''
로봇 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	14902	3866	2566	25.204%
문제
많은 공장에서 로봇이 이용되고 있다. 우리 월드 공장의 로봇은 바라보는 방향으로 궤도를 따라 움직이며, 
움직이는 방향은 동, 서, 남, 북 가운데 하나이다. 로봇의 이동을 제어하는 명령어는 다음과 같이 두 가지이다.

명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.
공장 내 궤도가 설치되어 있는 상태가 아래와 같이 0과 1로 이루어진 직사각형 모양으로 로봇에게 입력된다. 
0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점이고, 1은 궤도가 없어 로봇이 갈 수 없는 지점이다. 
로봇이 (4, 2) 지점에서 남쪽을 향하고 있을 때,  이 로봇을 (2, 4) 지점에서 동쪽으로 향하도록 이동시키는 것은 아래와 같이 9번의 명령으로 가능하다.



로봇의 현재 위치와 바라보는 방향이 주어졌을 때, 로봇을 원하는 위치로 이동시키고, 
원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공장 내 궤도 설치 상태를 나타내는 직사각형의 세로 길이 M과 가로 길이 N이 빈칸을 사이에 두고 주어진다. 
이때 M과 N은 둘 다 100이하의 자연수이다. 
이어 M줄에 걸쳐 한 줄에 N개씩 각 지점의 궤도 설치 상태를 나타내는 숫자 0 또는 1이 빈칸을 사이에 두고 주어진다. 
다음 줄에는 로봇의 출발 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다. 
마지막 줄에는 로봇의 도착 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다. 
방향은 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4로 주어진다. 출발지점에서 도착지점까지는 항상 이동이 가능하다.

출력
첫째 줄에 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수를 출력한다.

예제 입력 1 
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 1
예제 출력 1 
9
'''

# https://www.acmicpc.net/problem/1726

import collections


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

INF = 1e9
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
inOut = {1:0, 2:2, 3:1, 4:3}
distDir = [[[INF]*4 for _ in range(n)] for _ in range(m)]
distDir[sx-1][sy-1][inOut[sd]] = 0

queue = collections.deque()
queue.append((sx-1, sy-1, inOut[sd]))
while queue:
    x, y, d = queue.popleft() # 출발 좌표, 방향
    if distDir[x][y][(d-1)%4] > distDir[x][y][d]: # 회전이동
        distDir[x][y][(d-1)%4] = distDir[x][y][d]+1
        queue.append((x, y, (d-1)%4))
    if distDir[x][y][(d+1)%4] > distDir[x][y][d]: # 회전이동은 두 방향이다.
        distDir[x][y][(d+1)%4] = distDir[x][y][d]+1
        queue.append((x, y, (d+1)%4))
    for i in range(1, 4): # 1~3칸 이동한다.
        dx, dy = dir[d]
        nx, ny = x+dx*i, y+dy*i
        if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny]: # 못 가는 곳이면 더 갈 수 없다.
            break
        if distDir[nx][ny][d] > distDir[x][y][d]+1:
            distDir[nx][ny][d] = distDir[x][y][d]+1
            queue.append((nx, ny, d))
print(distDir[ex-1][ey-1][inOut[ed]])

'''
90도씩 방향전환 하는 것을 아무 생각 없이 방향을 1 더하고 빼는 것으로 했었다. 
이것을 고려하는지 보기 위해서 문제에서 동서남북 방향으로 숫자를 줬던 것 갔다.
이걸 고려해서 변환해주는 inOut이라는 딕셔너리를 만들어서 해결하였다.
'''