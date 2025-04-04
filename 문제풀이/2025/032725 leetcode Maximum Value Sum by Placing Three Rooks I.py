from heapq import heappop, heappush
from itertools import combinations
from sys import maxsize
from typing import List, Self


class Solution:
    def maximumValueSum(self: Self, board: List[List[int]]) -> int:

        cntr = [[0] * len(board[0]) for _ in range(len(board))]
        for i, line in enumerate(board):
            q = []
            for j, num in enumerate(line):
                if 3 <= len(q) and q[0][0] < num:
                    heappop(q)
                if len(q) < 3:
                    heappush(q, (num, i, j))

            for _, i, j in q:
                cntr[i][j] += 1

        candidates = []

        for j in range(len(board[0])):
            line = [board[i][j] for i in range(len(board))]
            q = []
            for i, num in enumerate(line):
                if 3 <= len(q) and q[0][0] < num:
                    heappop(q)
                if len(q) < 3:
                    heappush(q, (num, i, j))

            for num, i, j in q:
                if cntr[i][j]:
                    if 11 <= len(candidates) and candidates[0][0] < num:
                        heappop(candidates)
                    if len(candidates) < 11:
                        heappush(candidates, (num, i, j))

        ret = -maxsize

        for i, j, k in combinations(candidates, 3):
            if i[1] != j[1] and i[1] != k[1] and j[1] != k[1]:
                if i[2] != j[2] and i[2] != k[2] and j[2] != k[2]:
                    ret = max(ret, i[0] + j[0] + k[0])

        return ret


assert 15 == Solution().maximumValueSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


assert 4 == Solution().maximumValueSum([
    [-3, 1, 1, 1],
    [-3, 1, -3, 1],
    [-3, 2, 1, 1]
])


assert 3 == Solution().maximumValueSum([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
