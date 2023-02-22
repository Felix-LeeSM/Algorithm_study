'''
행렬 제곱 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	26882	9478	7526	34.124%
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

예제 입력 1 
2 5
1 2
3 4
예제 출력 1 
69 558
337 406
예제 입력 2 
3 3
1 2 3
4 5 6
7 8 9
예제 출력 2 
468 576 684
62 305 548
656 34 412
예제 입력 3 
5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
예제 출력 3 
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
'''
from sys import stdin
input = stdin.readline
DIVISOR = 1_000


def solution(N, M, matrix):
    temp = matrix
    cache = {1: matrix}

    for expo in map(lambda x: 2**x, range(1, 39)):
        if expo > M:
            break
        cache[expo] = square(N, cache[expo//2])

    M -= 1
    for expo in map(lambda x: 2**x, range(38, -1, -1)):
        if expo > M:
            continue
        M -= expo
        temp = multiply(N, temp, cache[expo])

    return temp


def square(N, matrix):
    return multiply(N, matrix, matrix)


def multiply(N, matrix1, matrix2):
    ret = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] = (ret[i][j] + matrix1[i][k]
                             * matrix2[k][j]) % DIVISOR
    return ret


def main():
    N, M = map(int, input().split())
    matrix = [list(map(lambda x: int(x) % DIVISOR, input().split()))
              for _ in range(N)]

    for line in solution(N, M, matrix):
        print(*line)

    return 1


if __name__ == '__main__':
    main()
