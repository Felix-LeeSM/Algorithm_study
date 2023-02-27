from functools import reduce
from itertools import permutations
from sys import argv, maxsize as INF, stdin
input = stdin.readline

enum = enumerate


def get_edges(i, j, d):
    funcs = [
        lambda i, j, n: (i, j+n),
        lambda i, j, n: (i+n, j+d),
        lambda i, j, n: (i+d, j+d-n),
        lambda i, j, n: (i+d-n, j),
    ]
    for func in funcs:
        for n in range(d):
            yield func(i, j, n)


def solution(N: int, M: int, arr: list[list[int]], rotates: list[tuple[int, int, int]]) -> str:
    def rotate(arr, r, c, s):
        coords = list(get_edges(r, c, s*2))
        vals = []
        for i in range(-1, 8*s-1):
            x, y = coords[i]
            vals.append(arr[x][y])

        for next_val, (i, j) in zip(vals, coords):
            arr[i][j] = next_val

    def min_row_sum(acc, cur):
        return min(acc, sum(cur))

    ans = INF
    for trials in permutations(rotates, len(rotates)):
        arr_copy = [row[:] for row in arr]
        for r, c, s in trials:
            for cs in range(1, s+1):
                rotate(arr_copy, r-1-cs, c-1-cs, cs)
        ans = min(ans, reduce(min_row_sum, arr_copy, INF))

    return ans


def main(args=argv) -> int:
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rotates = [tuple(map(int, input().split())) for _ in range(K)]

    answer = solution(N, M, arr, rotates)
    print(answer)
    return 1


if __name__ == '__main__':
    main()
