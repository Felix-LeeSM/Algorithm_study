# https://www.acmicpc.net/problem/2042

from sys import argv, stdin
input = stdin.readline

UPDATE = 1
QUERY = 2


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


def update(seg_tree, idx, val, length, merge):
    def operation(node, left, right):
        # 나의 담당구역 left~right 사이에 target이 없는 경우 => 기존 값을 그대로 반환(변경 필요 x)
        if idx < left or idx > right:
            return seg_tree[node]
        # leaf node: 바꿀 idx 값 발견 => 값 변경
        if left == right:
            seg_tree[node] = val
            return seg_tree[node]

        mid = (right + left) // 2
        left_val = operation(node << 1, left, mid)
        right_val = operation((node << 1) + 1, mid + 1, right)
        seg_tree[node] = merge(left_val, right_val)
        return seg_tree[node]

    operation(1, 0, length-1)
    return seg_tree


def solution(N: int, M: int, K: int, nums: list[int], problems: list[tuple[int]]) -> int:
    def add(*args):
        return sum(args)
    sums_tree = build([0]*(4*N), nums, add)
    answer = []

    for operation, a, b in problems:
        if operation == UPDATE:
            update(sums_tree, a-1, b, N, add)
        elif operation == QUERY:
            answer.append(query(sums_tree, a-1, b-1, N, add, 0))

    return answer


def main(args=argv[1:]) -> int:
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    problems = [tuple(map(int, input().split())) for _ in range(M+K)]

    answer = solution(N, M, K, nums, problems)

    print(*answer, sep='\n')

    return 1


if __name__ == '__main__':
    main()
