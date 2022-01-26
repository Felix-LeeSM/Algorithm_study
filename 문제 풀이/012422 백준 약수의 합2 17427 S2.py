# 최초의 코드.
# 모든 숫자에 대해서 각각의 약수의 합을 구한다.
# 당연한듯 시간초과.
'''
import sys

def operator(num):
    temp = 0
    for j in range(1, num+1):
        if not num%j:
            temp += j
    return temp

n = int(sys.stdin.readline())
ans = 0
for i in range(1, n+1):
    ans += operator(i)
print(ans)
'''
# 그 이후 작성한 코드.
# 각각의 숫자에 대해서 약수이면 더하기만 해준다.

# 아이디어는, 각각의 수에 대해서 모든 숫자를 한바퀴씩 돌리고, 더해주는 것이었다. 
# 뭐가 맞을 지 모르겠다.

# 아무튼, 시간초과.
# 한 바퀴에 해결할 수 있을 지 탐색해보자.

'''
import sys

n = int(sys.stdin.readline())
temp = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if not i%j:
            temp += j
print(temp)
'''

# 약수에서 배수를 찾는다는 느낌으로의 접근

import sys

n = int(sys.stdin.readline())
temp = n
for i in range(2, n+1):
    temp += i*(n//i)
print(temp)