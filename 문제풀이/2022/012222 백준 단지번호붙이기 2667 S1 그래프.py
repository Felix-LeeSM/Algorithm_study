# 무수한 반례는 모두 뚫었지만... 한시간 동안 틀려서 부여잡고 있었다.
# 변수 x, y를 원래 i, j로 했었는데, 이것이 문제였다. 
# 변수는 항상 나누어서 이용하자.


N = int(input())
board = list()
stack = list()
cnt = 0
di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)
each = list()
for _ in range(N):
    board.append(list(map(int, list(input()))))
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 0:
            continue
        else:
            eachbuild = 0
            stack.append((x, y))
            while stack:
                i, j = stack.pop()
                print(i, j)
                eachbuild += 1
                board[i][j] = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
                        continue
                    else :
                        if (ni, nj) not in stack and board[ni][nj] == 1:
                            stack.append((ni, nj))
            cnt += 1
            each.append(eachbuild)
print(cnt)
for i in sorted(each):
    print(i)