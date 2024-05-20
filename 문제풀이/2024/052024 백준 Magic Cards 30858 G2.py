
from collections import defaultdict
from sys import stdin
input = stdin.readline


def solution(N, K, M, F, cards, queries):
    cards_str = [['N']*K for _ in range(N+1)]

    for card_no, card in enumerate(cards):
        for num in card:
            cards_str[num][card_no] = 'Y'

    memo = defaultdict(int)
    for num in range(1, N+1):
        s = ''.join([cards_str[num][i] for i in range(K)])

        if s in memo:
            memo[s] = 0
        else:
            memo[s] = num

    ret = [memo[query] for query in queries]
    return ret


def main():
    N, K, M, F = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(K)]
    queries = [input().rstrip() for _ in range(F)]

    print(*solution(N, K, M, F, cards, queries), sep="\n")

    return 0


if __name__ == '__main__':
    main()
