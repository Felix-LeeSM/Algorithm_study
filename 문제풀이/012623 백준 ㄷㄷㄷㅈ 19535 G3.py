from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
input = stdin.readline


def main():
    try:
        nodes = int(input())
        graph = [[] for _ in range(nodes + 1)]
        for _ in range(nodes-1):
            fr, to = map(int, input().split())
            graph[fr].append(to)
            graph[to].append(fr)

        answer = solution(nodes, graph)

        print(answer)
        return 1

    except BaseException as e:
        print(e.__class__.__name__, e, 'Error Occured', sep='\n')

        return 0


def solution(nodes, graph):
    def dfs(node):
        nonlocal D, G, visited

        childs = len(graph[node])
        if childs >= 3:
            G += childs * (childs-1) * (childs-2) // 6

        for child in graph[node]:
            if visited[child]:
                continue

            visited[child] = True
            dfs(child)

            if childs >= 2 and len(graph[child]) >= 2:
                D += (childs-1) * (len(graph[child])-1)
    D = G = 0
    root = 1

    visited = [False]*(nodes+1)
    visited[root] = True
    dfs(1)

    if D < 3*G:
        return 'G'
    if D > 3*G:
        return 'D'
    return 'DUDUDUNGA'


main()
