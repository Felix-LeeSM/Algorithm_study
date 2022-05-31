# is_prime 함수가 불안하긴 하다. 
# 다만, 6 이상의 짝수만 들어오므로 그냥 이용함.
# 입력은 짝수만 들어오고, 2를 포함하는 경우는 다른 수도 짝수가 되어야 하므로 2는 무시한다.
# for i in range(3, n, 2)에서 간격을 2로 둔다.



import sys

def is_prime(num):
    for k in range(2, int(num**0.5+1)):
        if not num%k:
            return False
    else:
        return True

while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    for i in range(3, n, 2):
        if is_prime(i) and is_prime(n-i):
            print('{0} = {1} + {2}'.format(n, i, n-i))
            break