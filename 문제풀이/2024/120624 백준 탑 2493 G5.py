from sys import stdin
input = stdin.readline

n = int(input())
towers = list(map(int, input().split()))

stack = []
answer = [0] * n

for i in range(n-1, -1, -1):
    tower = towers[i]

    while stack:
        last, idx = stack[-1]
        if last <= tower:
            stack.pop()
            answer[idx] = i+1
        else:
            break

    stack.append((tower, i))

print(*answer)
