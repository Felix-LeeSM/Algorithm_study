'''
스도쿠 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	11148	5436	4013	47.728%
문제
스도쿠는 매우 간단한 숫자 퍼즐이다. 
9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 
1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.



위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다. 
각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 
각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 
각 3×3짜리 사각형에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.

하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.

입력
9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

출력
9개의 줄에 9개의 숫자로 답을 출력한다.
답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다. 
즉, 81자리의 수가 제일 작은 경우를 출력한다.

제한
12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
C++17: 180ms
Java 15: 528ms
PyPy3: 2064ms
예제 입력 1 
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
예제 출력 1 
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
'''

# https://www.acmicpc.net/problem/2239

board = []
for i in range(9):
    board.append(list(map(int, list(input()))))

rows = [2**10-2]*9
cols = [2**10-2]*9
boxes = [[2**10-2]*3 for _ in range(3)]
temp = [(i, 2**i) for i in range(1, 10)]

for i in range(9):
    for j in range(9):
        if board[i][j]:
            num = 2**board[i][j]
            rows[i] ^= num
            cols[j] ^= num
            boxes[i // 3][j // 3] ^= num


def dfs(i, j):
    if i == 9:
        for line in board:
            print(*line, sep='')
        exit(0)

    ni, nj = (i + (j == 8), (j+1) % 9)

    if board[i][j]:
        return dfs(ni, nj)

    for ex, num in temp:
        if rows[i] & cols[j] & boxes[i // 3][j // 3] & num:
            rows[i] ^= num
            cols[j] ^= num
            boxes[i // 3][j // 3] ^= num
            board[i][j] = ex

            dfs(ni, nj)

            board[i][j] = 0
            rows[i] |= num
            cols[j] |= num
            boxes[i // 3][j // 3] |= num


dfs(0, 0)
