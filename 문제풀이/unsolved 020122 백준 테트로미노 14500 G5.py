import sys
N, M = map(int, sys.stdin.readline().split())
board = list()
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
vector = ((0, 1), (0, -1), (1, 0), (-1, 0))
def dfs(lv, nomino):
    if lv == 4:
        ret = 0
        for x, y in nomino:
            print(y, x)
            ret += board[y][x]
        return ret
    else:
        x, y = nomino[-1]
        for i in range(4):
            nx, ny = x + vector[i][0], y + vector[i][1]
            if not(0 <= nx < len(board[0]) and 0 <= ny <= len(board)):
                continue
            else:
                if (nx, ny) in nomino:
                    continue
                else:
                    dfs(lv+1, nomino+[(nx, ny)])
answer = []
for i in range(len(board[0])):
    for j in range(len(board[1])):
        answer.append(dfs(1, [(j, i)]))
print(max(answer))