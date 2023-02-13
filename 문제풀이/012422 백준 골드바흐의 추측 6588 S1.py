import sys
input = sys.stdin.readline


def make_sieve(n: int) -> list[bool]:
    sieve = [0] * 2 + [1] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if sieve[k]:
            sieve[k*2::k] = [0] * ((n - k) // k)
    return sieve


def main() -> int:
    sieve = make_sieve(1000000)
    primes = [i for i, j in enumerate(sieve) if j]
    while True:
        n = int(input())
        if not n:
            break

        for i in range(1, len(primes)):
            prime = primes[i]
            if prime >= n:
                print('Goldbach\'s conjecture is wrong.')
                break

            if sieve[n-prime]:
                print(f'{n} = {prime} + {n-prime}')
                break

    return 1


main()
