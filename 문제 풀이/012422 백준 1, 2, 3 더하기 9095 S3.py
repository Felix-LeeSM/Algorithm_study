# 재귀적으로 해결한다.
# key를 이용해서 더 짧은 코드를 구현하려 해봤다.

import sys

key = (-1, 1, 2, 4)
def operator(num):
    if num in (1, 2, 3):
        return key[num]
    else:
        return operator(num-1) + operator(num-2) + operator(num-3)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(operator(n))