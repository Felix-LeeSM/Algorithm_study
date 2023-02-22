'''
레이저 통신 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	10655	3634	2513	32.062%
문제
크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.

'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 
레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.

레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다. 

아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 
왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.

7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
입력
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)

둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.

.: 빈 칸
*: 벽
C: 레이저로 연결해야 하는 칸
'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.

출력
첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.

예제 입력 1 
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......
예제 출력 1 
3
'''

# https://www.acmicpc.net/problem/6087

from sys import stdin
from heapq import heappop, heappush
input = stdin.readline
INF = 1e9

m, n = map(int, input().split())

board = [input().rstrip() for _ in range(n)]
memo = [[[INF]*4 for _ in range(m)] for __ in range(n)]

points = []

for i in range(n):
    for j in range(m):
        if (board[i][j]) == 'C':
            points.append((i, j))


x, y = points[0]
memo[x][y] = [0]*4

gr, gc = points[1]
queue = [(0, k, x, y) for k in range(4)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
while queue:
    mir, cur_dir, r, c = heappop(queue)
    if (r == gr and c == gc):
        break

    for dir in range(4):
        nr, nc = r+dr[dir], c+dc[dir]
        par = dir != cur_dir
        if (0 <= nr < n and 0 <= nc < m and board[nr][nc] != '*' and memo[nr][nc][dir] > mir+par):
            memo[nr][nc][dir] = mir+par
            heappush(queue, (mir+par, dir, nr, nc))

print(min(memo[gr][gc]))
