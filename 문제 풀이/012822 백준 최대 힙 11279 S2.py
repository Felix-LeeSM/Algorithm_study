# 파이썬의 heapq는 오직 최소힙만을 지원한다.
# 음수로 만들면, 최소 힙으로 최대힙을 구할 수 있다.
# 다만, 입=출력 시 다시 부호를 바꿔줘야 한다.

import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
length = 0

for _ in range(N):
    temp = -1 * int(input())
    if temp == 0:
        if length == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
            length -= 1
    else:
        heapq.heappush(heap, temp)
        length += 1

