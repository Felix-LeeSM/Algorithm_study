# 자음이 최소 2개, 모음이 최소 1개 있어야 한다.

import sys
N, M = map(int, sys.stdin.readline().split())
letters = sorted(sys.stdin.readline().strip().split())
#m개의 문자에서 n개를 뽑아내는 것이다.
def operator(n, m):
    board = [0]*n
    vowels = {'a', 'e', 'i', 'o', 'u'} & set(letters)
    def dfs(i):
        if i >= n:
            to_go = board[:]
            for i in range(len(to_go)):
                to_go[i] = letters[to_go[i]]
            if 1 <= len(set(to_go)&vowels) <= n-2:
                print(''.join(to_go))
            else:
                pass
        else:
            for j in range(m): # 넣을 것
                for k in range(i): # 한바퀴 돌면서 더 작은 것만 취할 것.
                    if board[k] >= j:
                        break
                else:
                    board[i] = j
                    dfs(i+1)
    dfs(0)
operator(N, M)