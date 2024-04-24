from collections import deque
from sys import maxsize


def solution(coin, cards):
    n = len(cards)
    hand = set(cards[:n//3])
    unused = set()
    cards = deque([cards[n//3 + i:n//3 + i+2] for i in range(0, 2*n//3, 2)])

    for turn in range(1, maxsize):
        if not cards:
            return turn

        done = False
        unused.update(cards.popleft())

        for card in hand:
            req = n + 1 - card
            if req in hand:
                hand.remove(card)
                hand.remove(req)
                done = True
                break

        if done:
            continue
        if not coin:
            return turn

        for card in hand:
            req = n + 1 - card
            if req in unused:
                unused.remove(req)
                hand.remove(card)
                coin -= 1
                done = True
                break

        if done:
            continue
        if coin <= 1:
            return turn

        for card in unused:
            req = n + 1 - card
            if req in unused:
                unused.remove(card)
                unused.remove(req)
                coin -= 2
                done = True
                break
        if not done:
            return turn

    return turn


assert solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]) == 5
assert solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]) == 2
assert solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]) == 4
assert solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18]) == 1
