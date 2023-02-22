'''
수들의 합 7 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	8892	2687	2152	30.353%
문제
N개의 수 A[1], A[2], …, A[N] 이 주어졌을 때, 함수 Sum(i, j)는 A[i] + A[i+1] + … + A[j]를 구하는 함수이다.
(i > j일 경우에는 A[j] + A[j+1] + ... + A[i]) A가 주어졌을 때, Sum(i, j)를 구하는 것은 매우 쉬운 문제이다. 
이러한 (i, j)가 여러 개 주어졌을 때도 별로 어려운 문제는 아니다.

Sum함수와 더불어 Modify라는 함수를 정의하자. Modify(i, k)를 수행하면 A[i] = k가 되는 함수이다. 
Sum함수와 Modify 함수의 사용 목록이 주어졌을 때, 이에 해당하는 연산을 하는 프로그램을 작성하시오. 
두 함수를 섞어서 사용할 수도 있다.

입력
첫째 줄에는 N(1 ≤ N ≤ 1,000,000), M(1 ≤ M ≤ 1,000,000)이 주어진다. 
M은 수행한 명령의 개수이며 다음 M개의 줄에는 수행한 순서대로 함수의 목록이 주어진다. 
첫 번째 숫자는 어느 함수를 사용했는지를 나타내며, 0일 경우에는 Sum 함수를, 1일 경우에는 Modify 함수를 나타낸다. 
다음 두 수는 각 함수의 인자 (i, j)나 (i, k)를 나타낸다. 처음에는 A[1] = A[2] = … = A[N] = 0이다. 
Modify인 경우에 1 ≤ k ≤ 100,000 이다.

출력
Sum 함수의 개수만큼 각 줄에 Sum 함수의 리턴값을 출력한다.

예제 입력 1 
3 5
0 1 3
1 1 2
1 2 3
0 2 3
0 1 3
예제 출력 1 
0
3
5
'''

from array import array
from itertools import repeat
from sys import argv, stdin
input = stdin.readline

SUM, MODIFY = 0, 1


def solution(N: int, nums: list[int], queries: list[tuple[int, int, int, int]]) -> str:
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

    for oper, a, b in queries:
        if oper == MODIFY:
            update(a, b-arr[a])
            arr[a] = b
        elif oper == SUM:
            ret.append(query(a, b))

    return ret


def main(args=argv) -> int:
    N, M = map(int, input().split())
    nums = array('l', repeat(0, N+1))
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    answer = solution(N, nums, queries)
    for line in answer:
        print(line)
    return 1


if __name__ == '__main__':
    main()
