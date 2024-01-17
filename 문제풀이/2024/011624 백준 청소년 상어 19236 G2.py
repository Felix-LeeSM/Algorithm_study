from collections import deque
from copy import deepcopy
from sys import maxsize, stdin


def input(): return stdin.readline().rstrip()


def move_fishes(board):
    for fish in range(1, 17):
        next_coord = list(filter(lambda coord: board[coord[0]][coord[1]][0] == fish,
                                 [(i, j) for i in range(4) for j in range(4)]))
        if not next_coord:
            continue
        x, y = next_coord.pop()
        d = board[x][y][1]

        for turn in range(8):
            dir = (d + turn) % 8
            dx, dy = vectors[dir]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if board[nx][ny][0] == -1:
                continue

            board[x][y][1] = dir
            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            break


def move_shark(board):
    x, y = filter(lambda coord: board[coord[0]][coord[1]][0] == -1,
                  [(i, j) for i in range(4) for j in range(4)]).__next__()

    ret = []

    dir = board[x][y][1]
    dx, dy = vectors[dir]

    for dist in range(1, 4):
        nx, ny = x + dx*dist, y + dy*dist

        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if board[nx][ny][0] == 0:
            continue

        new_board = deepcopy(board)

        eaten = new_board[nx][ny][0]
        new_board[nx][ny][0] = -1
        new_board[x][y] = [0, 0]

        ret.append((new_board, eaten))

    return ret


vectors = [(-1, 0), (-1, -1), (0, -1), (1, -1),
           (1, 0), (1, 1), (0, 1), (-1, 1)]

# 번호, 방향
board = [[] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, 8, 2):
        board[i].append([line[j], line[j+1]-1])


queue = deque()
queue.append((board, board[0][0][0]))
board[0][0][0] = -1
maximum = -maxsize

while queue:
    curr_board, eaten = queue.popleft()
    maximum = max(maximum, eaten)

    move_fishes(curr_board)

    for new_board, new_eaten in move_shark(curr_board):
        queue.append((new_board, eaten + new_eaten))

print(maximum)
