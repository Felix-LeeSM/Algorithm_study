# 더 기본적인 방법.
# 이차원 배열을 이용한다.

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
                board[j][i] = max(board[j-1][i], board[j-1]
                                  [i-loads[j][0]]+loads[j][1])
            else:
                board[j][i] = board[j-1][i]
    return board[n][w]


print(solution(N, W, luggages))

# 메모리를 덜 쓰는 방법
# 한 줄 한 줄만 구현하여 메모리를 덜 소모한다.
# 시간은 많이 줄었는데, 메모리는 큰 차이가 없다.

read = sys.stdin.readline
N, W = map(int, read().split())
luggages = []
for _ in range(N):
    luggages.append(tuple(map(int, read().split())))


def solution(n, w, loads):
    board = [0]*(w+1)
    cache = [0]*(w+1)
    for j in range(n):
        for i in range(1, w+1):
            if i >= loads[j][0]:
                cache[i] = max(board[i], board[i-loads[j][0]]+loads[j][1])
            else:
                cache[i] = board[i]
        board = cache
        cache = [0]*(w+1)
    return board[w]


print(solution(N, W, luggages))

'''
가장 기본적인 knapsack 문제이다.
각각의 짐에 대해서 넣는다 / 넣지 않는다 2가지 경우로 나누고,
최후에 하나의 짐만 대상으로 넣는다 / 넣지 않는다를 나누어 각각의 경우를 board에 작성한다.
그리고 해당 경우에 대해서 또 그 다음 하나의 짐을 더 추가로 고려했을 경우를 board에 작성하는 식이다.
https://www.youtube.com/watch?v=rhda6lR5kyQ&t=641s&ab_channel=%EC%BD%94%EB%93%9C%EC%97%86%EB%8A%94%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
'''
