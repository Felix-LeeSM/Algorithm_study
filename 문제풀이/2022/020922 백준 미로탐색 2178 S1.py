'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13

'''
import sys
import heapq
INF = 10000  # row, col이 최대 100이므로, 10000을 넘는 경우는 존재하지 않는다.
row, col = map(int, sys.stdin.readline().split())
v = ((0, 1), (0, -1), (1, 0), (-1, 0))

board = [list(map(int, list(sys.stdin.readline().strip())))
         for _ in range(row)]
for i in range(row):
    for j in range(col):
        if board[i][j] == 1:
            board[i][j] = INF
board[0][0] = 1
queue = [(1, 0, 0)]  # 거리, 행, 열 순으로 삽입. why? 우선순위 큐를 힙큐로 구현하기 위함.

while queue:
    d, oldr, oldc = heapq.heappop(queue)
    for i in range(4):
        nr, nc = oldr+v[i][0], oldc+v[i][1]
        if nr == row-1 and nc == col-1:  # 우선순위 큐이므로 도착하면 끝이다.
            print(d+1)
            # break를 해봤자 for문을 탈출하고 만다. >> while queue에서 queue를 False로 바꿔준다.
            queue = False
            break
        if 0 <= nr < row and 0 <= nc < col:  # 허공이 아니면!
            if board[nr][nc] != 0 and board[nr][nc] > d+1:  # 더 작게 도달하지 못했으면!
                board[nr][nc] = d+1  # 갈아치우고,
                heapq.heappush(queue, (d+1, nr, nc))  # 한번 더 탐색
