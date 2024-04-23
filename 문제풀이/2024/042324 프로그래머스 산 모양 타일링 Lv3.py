# 하나를 더 이어붙일 때,
#   공유하는 하나의 삼각형이 이전의 모양에서 이미 마름모로 쓰인 경우가 prison,
#   그렇지 않고 자유로운 경우가 free이다.


def solution(n, tops):
    free = 2 if tops[0] == 0 else 3
    prison = 1

    for top in tops[1:]:
        if top == 0:
            free, prison = (2 * free + prison) % 10007, (free + prison) % 10007
        else:
            free, prison = (
                3 * free + 2 * prison) % 10007, (free + prison) % 10007

    return (free + prison) % 10007
