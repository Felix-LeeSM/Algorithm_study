'''
두 배열의 합 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	64 MB	18009	5966	3967	30.685%
문제
한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 
이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 
각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때,
A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

T(=5) = A[1] + B[1] + B[2]
      = A[1] + A[2] + B[1]
      = A[2] + B[3]
      = A[2] + A[3] + B[1]
      = A[3] + B[1] + B[2]
      = A[3] + A[4] + B[3]
      = A[4] + B[2] 
입력
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 
다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 
다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 
각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.

출력
첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.

예제 입력 1 
5
4
1 3 1 2
3
1 3 2
예제 출력 1 
7
'''

# https://www.acmicpc.net/problem/2143

from collections import defaultdict
from sys import stdin
input = stdin.readline

T = int(input())
A_N = int(input())
A = list(map(int, input().split()))
B_N = int(input())
B = list(map(int, input().split()))

for idx in range(1, A_N):
    A[idx] += A[idx-1]
for idx in range(1, B_N):
    B[idx] += B[idx-1]

A.append(0)
B.append(0)

sheet_A = defaultdict(int)

for i in range(-1, A_N):
    for j in range(i+1, A_N):
        sheet_A[A[j]-A[i]] += 1

pos = 0
for i in range(-1, B_N):
    for j in range(i+1, B_N):
        pos += sheet_A[T - (B[j]-B[i])]

print(pos)
