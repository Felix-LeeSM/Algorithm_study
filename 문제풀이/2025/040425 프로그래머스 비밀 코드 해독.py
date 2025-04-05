from itertools import combinations


def solution(n, qs, answers):
    possibilities = combinations(range(1, n+1), 5)
    ret = 0

    for possibility in possibilities:
        curr = 0

        for q, ans in zip(qs, answers):
            if len(set(possibility) & set(q)) == ans:
                continue
            break
        else:
            ret += 1

    return ret


assert 3 == solution(10,
                     [
                         [1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10],
                         [3, 7, 8, 9, 10],
                         [2, 5, 7, 9, 10],
                         [3, 4, 5, 6, 7]
                     ],
                     [2, 3, 4, 3, 3])

assert 5 == solution(15,
                     [
                         [2, 3, 9, 12, 13],
                         [1, 4, 6, 7, 9],
                         [1, 2, 8, 10, 12],
                         [6, 7, 11, 13, 15],
                         [1, 4, 10, 11, 14]
                     ],
                     [2, 1, 3, 0, 1])
