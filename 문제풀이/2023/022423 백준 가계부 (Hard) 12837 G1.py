from array import array
from itertools import repeat
from sys import argv, maxsize as INF, stdin
input = stdin.readline

UPDATE, QUERY = 1, 2
enum = enumerate


def solution(N: int,  queries: list[tuple[int, int, int]]) -> str:
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

    for type, a, b in queries:
        if type == UPDATE:
            update(a, b)

        elif type == QUERY:
            print(query(a, b))


def main(args=argv) -> int:
    N, M = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    solution(N, queries)
    return 1


if __name__ == '__main__':
    main()
