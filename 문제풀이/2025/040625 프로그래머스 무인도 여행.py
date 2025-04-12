from typing import List


def solution(maps: List[str]):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(maps), len(maps[0])

    maps = [
        [0 if char == 'X' else int(char) for char in line]
        for line in maps
    ]

    visited = [[False] * m for _ in range(n)]

    ret = []

    for x in range(n):
        for y in range(m):
            if maps[x][y] and not visited[x][y]:
                stack = [(x, y)]
                visited[x][y] = True
                area = maps[x][y]

                while stack:
                    i, j = stack.pop()

                    for di, dj in delta:
                        ni, nj = i + di, j + dj
                        if ni < 0 or n <= ni or nj < 0 or m <= nj:
                            continue
                        if visited[ni][nj]:
                            continue
                        if maps[ni][nj] == 0:
                            continue

                        area += maps[ni][nj]
                        visited[ni][nj] = True
                        stack.append((ni, nj))
                ret.append(area)

    return [i for i in sorted(ret)] if ret else [-1]


assert [1, 1, 27] == solution(["X591X", "X1X5X", "X231X", "1XXX1"])
assert [-1] == solution(["XXX", "XXX", "XXX"])
