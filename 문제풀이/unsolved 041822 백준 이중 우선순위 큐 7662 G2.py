'''
for _ in range(int(input())):
    max_heap = list()
    min_heap = list()
    nums = collections.defaultdict(int)
    length = 0
    for __ in range(int(input())):
        operation = input().split()
        if operation[0] == 'I':
            length += 1
            num = int(operation[1])
            nums[num] += 1
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        else:
            if length:
                if operation[1] == '1':
                    popped = heapq.heappop(max_heap)
                else:
                    popped = heapq.heappop(min_heap)
                nums[popped] -= 1
            else:
                continue
            length -= 1
            if not nums[popped]:
                del nums[popped]
    if length:
        if length == 1:
            popped = -1*heapq.heappop(max_heap)
            while not nums[popped]:
                popped = -1*heapq.heappop(max_heap)
            print(popped, popped)
        else:
            min_popped, max_popped = heapq.heappop(
                min_heap), -1*heapq.heappop(max_heap)
            while not nums[min_popped]:
                min_popped = heapq.heappop(min_heap)
            while not nums[max_popped]:
                max_popped = -1*heapq.heappop(max_heap)
            print(min_popped, max_popped)
    else:
        print('EMPTY')
'''

'''
반례
1
9
I 1
I 2
I 3
D -1
D -1
I -1
I -2
I -3
D 1

답: -1, -3
1과 2가 max_heap에서 빠지지 않아서 나중에 문제가 된다. 
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def solve():
    minq = []
    maxq = []
    pd = dict()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'I':
            v = int(cmd[1])
            if v in pd:
                pd[v] += 1
            else:
                pd[v] = 1
                if v >= 0:
                    heappush(maxq, -v)
                else:
                    heappush(minq, v)
        else:
            if not minq and not maxq:
                continue
            if cmd[1] == '1':
                if maxq:
                    v = -maxq[0]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        heappop(maxq)
                        pd.pop(v)
                else:
                    minq.sort()
                    v = minq[-1]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        pd.pop(v)
                        minq.pop()
            else:
                if minq:
                    v = minq[0]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        heappop(minq)
                        pd.pop(v)
                else:
                    maxq.sort()
                    v = -maxq[-1]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        pd.pop(v)
                        maxq.pop()
    if minq and maxq:
        print(-maxq[0], minq[0])
    elif minq:
        minq.sort()
        print(minq[-1], minq[0])
    elif maxq:
        maxq.sort()
        print(-maxq[0], -maxq[-1])
    else:
        print("EMPTY")


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
