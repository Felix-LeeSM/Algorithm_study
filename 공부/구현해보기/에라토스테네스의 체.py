def primes_up_to_good(n: int) -> list[int]:
    sieve = [0] * 2 + [1] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if sieve[k]:
            sieve[k*2::k] = [0] * ((n - k) // k)
    return [x for x in range(n+1) if sieve[x]]
