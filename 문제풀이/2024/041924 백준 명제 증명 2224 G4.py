from collections import defaultdict
from sys import stdin
input = stdin.readline

cnt = int(input())

propositions = [input().rstrip().split(' => ') for _ in range(cnt)]

graph = defaultdict(list)

for fr, to in propositions:
    graph[fr].append(to)


answer = []
starts = {p[0] for p in propositions}

for fr in starts:
    stack = [fr]
    visited = set()
    while stack:
        node = stack.pop()

        if node in visited:
            continue

        if node != fr:
            answer.append((fr, node))

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

answer.sort(key=lambda x: (ord(x[0]), ord(x[1])))
answer = list(map(lambda x: ' => '.join(x), answer))

print(len(answer), *answer, sep='\n')
