from sys import setrecursionlimit, stdin

setrecursionlimit(10**6)


def max_val(tree, node, values, computed):
    values[node] = max(
        map(
            lambda node: (
                values[node]
                if computed[node]
                else min_val(tree, node, values, computed)
            ),
            tree[node],
        )
    )

    computed[node] = True
    return values[node]


def min_val(tree, node, values, computed):
    values[node] = min(
        map(
            lambda node: (
                values[node]
                if computed[node]
                else max_val(tree, node, values, computed)
            ),
            tree[node],
        )
    )

    computed[node] = True
    return values[node]


def main():
    data = stdin.read().strip().splitlines()
    nodes, root = map(int, data[0].split())

    graph = [[] for _ in range(nodes + 1)]
    for i in range(1, nodes):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)

    tree = [[] for _ in range(nodes + 1)]
    stack = [root]
    visited = [False] * (nodes + 1)
    visited[root] = True

    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                tree[node].append(nxt)
                stack.append(nxt)

    index = nodes
    l = int(data[index].strip())
    index += 1

    values = [0] * (nodes + 1)
    computed = [False] * (nodes + 1)

    for _ in range(l):
        node, val = map(int, data[index].split())
        index += 1
        values[node] = val
        computed[node] = True

    max_val(tree, root, values, computed)

    q = int(data[index].strip())
    index += 1
    results = []

    for _ in range(q):
        node = int(data[index].split()[0])
        index += 1
        results.append(str(values[node]))

    print("\n".join(results))


if __name__ == "__main__":
    main()
