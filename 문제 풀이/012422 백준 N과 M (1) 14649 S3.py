# cnt를 추가하여 몇개의 숫자가 출력되야 하는 지도 적었다.
# 그 이후의 결과를 무시하기 위해서 if j in board에서 [:i]를 한 것이 포인트.


import sys

def operator(n):
    cnt = 0
    board = [0]*n
    def dfs(i):
        if i >= n:
            nonlocal cnt
            cnt += 1
            for k in board:
                print(k, end=" ")
            print()
        else:
            for j in range(1, n+1):
                if j in board[:i]:
                    continue
                else:
                    board[i] = j
                    dfs(i+1)
    dfs(0)
    print(cnt)
    return
N, M = map(int, sys.stdin.readline().split())
operator(N,M)



