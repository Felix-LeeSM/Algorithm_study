'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
예를 들어 수열 [1, 1, 2, 2, 2, 2, 3]이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받습니다.

입력 예시
7 2
1 1 2 2 2 2 3
출력 예시
4

입력 예시
7 4
1 1 2 2 2 2 3
출력 예시
-1
'''
N, X = map(int, input().split())
nums = list(map(int, input().split()))


def bs_l(N, X, nums):
    lo, hi = 0, N

    while lo < hi:
        mid = (lo+hi)//2
        if nums[mid] >= X:
            hi = mid-1
        else:
            lo = mid+1
    return lo


def bs_r(N, X, nums):
    lo, hi = 0, N

    while lo < hi:
        mid = (lo+hi)//2
        if nums[mid] > X:
            hi = mid-1
        else:
            lo = mid+1
    return lo


def solution(N, X, nums):
    answer = bs_r(N, X, nums) - bs_l(N, X, nums)
    return answer if answer else -1


print(solution(N, X, nums))
