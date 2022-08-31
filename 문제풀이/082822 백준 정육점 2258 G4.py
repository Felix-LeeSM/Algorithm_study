'''
정육점 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	4131	688	483	16.159%
문제
은혜는 정육점에서 고기를 사려고 한다.
보통 정육점에서는 자신이 원하는 양을 이야기하면 그 양만큼의 고기를 팔지만,
은혜가 방문한 정육점에서는 세일 행사를 하고 있었기 때문에 N 덩어리의 고기를 이미 잘라놓고 판매하고 있었다.

각각의 덩어리들은 이미 정해져 있는 무게와 가격이 있는데, 
어떤 덩어리를 샀을 때에는 그 덩어리보다 싼 고기들은 얼마든지 덤으로 얻을 수 있다(추가 비용의 지불 없이).
또한 각각의 고기들은 부위가 다를 수 있기 때문에 비용과 무게와의 관계가 서로 비례하는 관계가 아닐 수도 있다.
은혜는 이러한 점을 고려하지 않고, 어느 부위든지 자신이 원하는 양만 구매하면 되는 것으로 가정한다. 
또한 만약 가격이 더 싸다면 은혜가 필요한 양보다 더 많은 고기를 살 수도 있다.

각 덩어리에 대한 정보가 주어졌을 때, 은혜가 원하는 양의 고기를 구매하기 위해 필요한 최소 비용을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 100,000), M(1 ≤ M ≤ 2,147,483,647)이 주어진다. 
N은 덩어리의 개수를 의미하고, M은 은혜가 필요한 고기의 양이다. 
다음 N개의 줄에는 각 고기 덩어리의 무게와 가격을 나타내는 음 아닌 두 정수가 주어진다. 
무게의 총 합과 가격의 총 합은 각각 2,147,483,647을 넘지 않는다.

출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
4 9
1 2
2 4
3 6
4 8
예제 출력 1 
8
'''

# https://www.acmicpc.net/problem/2258

from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

meats, need = map(int, input().split())

weight_cost = [tuple(map(int, input().split())) for _ in range(meats)]

weight_cost.sort(key=lambda x: (x[1], -x[0]))

cur_weight = 0
cur_cost = 0
free = 0
cnt = 1
res1 = INF
res2 = INF

for idx, (weight, cost) in enumerate(weight_cost):
    if cost > cur_cost:
        cur_cost = cost
        free += cur_weight
        cur_weight = weight
        cnt = 1
    else:
        cur_weight += weight
        cnt += 1

    if cur_weight + free >= need:
        res1 = cur_cost*cnt

        for i in range(idx, len(weight_cost)):
            next_weight, next_cost = weight_cost[i]
            if next_cost > cur_cost:
                res2 = next_cost
                break

        print(min(res1, res2))

        break
else:
    print(-1)
    exit()
