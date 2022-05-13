'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
'''
n = int(input())
ans = [0]
board = [n+2]*n
check = [0]*n


def dfs(row):
    # row를 채워야 함.
    if row >= n:
        ans[0] += 1
        return
    for col in range(n):
        if check[col]:
            continue
        for bef in range(row):
            if row-bef == abs(board[bef]-col):
                break
        else:
            board[row] = col
            check[col] = 1
            dfs(row+1)
            check[col] = 0


dfs(0)
print(ans[0])
