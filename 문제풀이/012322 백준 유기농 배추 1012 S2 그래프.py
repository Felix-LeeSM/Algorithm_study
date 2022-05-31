# 섬의 개수를 구하는 문제와 기본적으로 같으나, 그래프를 주는 형식이 다르다.

import sys

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
T = int(sys.stdin.readline())
for _ in range(T):
    stack = list()
    cnt = 0
    y, x, cavs =  map(int, sys.stdin.readline().strip().split())
    board = list()
    for __ in range(x):
        board.append([0]*y)
    for ___ in range(cavs):
        cord_y, cord_x = map(int, sys.stdin.readline().strip().split())
        board[cord_x][cord_y] = 1

    for i in range(x):
        for j in range(y):
            if board[i][j] == 0 :
                continue
            else :
                stack.append((i, j))
                cnt += 1
                while stack:
                    r, c = stack.pop()
                    board[r][c] = 0
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if nr < 0 or nc < 0 or nr >= x or nc >= y:
                            continue
                        else:
                            if board[nr][nc] == 1:
                                stack.append((nr, nc))
    print(cnt)