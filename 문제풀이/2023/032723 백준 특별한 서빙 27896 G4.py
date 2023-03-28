from heapq import heappop, heappush
from sys import argv, maxsize as INF, stdin
input = stdin.readline
A, B = 'A', 'B'


class MaxHeap(list):
    def hPush(self, x):
        heappush(self, -x)

    def hPop(self):
        return -heappop(self)


def solution(N: int, M: int, sads: list[int]) -> int:
    heap = MaxHeap()
    curSad = 0
    cnt = 0

    for sad in sads:
        curSad += sad
        heap.hPush(sad)

        while curSad >= M:
            cnt += 1
            curSad -= 2*heap.hPop()

    return cnt


def main(*args: list[str]) -> int:
    N, M = map(int, input().split())
    sads = list(map(int, input().split()))

    answer = solution(N, M, sads)
    print(answer)
    return 1


if __name__ == '__main__':
    main(*argv)
