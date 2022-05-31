'''
문제
수학 나라에 전쟁이 일어났다. 팩토리얼 진영과 거듭제곱 진영은 누가 수학 나라를 지배할 것인지 결정하기 위해 싸우고 있다.

팩토리얼 진영의 유명한 장군 n은 자기 자신을 팩토리얼 계산을 하면서 훈련을 하고 있고, 
거듭제곱진영의 제독 k는 자기 자신에 i제곱을 하기 위해 i를 만들고 있었다.

드디어 오늘은 n과 k가 싸우는 날이다. k는 n을 나누어서 작은 수로 만들어 버리기 위해서 몇 년동안 훈련을 진행하고 있었다.

이제 k는 n을 나누려고 한다. 훈련을 통해서 모두 성장했으므로, n!와 k**i와 싸우는 것이다.

이때, n!을 k**i로 나눌 수 있는 가장 큰 i를 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. (1 ≤ T ≤ 100) 
다음 T개의 줄에는 n과 k가 공백으로 구분되어 주어진다. (2 ≤ n ≤ 1018, 2 ≤  k ≤ 1012)

출력
각각의 테스트 케이스에 대해서, 가장 큰 i를 한 줄에 하나씩 출력한다.


예제 입력 1 
2
5 2
10 10

예제 출력 1 
3
2
'''
# 시간 초과가 난다...
# 소인수분해를 잘 하면 될 것 같은데...
# 에라토스테네스의 체는 10**9 기준 8기가바이트 메모리를 먹는다...
# 소인수분해는 매번 해줘야 하는 듯 하다.

import sys
import collections
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = sys.maxsize
    primes = collections.defaultdict(int)  # 소인수분해 결과  딕셔너리

    while not k % 2:
        primes[2] += 1
        k //= 2
    d = 3  # 소인수분해 해주기
    while d**2 <= k:
        while not k % d:
            primes[d] += 1
            k //= d
        d += 2
    else:
        if k != 1:
            primes[k] += 1

    for prime, expo in primes.items():  # 각각의 인수로 나눠보고, ans값 구하기
        cnt = 0
        x = prime**expo
        init = n//x
        while init:
            cnt += init
            init //= x
        ans = min(cnt, ans)

    print(ans)


# 에라토스테네스의 체는 10**9 기준 8기가바이트 메모리를 먹는다...
# 소인수분해는 매번 해줘야 하는 듯 하다.
'''
import sys
n_ks = []
max_k = -sys.maxsize

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    n_ks.append((n, k))
    max_k = max(max_k, k)

seive = [False, False] + [True] * (max_k - 1)
for l in range(2, int(max_k ** 0.5 + 1.5)):
    if seive[l]:
        seive[l*2::l] = [False] * ((max_k - l) // l)
seive = tuple([x for x in range(max_k+1) if seive[x]])


for n, k in n_ks:
    ans = sys.maxsize
    # k를 소인수분해 해야함.
    divisors = list()
    for p in seive:
        if p > k:
            break
        if k % p:
            continue

        # p로 나누어 떨어짐
        cut = 0
        while True:
            if k % p:
                break
            else:
                cut += 1
                k //= p
        divisors.append((p, cut))

    for prime, expo in divisors:
        x = prime**expo
        cnt = 0
        i = 1
        while n >= x**i:
            cnt += n // x**i
            i += 1
        ans = min(ans, cnt)
    print(ans)
'''
