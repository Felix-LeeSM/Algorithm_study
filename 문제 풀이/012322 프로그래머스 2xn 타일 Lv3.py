# 기본적으로 피보나치 수열과 유사한 형태이다.
# 다만, a0이 답이 0이 나와야 하나 연산을 할 때에는 1로 해줘야 맞게 나온다.


def solution(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    a0, a1 = 1, 1
    for i in range(1, n):
        a0, a1 = a1, (a0+a1)%1000000007
    return a1