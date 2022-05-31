'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

<<입출력 예제>>
예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
'''
A = input()
B = input()

table = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            table[i+1][j+1] = table[i][j]+1
        else:
            table[i+1][j+1] = max(table[i][j+1], table[i+1][j])

print(table[-1][-1])

# 문제 해설
# 예를 들어 aasdfg와 odsdfg를 비교하는 경우,
# aasdfg, odsdf // aasdf, odsdf + 1 // aasdf, odsdfg 이렇게 3가지를 비교하는 경우가 된다.
# 다만 마지막 문자열이 이 경우에는 일치하므로 무조건 중앙으로 가는 것이 더 큰 값이다.
# 풀이에서는 이 점이 대각선으로 1 값을 더한 값을 받는 것으로 구현되었다.
# 그 외의 경우에는 두가지 중의 max치를 받아오면 된다.
