# heapq 모듈로 날먹했다...
# heap 자료구조 구현에 대한 고민을 해야 할 듯 하다.


import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
length = 0 # 매번 len(heap) 하는 것이 손해일 것 같아서 따로 변수를 두었습니다.

for _ in range(N):
    temp = int(input())
    if temp == 0:
        if length == 0:
            print(0) # 뽑을 게 없으면 0을 출력합니다.
        else:
            print(heapq.heappop(heap))
            length -= 1 # 하나 뽑으면 길이를 하나 줄입니다. 0이 되면 상위 if문에서 걸립니다.
    else:
        heapq.heappush(heap, temp)
        length += 1 # 하나 push하고, 길이를 1 증가시킵니다.