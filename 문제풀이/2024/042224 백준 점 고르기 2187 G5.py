from functools import reduce
from sys import maxsize, stdin
input = stdin.readline

n, a, b = map(int, input().split())

dots = [tuple(map(int, input().split())) for _ in range(n)]


def max_gap(nums):
    min_num = maxsize
    max_num = -maxsize
    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    return max_num - min_num


answer = -maxsize

for (r, c, s) in dots:
    def in_right_down(x): return r <= x[0] < r + a and c <= x[1] < c + b

    weights_in_right_downs = map(lambda x: x[2], filter(in_right_down, dots))

    answer = max(answer, max_gap(weights_in_right_downs))

    def in_right_up(x): return r <= x[0] < r + a and c - b < x[1] <= c

    weights_in_right_ups = map(lambda x: x[2], filter(in_right_up, dots))

    answer = max(answer, max_gap(weights_in_right_ups))


print(answer)
