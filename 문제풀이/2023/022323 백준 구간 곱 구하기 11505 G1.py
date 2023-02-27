'''
구간 곱 구하기 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	18787	6428	4699	32.616%
문제
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다.
만약에 1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다.
그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다.
M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다. 
그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데,
a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
예제 출력 1 
240
48
예제 입력 2 
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
예제 출력 2 
0
240
'''
# https://st-lab.tistory.com/241
# 모드 연산에서 나눗셈은 없다.
# 즉, 나눗셈이 아니라 곱셈을 이용해서 표현해야 한다.
# -> 어떤 수 a를 나누려고 할 때, 곱셈에 대한 a의 역원을 구하여 곱하면 된다.
# -> 곱셈의 항등원은 1이므로, a * n ≡ 1 (mod p)인 어떤 수 n을 찾아야 한다.
# 페르마의 소정리를 이용한다.
# 정수 a가 소수 p의 배수가 아니라면
# a^(p-1) ≡ 1 (mod p)
# -> a^(p-2) * a ≡ 1 (mod p)이다.
# 즉, a를 나누려면 a^(p-2)를 곱하면 된다.

# BIT(Binary Indexed Tree)에서 곱을 나타낼 경우,
# 0으로 update하게 되면 그 이후 곱으로는 이것을 원래대로 되돌릴 수 없다.
# 정확하게는, 트리에서 해당 노드들을 다시 만들어줘야 한다.
# 그러므로 0으로 update하는 경우는 무시해야 한다.
# -> 0으로 update하는 경우에 대해서는 따로 처리해줘야 한다.
# 0의 갯수에 대한 BIT를 따로 만들어서 처리해준다.
# https://www.acmicpc.net/problem/11505
from sys import argv, setrecursionlimit, stdin
input = stdin.readline
setrecursionlimit(10**6)
UPDATE, PRINT = 1, 2
MOD = 1000000007


def inverse(b):
    return pow(b, MOD-2, MOD)


def merge(a, b):
    return a * b % MOD


def solution(N: int, M: int, K: int, nums: list[int], queries: list[tuple[int, int, int]]) -> str:
    arr = [1] * (N+1)
    tree = [1] * (N+1)
    zeros = [0] * (N+1)
    zero_tree = [0] * (N+1)
    ret = []

    def update_zero(idx, dif):
        zeros[idx] += dif

        while idx <= N:
            zero_tree[idx] += dif
            idx += (idx & -idx)

    def accum_zero(idx):
        result = 0
        while idx > 0:
            result += zero_tree[idx]
            idx -= (idx & -idx)
        return result

    def query_zero(start, end):
        return accum_zero(end) - accum_zero(start-1)

    def update(idx, val):
        update_val = merge(inverse(arr[idx]), val)
        arr[idx] = val

        while idx <= N:
            tree[idx] = merge(tree[idx], update_val)
            idx += (idx & -idx)

    def accum(idx):
        result = 1
        while idx > 0:
            result = merge(result, tree[idx])
            idx -= (idx & -idx)
        return result

    def query(start, end):
        return merge(accum(end), inverse(accum(start-1)))

    for idx, num in enumerate(nums, 1):
        if num:
            update(idx, num)
        else:
            update_zero(idx, 1)

    for query_type, a, b in queries:
        if query_type == UPDATE:
            if b == 0 and zeros[a] == 1:
                continue
            elif b == 0:
                update_zero(a, 1)
                pass
            elif zeros[a] == 1:
                update_zero(a, -1)
                update(a, b)
            else:
                update(a, b)
        else:
            if query_zero(a, b):
                print(0)
            else:
                print(query(a, b))


def main(args=argv) -> int:
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    queries = [tuple(map(int, input().split())) for _ in range(M + K)]

    solution(N, M, K, nums, queries)
    return 1


if __name__ == '__main__':
    main()
