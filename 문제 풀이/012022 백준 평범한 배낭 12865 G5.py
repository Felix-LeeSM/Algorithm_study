# 최초의 풀이.
# N <= 100으로 이렇게 풀어도 시간이 부족하지 않다고 생각했지만, 그렇지 않았다. 
'''
N, W = map(int, input().split())
luggages = list()
for _ in range(N):
    luggages.append(list(map(int, input().split())))
luggages.sort(key=lambda x:x[0])
def solution(w, loads):
    if loads[0][0] > w:
        return 0
    else :
        return max([ loads[i][1] + solution(w-loads[i][0], loads[:i]+loads[i+1:]) for i in range(len(loads)) if w-loads[i][0]>=0])
print(solution(W, luggages))
'''
'''
import sys
read = sys.stdin.readline
N, W = map(int, read().split())
luggages = [0]
for _ in range(N):
    luggages.append(tuple(map(int, read().split())))
def solution(n, w, loads):
    board = [[0]*(w+1) for _ in range(n+1)]
    for j in range(1, n+1):
        for i in range(1, w+1):
            if i >= loads[j][0]:
                board[j][i] = max(board[j-1][i], board[j-1][i-loads[j][0]]+loads[j][1])
            else:
                board[j][i] = board[j-1][i]
    return board[n][w]
print(solution(N, W, luggages))
'''
# refine하기.

import sys
read = sys.stdin.readline
N, W = map(int, read().split())
luggages = [0]
for _ in range(N):
    luggages.append(tuple(map(int, read().split())))
def solution(n, w, loads):
    board = [[0]*(w+1)]
    cache = [[0]*(w+1)]
    for j in range(1, n+1):
        for i in range(1, w+1):
            if i >= loads[j][0]:
                cache[i] = max(board[i], board[i-loads[j][0]]+loads[j][1])
            else:
                cache[i] = board[i]
        board = cache
        cache = [[0]*(w+1)]
    return board[w]
print(solution(N, W, luggages))