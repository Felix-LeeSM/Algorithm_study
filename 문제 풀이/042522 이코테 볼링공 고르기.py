import collections
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
balls = map(int, input().split())
sheet = collections.Counter(balls)
ans = 0
items = sheet.items()
for i in range(len(items)):
    for j in range(i+1, len(items)):
        ans += items[i][1]*items[j][1]
print(ans)
