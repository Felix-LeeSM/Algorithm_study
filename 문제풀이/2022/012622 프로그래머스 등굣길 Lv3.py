# m이 그림 상 x좌표고, n이 그림 상 y좌표이다.
# 문제를 잘 읽자...
# 파이썬은 그렇지 않지만 값이 매우 큰 문제의 경우에는
# 숫자의 크키가 문제가 될 수 있다.
# 1000000007로 나눈 나머지를 출력해야 하는 문제였다...


def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]
    board[n-1][m] = 1
    for i in puddles:
        x, y = i
        board[y-1][x-1] = -1

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if board[j][i] == -1:
                board[j][i] = 0
            else:
                board[j][i] = (board[j][i+1] + board[j+1][i])%1000000007
    return board[0][0]