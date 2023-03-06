from array import array
from itertools import repeat
from collections.abc import Iterable


class BIT:
    def __init__(self, N: int):
        self.N = N
        self.arr = array('l', repeat(0, N+1))
        self.tree = array('l', repeat(0, N+1))
        self.init = False

    def init_tree(self, nums: Iterable[int]):
        if self.init:
            raise Exception('Already initialized')

        self.init = True
        for i, num in enumerate(nums, 1):
            self.arr[i] = num
            self.update(i, num)

    def update(self, idx, dif):
        while idx <= self.N:
            self.tree[idx] += dif
            idx += (idx & -idx)

    def _accumulate(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= (idx & -idx)
        return result

    def query(self, start, end):
        return self._accumulate(end) - self._accumulate(start-1)


N = 100
arr = array('l', repeat(0, N+1))
tree = array('l', repeat(0, N+1))
ret = []


def update(idx, dif):
    while idx <= N:
        tree[idx] += dif
        idx += (idx & -idx)


def accum(idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= (idx & -idx)
    return result


def query(start, end):
    if end < start:
        return query(end, start)
    return accum(end) - accum(start-1)
