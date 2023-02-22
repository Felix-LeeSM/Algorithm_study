'''
행렬 곱셈 순서 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	21845	9978	7147	44.372%
문제
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 
행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 
행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 
모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 
입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 
정답은 231-1 보다 작거나 같은 자연수이다.
또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.

예제 입력 1 
3
5 3
3 2
2 6
예제 출력 1 
90

예제 입력 2
4
5 3
3 2
2 6
6 3
예제 출력 2
96

예제 입력 3
5
1 10
10 1
1 10
10 1
1 10
예제 출력 3
31

'''

# https://www.acmicpc.net/problem/11049

from collections import deque
from sys import stdin, maxsize
input = stdin.readline

n = int(input())
mtrx = deque([tuple(map(int, input().split())) for _ in range(n)])

dp = [[maxsize]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for interval in range(1, n):
    for start in range(n-interval):
        end = start+interval
        for mid in range(start, end):
            dp[start][end] = min(
                dp[start][end],
                dp[start][mid] + dp[mid+1][end] +
                mtrx[start][0] * mtrx[mid][1] * mtrx[end][1],
            )

print(dp[0][n-1])
