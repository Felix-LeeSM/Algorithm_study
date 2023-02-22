# dests의 입력 사이즈가 10정도로 작아서 완전탐색 재귀함수로 구현하였다.
# 입력이 커질 경우에 어떻게 하는 것이 좋은 지에 대해서 추가적인 풀이가 있으면 좋을 듯.
# 아마도 그래프를 통해서 가장 깊은 그래프를 찾는 것이 좋을 수도..?



def solution(k, dests):
    for i in dests:
        if k >= i[0]:
            return max([1 + solution(k-dests[i][1], dests[:i] + dests[i+1:]) for i in range(len(dests)) if k - dests[i][0] >= 0])
    else:
        return 0
