from sys import stdin
def input(): return stdin.readline().rstrip()


parentheses = input()
stack = []
point_stack = [1]

points = {'(': 2, '[': 3, ')': 2, ']': 3}
pairs = {'(': ')', '[': ']'}
openers = ['(', '[']

temp = 1
crack = False

for p in parentheses:
    if p in openers:
        stack.append(p)
        temp *= points[p]
        point_stack.append(temp)
        continue

    if not stack or pairs[stack[-1]] != p:
        crack = True
        break

    temp //= points[p]
    stack.pop()
    point_stack.append(temp)


answer = 0
if not crack and not stack:
    for i, p in enumerate(point_stack[1:-1], 1):
        if point_stack[i] > point_stack[i-1] and point_stack[i] > point_stack[i+1]:
            answer += p


print(answer)
