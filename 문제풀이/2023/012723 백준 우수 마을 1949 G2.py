from sys import maxsize, stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline
INF = maxsize
YES, NO = 0, 1
TRUE, FALSE = 1, 0


def solution(N, citizens, graph):
    root = 1
    dp = [[0, 0] for _ in range(N+1)]
    visited = [FALSE] * (N+1)

    dfs(root, graph, citizens, dp, visited)

    print(dp)
    return max(dp[root])


def dfs(node, graph, citizens, dp, visited):
    visited[node] = TRUE

    for child in graph[node]:
        if visited[child]:
            continue
        dfs(child, graph, citizens, dp, visited)

        dp[node][YES] += dp[child][NO]
        dp[node][NO] += max(dp[child])

    dp[node][YES] += citizens[node]


def main():
    N = int(input())
    citizens = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        fr, to = map(int, input().split())
        graph[fr].append(to)
        graph[to].append(fr)

    answer = solution(N, citizens, graph)
    print(answer)

    return 1


if __name__ == '__main__':
    assert solution(7, [0, 1000, 3000, 4000, 1000, 2000, 2000, 7000], [
                    [], [2], [1, 3, 6], [2, 4], [3, 5], [4], [2, 7], [6]]) == 14000
    assert solution(6, [0, 10, 1, 1, 1, 10, 10], [
                    [], [2], [1, 3], [2, 4, 6], [3, 5], [4], [3]]) == 30

    main()
