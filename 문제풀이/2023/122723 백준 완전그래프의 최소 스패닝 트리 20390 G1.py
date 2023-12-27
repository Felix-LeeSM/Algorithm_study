# 시간 / 메모리 제한으로 인해 C/C++ 와 Java11, 그리고 PyPy3 이외의 언어로는 정해로도 정답을 받을 수 있는 것이 보장되지 않는다.
# PyPy3 로 제출하면 정답이 나온다.
from sys import stdin, maxsize
input = stdin.readline


n = int(input())
a, b, c, d = map(int, input().split())
nums = list(map(int, input().split()))

a %= c
b %= c


def dist(n1, n2):
    if n1 > n2:
        return dist(n2, n1)
    return ((nums[n1] * a + nums[n2] * b) % c) ^ d


distances = [maxsize] * n
connected = [False] * n
last_connected = 0
answer = 0

for _ in range(n-1):
    connected[last_connected] = True

    min_dist = maxsize
    min_dist_idx = 0

    for next in range(n):
        if connected[next]:
            continue

        curr_dist = dist(last_connected, next)

        if curr_dist < distances[next]:
            distances[next] = curr_dist

        if min_dist > distances[next]:
            min_dist = distances[next]
            min_dist_idx = next

    connected[min_dist_idx] = True
    last_connected = min_dist_idx
    answer += min_dist

print(answer)
