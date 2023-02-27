from array import array
from itertools import chain, repeat
from sys import argv, maxsize, stdin
input = stdin.readline

UPDATE, QUERY = 1, 2


def solution(N: int, nums: list[int], queries: list[tuple[int, int, int]]) -> str:
    tree = array('L', chain(repeat(0, N), nums))

    for i in range(N-1, 0, -1):
        tree[i] = min(tree[2*i], tree[2*i+1])

    for type, a, b in queries:
        if type == UPDATE:
            idx = N+a-1
            tree[idx] = b
            idx //= 2
            while idx:
                tree[idx] = min(tree[2*idx], tree[2*idx+1])
                idx //= 2

        elif type == QUERY:
            init = N+a-1
            fin = N+b-1
            ans = maxsize
            while init <= fin:
                if init % 2:
                    ans = min(ans, tree[init])
                    init += 1
                if not fin % 2:
                    ans = min(ans, tree[fin])
                    fin -= 1
                init //= 2
                fin //= 2
            print(ans)


def main(args=argv) -> int:
    N = int(input())
    nums = map(int, input().split())
    M = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    solution(N, nums, queries)
    return 1


if __name__ == '__main__':
    main()
