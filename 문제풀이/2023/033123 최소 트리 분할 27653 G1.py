from collections import deque
from sys import argv, setrecursionlimit, stdin
setrecursionlimit(10**9)
input = stdin.readline


def solution(N: int, goals: list[int], graph: list[list[int]]) -> int:
    answer = 0
    tree = [[] for _ in range(N)]
    root = 1

    visited = [0] * (N+1)
    visited[root] = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = 1
            tree[node-1].append(child-1)
            queue.append(child)

    def dfs(node: int, befMax: int):

        if goals[node] > befMax:
            nonlocal answer
            answer += goals[node] - befMax

        for child in tree[node]:
            dfs(child, goals[node])

    dfs(0, 0)
    return answer


def main(*args: list[str]) -> int:
    N = int(input())
    graph = [[] for _ in range(N+1)]
    goals = list(map(int, input().split()))

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = solution(N, goals, graph)
    print(answer)
    return 1


if __name__ == '__main__':
    main(*argv)
