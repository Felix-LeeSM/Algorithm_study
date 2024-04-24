from collections import deque, defaultdict
from sys import maxsize


def solution(edges, target):
    graph = defaultdict(deque)

    for par, child in edges:
        graph[par].append(child)
    for key in graph.keys():
        graph[key] = deque(sorted(graph[key]))

    stackeds = [[] for _ in range(len(edges) + 2)]
    done = [True] + [target[i] == 0 for i in range(len(target))]
    req = sum(map(lambda x: not x, done))

    for turn in range(maxsize):
        node = traverse(graph, 1)
        stackeds[node].append(turn)
        if is_too_much(stackeds[node], target[node - 1]):
            return [-1]
        if not done[node]:
            is_done = is_ok(stackeds[node], target[node - 1])
            if is_done:
                req -= 1
                done[node] = True

                if req == 0:
                    result = [1] * (turn + 1)
                    for stack, tar in zip(stackeds[1:], target):
                        if not tar:
                            continue

                        diff = tar - len(stack)
                        curr = [1] * len(stack)
                        idx = len(stack) - 1

                        while diff:
                            if curr[idx] == 3:
                                idx -= 1
                            curr[idx] += 1
                            diff -= 1

                        for turn, value in zip(stack, curr):
                            result[turn] = value

                    return result


def is_ok(stack, target):
    return len(stack) <= target <= len(stack) * 3


def is_too_much(stack, target):
    return len(stack) > target


def traverse(graph, node):
    while True:
        if not graph[node]:
            return node
        children = graph[node]
        node = children[0]
        children.rotate(-1)
