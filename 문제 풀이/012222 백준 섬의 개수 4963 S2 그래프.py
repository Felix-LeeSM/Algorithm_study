# 이 문제는 대각선도 움직일 수 있다.
# vector를 위한 dx와 dy에 이를 반영해주었다.


import sys
while True:
    stack = list()
    visited = list()
    cnt = 0
    dx = (1, 0, -1, 0, 1, 1, -1, -1)
    dy = (0, -1, 0, 1, 1, -1, -1, 1)
    j, i = map(int, sys.stdin.readline().split())
    if i + j == 0:
        break
    else:
        board = []
        for _ in range(i):
            board.append(sys.stdin.readline().strip().split())
        for x in range(i):
            for y in range(j):
                if board[x][y] == '0':
                    continue
                else:
                    stack.append((x, y))
                    while stack:
                        row, col = stack.pop()
                        board[row][col] = '0'
                        for k in range(8):
                            nrow = row + dx[k]
                            ncol = col + dy[k]
                            if nrow < 0 or ncol < 0 or nrow >= i or ncol >= j:
                                continue
                            else:
                                if board[nrow][ncol] == '0':
                                    continue
                                else:
                                    stack.append((nrow, ncol))
                    else:
                        cnt += 1
    print(cnt)