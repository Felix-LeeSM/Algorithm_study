'''
문제 설명
도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

image.png

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

제한사항
이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

입출력 예
money	
[1, 2, 3, 1]
return
4
'''


# DP이다
# table이 해당 지점까지 최대 돈이 된다.
# 원형 구조를 이루고 있어 첫집을 넣고 계산한 것과
# 첫 집을 빼고 계산한 것의 최대값을 구해야 한다.

def solution(money):
    # 첫 집 넣기
    table = [0]*len(money)
    table[0] = money[0]
    table[1] = max(money[0], money[1])
    for target in range(2, len(money)-1):
        table[target] = max(table[target-2]+money[target], table[target-1])
    maxi = table[-2]

    # 첫 집 빼기
    table = [0]*len(money)
    table[1] = money[1]
    for target in range(2, len(money)):
        table[target] = max(table[target-2]+money[target], table[target-1])
    maxi = max(maxi, table[-1])
    return maxi
