# 이 날 일을 한다, 안 한다로 나뉜다.
# knapsack과는 비슷한듯 다르다.

import sys
sys.setrecursionlimit = 10000
read = sys.stdin.readline

days = int(read())
works = [-1]
for i in range(1, days+1):
    works.append(tuple(map(int, read().split())))
    # 시간, 돈 순서


# def new_one(date, money):
#     if date > days:
#         return money
#     elif date == days:
#         if works[date][0] == 1:
#             return money + works[date][1]
#         else:
#             return money
#     else:
#         if date + works[date][0] - 1 > days:
#             return new_one(date+1, money)
#         else:
#             return max(new_one(date+1, money), new_one(date+works[date][0], money+works[date][1]))


# print(new_one(1, 0))


N = int(input())
works = [tuple(map(int, input().split())) for _ in range(N)]
money = [0]*(N+1)
for day in range(N):
    duration, wage = works[day]
    if day+duration > N:
        continue
    for each in range(day+duration, N+1):
        money[each] = max(money[day]+wage, money[each])
print(max(money))

# dp 풀이
