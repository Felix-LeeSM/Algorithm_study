'''
1로 만들기 2 성공스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	15020	6933	5676	47.822%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 
정답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
2
예제 출력 1 
1
2 1

예제 입력 2 
10
예제 출력 2 
3
10 9 3 1
'''

from collections import deque
from sys import maxsize
INF = maxsize

n = int(input())
dp = [INF]*(1 + 10**6)
paths = [i for i in range(1+10**6)]
dp[n] = 0

queue = deque()
queue.append(n)

while queue:
    number = queue.popleft()
    if number == 1:
        break

    if number//3 and number % 3 == 0 and dp[number//3] > dp[number]+1:
        dp[number//3] = dp[number]+1
        paths[number//3] = number
        queue.append(number//3)

    if number//2 and number % 2 == 0 and dp[number//2] > dp[number]+1:
        dp[number//2] = dp[number]+1
        paths[number//2] = number
        queue.append(number//2)

    if number > 1 and dp[number-1] > dp[number]+1:
        dp[number-1] = dp[number]+1
        paths[number-1] = number
        queue.append(number-1)

print(dp[1])
path = [1]
cur = 1

while paths[cur] != cur:
    path.append(paths[cur])
    cur = paths[cur]

print(*reversed(path))
