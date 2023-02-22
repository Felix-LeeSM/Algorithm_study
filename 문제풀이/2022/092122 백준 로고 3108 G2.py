'''
로고 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	3892	1254	839	29.858%
문제
로고는 주로 교육용에 쓰이는 프로그래밍 언어이다. 
로고의 가장 큰 특징은 거북이 로봇인데, 
사용자는 이 거북이 로봇을 움직이는 명령을 입력해 화면에 도형을 그릴 수 있다.

거북이는 위치와 각도로 표현할 수 있다. 거북이는 입에 연필을 물고 있는데, 
연필을 내리면 움직일 때 화면에 선을 그리고, 올리면 선을 그리지 않고 그냥 지나가기만 한다.

제일 처음에 거북이는 (0,0)에 있고, 거북이가 보고 있는 방향은 y축이 증가하는 방향이다. 
또한 연필은 내리고 있다.

사용자는 다음과 같은 다섯가지 명령으로 거북이를 조정할 수 있다.

FD x: 거북이를 x만큼 앞으로 전진
LT a: 거북이를 반시계 방향으로 a도 만큼 회전
RT a: 거북이를 시계 방향으로 a도 만큼 회전
PU: 연필을 올린다
PD: 연필을 내린다.

축에 평행한 직사각형 N개가 주어졌을 때, 
이 직사각형을 그리는데 필요한 PU 명령의 최솟값을 구하는 프로그램을 작성하시오.

거북이는 같은 선을 여러 번 그릴 수 있지만, 문제에 주어진 직사각형 N개를 제외한 어떤 것도 그릴 수 없다. 
거북이의 크기는 아주 작아서 좌표 평면의 한 점이라고 생각하면 된다. 직사각형의 변은 축에 평행하다.

입력
첫째 줄에 직사각형의 개수 N이 주어진다. (1 ≤ N ≤ 1000)

다음 N개의 줄에는 직사각형의 좌표 x1, y1, x2, y2가 주어진다. 
(−500 ≤ x1 < x2 ≤ 500), (−500 ≤ y1 < y2 ≤ 500) 
(x1, y1)는 직사각형의 한 꼭짓점 좌표이고, 
(x2, y2)는 그 점의 대각선 방향의 반대 꼭짓점의 좌표이다.

출력
N개의 직사각형을 그리는 필요한 PU명령의 최솟값을 출력한다.

예제 입력 1 
1
0 0 10 10
예제 출력 1 
0
예제 입력 2 
1
-5 -5 5 5
예제 출력 2 
1
예제 입력 3 
5
1 1 4 4
3 3 6 6
4 4 5 5
5 0 8 3
6 1 7 2
예제 출력 3 
2

'''

# https://www.acmicpc.net/problem/3108

from collections import deque

N = int(input())
boardSize = 2003
gap = (boardSize-1)//2


def processCoords(x1, y1, x2, y2, gap):
    return (
        2*min(x1, x2)+gap,
        2*min(y1, y2)+gap,
        2*max(x1, x2)+gap,
        2*max(y1, y2)+gap
    )


def preProcess(board, x1, y1, x2, y2):
    board[x1][y1] += 1
    board[x1][y2+1] -= 1
    board[x2+1][y1] -= 1
    board[x2+1][y2+1] += 1

    board[x1+1][y1+1] -= 1
    board[x1+1][y2] += 1
    board[x2][y1+1] += 1
    board[x2][y2] -= 1
    pass


def postProcess(board, boardSize):
    boardSize = len(board)
    for i in range(boardSize):
        for j in range(1, boardSize):
            board[i][j] += board[i][j-1]
    for j in range(boardSize):
        for i in range(1, boardSize):
            board[i][j] += board[i-1][j]


def inBoard(x, y, boardSize):
    return 0 <= x < boardSize and 0 <= y < boardSize


def solution(board, boardSize, gap):
    answer = 0
    if board[gap][gap]:
        answer -= 1
    queue = deque([])
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i][j]:
                answer += 1
                board[i][j] = 0

                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if inBoard(x, y, boardSize) and board[nx][ny]:
                            board[nx][ny] = 0
                            queue.append((nx, ny))
    return answer


board = [[0]*boardSize for _ in range(boardSize)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = processCoords(x1, y1, x2, y2, gap)
    preProcess(board, x1, y1, x2, y2)
postProcess(board, boardSize)

print(solution(board, boardSize, gap))