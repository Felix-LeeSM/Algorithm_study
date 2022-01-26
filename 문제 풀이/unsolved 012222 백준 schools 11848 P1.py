# 각 cities의 원소에서 [0]을 M회, [1]을 S회 선택하여 
# 최대값을 뽑아내는 문제.
# M과 S로 같은 원소르 선택할 수는 없다.

# max를 기준으로 정렬하면 될 것 같았지만... 너무 간단한 반례가 있었다.
# ------012222

import sys
cities = []
N, M, S = map(int, sys.stdin.readline().split())
for _ in range(N):
    cities.append(list(map(int, sys.stdin.readline().split())))
cities.sort(key=lambda x : -max(x))
for _ in range(N):
    ret = 0
    while M or S:
        m, s = cities.pop()
        if m > s: # 왼쪽이 더 큼
            if M > 0:
                ret += m
                M -= 1
        else:
            if S > 0:
                ret += s
                S -= 1
    print(ret)