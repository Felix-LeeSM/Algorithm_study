# https://www.acmicpc.net/problem/10868

from sys import argv, maxsize as INF, stdin
input = stdin.readline


def make_query(merge: callable, exception: int, nums: list[int]):
    def build(nums: list[int], merge: callable):
        def operation(node, left, right):
            if left == right:
                tree[node] = nums[left]
                return tree[node]

            mid = (left+right)//2
            left_val = operation(node << 1, left, mid)
            right_val = operation(1+(node << 1), mid+1, right)
            tree[node] = merge(left_val, right_val)
            return tree[node]

        tree = [0] * (4 * len(nums))
        operation(1, 0, len(nums)-1)
        return tree

    def query(start, end):
        def operation(node, left, right):
            if end < left or right < start:
                return exception
            if start <= left and right <= end:
                return tree[node]

            mid = (left+right)//2
            left_val = operation(node << 1, left, mid)
            right_val = operation(1+(node << 1), mid+1, right)
            return merge(left_val, right_val)

        return operation(1, 0, len(nums)-1)
    tree = build(nums, merge)

    return query


def solution(N: int, M: int, nums: list[int], problems: list[int]) -> int:
    answer = []
    query = make_query(min, INF, nums)
    for start, end in problems:
        answer.append(query(start-1, end-1))
    return answer


def main(args=argv) -> int:
    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    problems = [list(map(int, input().split())) for _ in range(M)]

    answer = solution(N, M, nums, problems)

    print(*answer, sep='\n')

    return 1


if __name__ == '__main__':
    main()
