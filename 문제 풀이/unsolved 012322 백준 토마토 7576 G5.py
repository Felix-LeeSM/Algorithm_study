# 시간 초과가 난다...
# 현재 로직은 한번씩 추가하고
# 그 다음에 하나씩 다 바꾸는 것이다.

# 이 방법은 매우 필요 횟수 + 1만큼 탐색을 진행해야 한다. 
# >> 탐색을 한번만 해야한다.

# queue 2개를 옮겨다니면서 그 때마다 check하면 될 것 같기도 하다.
# ---- 012322
import sys

board = list()
cnt = -1
change = True
di = (1, 0, -1, 0)
dj = (0, -1, 0, 1)
y, x = map(int, sys.stdin.readline().strip().split())
for _ in range(x):
    board.append(sys.stdin.readline().strip().split())
queue = list()
while True:
    if not change:
        break
    change = False
    for i in range(x):
        for j in range(y):
            if board[i][j] == '1':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni < 0 or nj < 0 or ni >= x or nj >= y:
                        continue
                    else:
                        if board[ni][nj] == '0':
                            queue.append((ni, nj))
    while queue:
        r, c = queue.pop()
        board[r][c] = '1'
        change = True
    cnt += 1
print(board)
par = True
for i in range(x):
    if not par:
        break
    for j in range(y):
        if board[i][j] == '0':
            print('-1')
            par = False
            break
if par:
    print(cnt)