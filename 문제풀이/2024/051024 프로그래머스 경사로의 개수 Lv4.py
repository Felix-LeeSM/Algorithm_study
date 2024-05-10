from collections import defaultdict
from itertools import product


DIV = 1_000_000_007
VEC = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def multiply(size, matrix1, matrix2):
    ret = [[0]*size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                ret[i][j] = (ret[i][j] + matrix1[i][k]
                             * matrix2[k][j]) % DIV
    return ret


def n_square(k, matrix):
    size = len(matrix)
    temp = matrix
    cache = {1: matrix}

    for expo in map(lambda x: 2**x, range(1, 39)):
        if expo > k:
            break
        cache[expo] = multiply(size, cache[expo//2], cache[expo//2])

    k -= 1
    for expo in map(lambda x: 2 << x, range(38, -1, -1)):
        if expo > k:
            continue
        k -= expo
        temp = multiply(size, temp, cache[expo])

    return temp


def solution(grid, d, k):
    n, m = len(grid), len(grid[0])
    matrix = [[0]*n*m for _ in range(n*m)]
    NOW, NEXT = 0, 1

    for i, j in product(range(n), range(m)):
        queues = [defaultdict(int), defaultdict(int)]
        queues[NOW][(i, j)] = 1

        for incline in d:
            for (x, y), cnt in queues[NOW].items():
                for dx, dy in VEC:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or n <= nx or ny < 0 or m <= ny or grid[nx][ny] - grid[x][y] != incline:
                        continue

                    queues[NEXT][(nx, ny)] += cnt

            queues[NOW] = queues[NEXT]
            queues[NEXT] = defaultdict(int)

        for (x, y), cnt in queues[NOW].items():
            matrix[i*m+j][x*m+y] += cnt

    graph = n_square(k, matrix)

    return sum(sum(line) for line in graph) % DIV


assert solution([[3, 4, 6, 5, 3], [3, 5, 5, 3, 6], [5, 6, 4, 3, 6], [
    7, 4, 3, 5, 0]], [1, -2, -1, 0, 2], 2) == 16
assert solution([[3, 6, 11, 12], [4, 8, 15, 10],
                 [2, 7, 0, 16]], [1, -2, 5], 3) == 1
assert solution([[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1], [
    1, 0, 0]], [0, 0, 1, -1, 0, 0, 1, -1], 10) == 595737277
