# 기본적인 정렬문제.
# sys.stdin.readline() 함수를 써보았다.

import sys
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)