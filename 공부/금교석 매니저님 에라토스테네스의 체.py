from typing import List
import sys
# 시간 복잡도 NloglogN이다.
# 대신 메모리를 돼지처럼 먹는다...
# 메모리가 많고 시간이 적을 떄 하면 될 듯..?


def primes_up_to_good(n: int) -> List[int]:
    seive = [0] * 2 + [1] * (n - 1)
    print(sys.getsizeof(seive))  # << 8기가
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [0] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]


a = primes_up_to_good(10**9)

print(sys.getsizeof(a))  # << 400메가
