# 피보나치 수열 구현
# 파사드 주기 같은 개념도 있지만,
# 이 경우 input이 그렇게 크지 않다.
n = int(input())
a0, a1 = 1, 1
n -= 1
while n > 0:
    a0, a1 = a1, (a0+a1) % 10007
    n -= 1
print(a1)
