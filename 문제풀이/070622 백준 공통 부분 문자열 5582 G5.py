'''
공통 부분 문자열 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	12111	4913	3840	42.790%
문제
두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 
예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 
하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 
이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 
또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

입력
첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.

출력
첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.

예제 입력 1 
ABRACADABRA
ECADADABRBCRDARA
예제 출력 1 
5

예제 입력 2 
UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV
예제 출력 2 
0
'''

# https://www.acmicpc.net/problem/5582

A, B = input(), input()
a, b = len(A), len(B)
dp = [[0]*b for _ in range(a)]
ans = 0
for i in range(a):
    if A[i] == B[0]:
        dp[i][0] = 1
        ans = 1
for j in range(b):
    if A[0] == B[j]:
        dp[0][j] = 1
        ans = 1

for i in range(1, a):
    for j in range(1, b):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+1
            ans = max(dp[i][j], ans)

print(ans)
