# 각 케이스를 따로 계산하지 않고, 가중치를 계산한다.

from collections import defaultdict as ddict, Counter
from functools import reduce
from itertools import combinations as comb


def solution(arr_dice):
    n = len(arr_dice)

    curr_max = 0

    arr_dice = [Counter(dice) for dice in arr_dice]

    for a_dice in comb([(idx, dice) for idx, dice in enumerate(arr_dice, 1)], n // 2):

        a_dice = [dice for dice in a_dice]
        a_dice_idxs = [idx for idx, _ in a_dice]
        a_dice = [dice for _, dice in a_dice]
        b_dice = [i for i in arr_dice if i not in a_dice]

        a_weights = reduce(accum_counter, a_dice).items()
        b_weights = reduce(accum_counter, b_dice).items()

        wins = 0
        for a_point, a_weight in a_weights:
            for b_point, b_weight in b_weights:
                if a_point > b_point:
                    wins += a_weight * b_weight

        if wins > curr_max:
            answer = a_dice_idxs
            curr_max = wins

    return answer


def accum_counter(a, b):
    cache = ddict(int)
    for ak, av in a.items():
        for bk, bv in b.items():
            cache[ak + bk] += av * bv
    return cache


ans = solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])
print(ans)
