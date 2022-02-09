# 각 cities의 원소에서 [0]을 M회, [1]을 S회 선택하여
# 최대값을 뽑아내는 문제.
# M과 S로 같은 원소르 선택할 수는 없다.

# max를 기준으로 정렬하면 될 것 같았지만... 너무 간단한 반례가 있었다.
# ------012222

'''
<<예제 입출력>>
입력 1
3 1 1
5 2
4 1
6 4
출력 1
9

입력 2
7 2 3
9 8
10 6
3 5
1 7
5 7
6 3
5 4
출력 2
38



'''


import sys
cities = []
N, M, S = map(int, sys.stdin.readline().split())

cities = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

cities.sort(key=lambda x: (-max(x), -min(x)))
for _ in range(N):
    ret = 0
    while M or S:
        m, s = cities.pop()
        if m > s:  # 왼쪽이 더 큼
            if M > 0:
                ret += m
                M -= 1
        else:
            if S > 0:
                ret += s
                S -= 1
    print(ret)
