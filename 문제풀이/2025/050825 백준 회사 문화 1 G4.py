def solve(n, bosses, applauses):

    tree = [[] for _ in range(n+1)]

    for employee, boss in enumerate(bosses, start=1):
        if boss == -1:
            continue

        tree[boss].append(employee)

    def dfs(node, tree, applauses, curr_weight):
        applauses[node] += curr_weight

        for child in tree[node]:
            dfs(child, tree, applauses, applauses[node])

    dfs(1, tree, applauses, 0)

    return applauses[1:]


if __name__ == '__main__':
    from sys import stdin, setrecursionlimit
    setrecursionlimit(1_000_000)

    input = stdin.readline

    n, m = map(int, input().split())

    bosses = list(map(int, input().split()))

    applauses = [0] * (n+1)
    for _ in range(m):
        employee, weight = map(int, input().split())
        applauses[employee] += weight

    print(*solve(n, bosses, applauses))
