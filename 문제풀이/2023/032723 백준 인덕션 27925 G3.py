from heapq import heappop, heappush
from sys import argv, maxsize as INF, stdin
input = stdin.readline
A, B = 'A', 'B'


def solution(N: int, foods: list[int]) -> int:
    def getDif(*nums):
        fr, to = sorted(nums)
        return min(to-fr, fr+10-to)

    def getNext(a, b, c, food):
        return [
            [*sorted([a, b, food]), getDif(c, food)],
            [*sorted([a, c, food]), getDif(b, food)],
            [*sorted([b, c, food]), getDif(a, food)]
        ]

    dp = [[[[INF]*10 for k in range(10)]
           for j in range(10)] for i in range(N)]
    queue = [(0, 0, 0, 0, 0)]

    while queue:
        cnt, idx, a, b, c = heappop(queue)
        if idx == N:
            return cnt

        for na, nb, nc, dif in getNext(a, b, c, foods[idx]):
            if dp[idx][na][nb][nc] > cnt+dif:
                dp[idx][na][nb][nc] = cnt+dif
                heappush(queue, (cnt+dif, idx+1, *sorted([na, nb, nc])))


def main(*args: list[str]) -> int:
    N = int(input())
    foods = list(map(int, input().split()))

    answer = solution(N, foods)
    print(answer)
    return 1


if __name__ == '__main__':
    main(*argv)
