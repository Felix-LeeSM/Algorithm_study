# stack을 활용한 DFS와 재귀함수를 이용한 DFS 모두 실패했다.
# stack을 활용했을 때 시간 초과가 났고, 재귀함수는 구현에 실패했다....
# scores라는, 해당 지점에서 도착하는 경우의 수를 저장하는 배열을 만들어서
# 값을 계산했다.

'''
test case
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''


import sys
read = sys.stdin.readline

size = int(read())
board = tuple([tuple(map(int, read().split())) for _ in range(size)])
scores = [[0]*size for _ in range(size)]
scores[-1][-1] = 1
dx, dy = (0, 1), (1, 0)
sheet = []
cnt = 0

for i in range(size-1, -1, -1):
    for j in range(size-1, -1, -1):
        for k in range(2):
            ni, nj = i + dx[k]*board[i][j], j + dy[k]*board[i][j]
            if board[i][j] != 0:
                if 0 <= ni < size and 0 <= nj < size:
                    scores[i][j] += scores[ni][nj]
print(scores[0][0])