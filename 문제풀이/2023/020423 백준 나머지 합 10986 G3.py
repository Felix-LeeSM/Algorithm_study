'''
나머지 합 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	21623	6372	4660	27.894%
문제
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

예제 입력 1 
5 3
1 2 3 1 2
예제 출력 1 
7
'''


from collections import defaultdict
from sys import stdin
input = stdin.readline


def solution(N, M, nums):
    answer = 0

    acc_sums = [0]
    for num in nums:
        acc_sums.append((acc_sums[-1] + num) % M)

    cache = defaultdict(int)
    for acc in acc_sums:
        cache[acc] += 1

    for acc, cnt in cache.items():
        answer += cnt * (cnt - 1) // 2
    return answer


def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    answer = solution(N, M, nums)
    print(answer)

    return 1


if __name__ == '__main__':
    main()
