'''
LCS 2 성공스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	256 MB	25925	9196	7106	38.471%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
ACAK
'''

# https://www.acmicpc.net/problem/9252

A = input()
B = input()

table = [['']*(len(B)+1) for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            table[i+1][j+1] = table[i][j]+A[i]
        else:
            table[i+1][j+1] = table[i][j +
                                       1] if len(table[i][j+1]) > len(table[i+1][j]) else table[i+1][j]

print(len(table[-1][-1]))
print(table[-1][-1])
