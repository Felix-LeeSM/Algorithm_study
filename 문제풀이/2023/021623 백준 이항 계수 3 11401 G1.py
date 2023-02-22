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
from sys import argv, stdin
input = stdin.readline
MOD = 1_000_000_007


def solution(N: int, R: int) -> int:
    def pow(n: int, expo: int) -> int:
        ret = 1

        while expo > 0:
            if expo % 2 == 1:
                ret = (ret*n) % MOD

            n = (n**2) % MOD
            expo //= 2
        return ret

    factorial = [1]
    for i in range(1, N+1):
        factorial.append(factorial[-1]*i % MOD)

    return factorial[N] * pow(factorial[R], MOD-2) * pow(factorial[N-R], MOD-2) % MOD


def main(args=argv) -> int:
    N, R = map(int, input().split())

    answer = solution(N, R)

    print(answer)

    return 1


if __name__ == '__main__':
    main()
