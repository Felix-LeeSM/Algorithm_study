# 1번 문제와 2번 문제는 key값의 위치만 다르고 사실상 같다.

# 첫번째 풀이
import sys
input = sys.stdin.readline

coords = list()
for _ in range(int(input())):
    coords.append(tuple(map(int, input().split())))
coords.sort(key=lambda x:(x[0], x[1]))
for x, y in coords:
    print(x, y)

# 두번째 풀이

import sys
input = sys.stdin.readline
coords = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x:(x[0],x[1]))
for x, y in coords:
    print(x, y)

# 세번째 풀이

for x, y in sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x:(x[0],x[1])):
    print(x, y)

