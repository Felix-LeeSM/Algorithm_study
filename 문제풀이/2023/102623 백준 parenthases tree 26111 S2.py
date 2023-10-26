# https://www.acmicpc.net/problem/26111

from sys import stdin
input = stdin.readline

parens = input().rstrip()

answer = 0
dist = 0
leaf = True

for idx, p in enumerate(parens):
    if p == "(":
        dist += 1
        leaf = True
        continue

    dist -= 1
    if leaf:
        leaf = False
        answer += dist

print(answer)
