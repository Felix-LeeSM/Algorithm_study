'''
문제
NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 
모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 
단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 
만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 
이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 
서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 
이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.



1초가 지난 후에 시험관의 상태는 다음과 같다.



2초가 지난 후에 시험관의 상태는 다음과 같다.



결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스다. 따라서 3을 출력하면 정답이다.

입력
첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 
둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며, 
해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 
단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. 
N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

출력
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

예제 입력 1 
3 3
1 0 2
0 0 0
3 0 0
2 3 2
예제 출력 1 
3


예제 입력 2 
3 3
1 0 2
0 0 0
3 0 0
1 2 2
예제 출력 2 
0
'''
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
queue = list()
board = [[0]*N for _ in range(N)]
for i in range(N):
    line = tuple(map(int, input().split()))
    for j in range(N):
        if line[j]:
            heapq.heappush(queue, (0, line[j], i, j))
            board[i][j] = line[j]
S, X, Y = map(int, input().split())
t = 0
while queue:
    t, v, x, y = heapq.heappop(queue)
    if t == S:
        break
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
            board[nx][ny] = v
            heapq.heappush(queue, (t+1, v, nx, ny))
print(board[X-1][Y-1])

# 힙을 적절히 이용하면, 경쟁은 알아서 해결된다.
'''
import sys
import collections
input = sys.stdin.readline

di, dj = (0, 0, 1, -1), (1, -1, 0, 0)
n, k = map(int, input().split())
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

s, x, y = map(int, input().split())

now = [[] for _ in range(k+1)]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            now[board[i][j]].append((i, j))

for _ in range(s):
    if board[x-1][y-1]:
        break
    for v in range(1, k+1):
        que = collections.deque(now[v])
        now[v].clear()
        while que:
            i, j = que.popleft()
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and not board[ni][nj]:
                    board[ni][nj] = v
                    now[v].append((ni, nj))

print(board[x-1][y-1])
'''
