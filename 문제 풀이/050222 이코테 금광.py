'''
NxM 크기의 금광이 있습니다. 금광은 1x1 크기의 칸으로 나누어져 있으며 각 칸은 특정한 크기의 금이 들어 있습니다. 
채굴자는 처 번째 열부터 출발하여 ㄱ므을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 
이후에 m번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요

입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력 예시
19
16
'''

import sys
input = sys.stdin.readline

Test_cases = int(input())
for test_case in range(Test_cases):
    N, M = map(int, input().split())
    line = list(map(int, input().split()))
    board = []
    idx = 0
    for _ in range(0, M):
        board.append(line[idx::M])
        idx += 1
    for i in range(1, M):
        for j in range(3):
            board[i][j] += max(board[i-1][max(0, j-1):min(3, j+2)])
    print(max(board[-1]))
