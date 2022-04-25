import sys
input = sys.stdin.readline
N = int(input())
coins = sorted(list(map(int, input().split())))
check = 1
for coin in coins:
    if coin > check:
        print(check+1)
        break
    check += coin