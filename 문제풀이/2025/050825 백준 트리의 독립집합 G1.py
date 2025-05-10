# https://www.acmicpc.net/problem/2213
from sys import stdin
input = stdin.readline


def solve(n, weights, graph):

    def dfs(node, parent):
        check_val, uncheck_val = weights[node], 0
        check_nodes, uncheck_nodes = [node], []

        for child in graph[node]:
            if child == parent:
                continue

            child_check, child_uncheck, child_check_nodes, child_uncheck_nodes =\
                dfs(child, node)

            check_val += child_uncheck
            check_nodes.extend(child_uncheck_nodes)

            if child_uncheck < child_check:
                uncheck_val += child_check
                uncheck_nodes.extend(child_check_nodes)
            else:
                uncheck_val += child_uncheck
                uncheck_nodes.extend(child_uncheck_nodes)

        return check_val, uncheck_val, check_nodes, uncheck_nodes

    root_check, root_uncheck, root_check_nodes, root_uncheck_nodes = dfs(1, 0)

    if root_uncheck <= root_check:
        return root_check, root_check_nodes
    return root_uncheck, root_uncheck_nodes


n = int(input())
weights = [0]
weights.extend(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    one, two = map(int, input().split())

    graph[one].append(two)
    graph[two].append(one)


weight, nodes = solve(n, weights, graph)

print(weight)
print(*sorted(nodes))
