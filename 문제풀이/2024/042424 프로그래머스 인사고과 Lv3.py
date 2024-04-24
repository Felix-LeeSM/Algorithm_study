from sys import maxsize


def solution(scores):
    me = sum(scores[0])
    scores = enumerate(scores)
    # a가 높은 순, b가 높은 순으로 정렬
    scores = sorted(scores, key=lambda x: (x[1][0], x[1][1]), reverse=True)
    is_valid = [True] * len(scores)

    curr_b_max = 0
    b_max = 0
    curr_a = maxsize

    for idx, (a, b) in scores:
        if curr_a != a:
            curr_a = a
            b_max = max(curr_b_max, b_max)
            curr_b_max = b

            if b < b_max:
                is_valid[idx] = False
                if idx == 0:
                    return -1
            continue

        else:
            if b < b_max:
                is_valid[idx] = False
                if idx == 0:
                    return -1

    scores = filter(lambda x: is_valid[x[0]], scores)
    scores = map(lambda x: sum(x[1]), scores)
    scores = sorted(scores, reverse=True)
    return scores.index(me) + 1


assert solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]) == 4
