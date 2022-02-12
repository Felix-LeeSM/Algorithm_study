'''
문제
NxM의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 
이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 
이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 
개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15

예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1

'''
import sys
import heapq
input = sys.stdin.readline

i, j = map(int, input().split())
INF = i*j
board = [list(map(int, list(input().strip()))) for _ in range(i)]
dx, dy = (0, 0, -1, 1), (-1, 1, 0, 0)
distances = [[INF]*j for _ in range(i)]
distances[0][0] = 1
iswall = False

if board[0][0] == 1:
    queue = [(True, 1, 0, 0)]
else:
    queue = [(False, 1, 0, 0)]  # 부수 술 수 있음.

while queue:
    done, d, x, y = heapq.heappop(queue)
    for l in range(4):
        nx, ny = x+dx[l], y+dy[l]
        if 0 <= nx < i and 0 <= ny < j:
            if distances[nx][ny] > d+1:
                if not done:
                    if board[nx][ny] == 1:
                        distances[nx][ny] = d+1
                        heapq.heappush(queue, (True, d+1, nx, ny))
                    else:
                        distances[nx][ny] = d+1
                        heapq.heappush(queue, (False, d+1, nx, ny))
                else:
                    if board[nx][ny] == 0:
                        distances[nx][ny] = d+1
                        heapq.heappush(queue, (True, d+1, nx, ny))

ans = -1 if distances[-1][-1] == INF else distances[-1][-1]
if i == j == 1:
    ans = 1
print(ans)
