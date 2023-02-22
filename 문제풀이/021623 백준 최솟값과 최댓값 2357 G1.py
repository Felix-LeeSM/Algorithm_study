# https://www.acmicpc.net/problem/2357
from sys import argv, maxsize, stdin
input = stdin.readline


def build(seg_tree, nums, merge):
    def operation(node, left, right):
        if left == right:
            seg_tree[node] = nums[left]
            return seg_tree[node]

        mid = (right + left) // 2
        left_val = operation(node << 1, left, mid)
        right_val = operation((node << 1) + 1, mid + 1, right)
        seg_tree[node] = merge(left_val, right_val)
        return seg_tree[node]

    operation(1, 0, len(nums)-1)
    return seg_tree


def query(seg_tree, start, end, length, merge, exception):
    def operation(node, left, right):
        # 나의 담당구역 left~right 사이에 start~end 가 아예 포함되지 않는 경우 => 가지 치기
        if end < left or start > right:
            return exception

        # 나의 담당구역 left~right 전체가 start~end 에 포함되는 경우 => 내 정보를 바로 리턴
        if start <= left and right <= end:
            return seg_tree[node]

        mid = (right + left) // 2
        left_val = operation(node << 1, left, mid)
        right_val = operation((node << 1) + 1, mid + 1, right)
        return merge(left_val, right_val)

    return operation(1, 0, length-1)


def solution(N: int, M: int, nums: list[int], problems: list[tuple[int]]) -> int:
    mins = build([maxsize]*(4*N), nums, min)
    maxs = build([-maxsize]*(4*N), nums, max)

    return [(query(mins, a-1, b-1, N, min, maxsize),
             query(maxs, a-1, b-1, N, max, -maxsize)) for a, b in problems]


def main(args=argv[1:]) -> int:
    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    problems = [tuple(map(int, input().split())) for _ in range(M)]

    answer = solution(N, M, nums, problems)

    for case in answer:
        print(*case)

    return 1


if __name__ == '__main__':
    main()
