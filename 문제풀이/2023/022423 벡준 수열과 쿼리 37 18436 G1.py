from itertools import chain, repeat
from sys import argv, maxsize as INF, stdin
input = stdin.readline

UPDATE, QUERY_EVEN, QUERY_ODD = 1, 2, 3
enum = enumerate


def solution(N: int, nums: list[int], queries: list[tuple[int, int, int]]) -> str:
    odd_tree = list(chain(repeat(0, N), map(
        lambda x: x % 2, nums)))

    for i in range(N-1, 0, -1):
        odd_tree[i] = odd_tree[2*i] + odd_tree[2*i+1]

    for type, a, b in queries:
        if type == UPDATE:
            idx = N+a-1
            odd_tree[idx] = b % 2
            idx //= 2
            while idx:
                odd_tree[idx] = odd_tree[2*idx] + odd_tree[2*idx+1]
                idx //= 2

        else:
            init = N+a-1
            fin = N+b-1
            odds = 0
            while init <= fin:
                if init % 2:
                    odds += odd_tree[init]
                    init += 1
                if not fin % 2:
                    odds += odd_tree[fin]
                    fin -= 1
                init //= 2
                fin //= 2
            if type == QUERY_EVEN:
                print(b-a+1 - odds)
            elif type == QUERY_ODD:
                print(odds)


def main(args=argv) -> int:
    N = int(input())
    nums = map(int, input().split())
    M = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    solution(N, nums, queries)
    return 1


if __name__ == '__main__':
    main()
