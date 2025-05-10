from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)


readline = stdin.readline

nodes, root, queries = map(int, readline().split())

graph = [[] for _ in range(nodes+1)]

for _ in range(nodes-1):
    one, two = map(int, readline().split())

    graph[one].append(two)
    graph[two].append(one)

visited = [False] * (nodes+1)

tree = [[] for _ in range(nodes+1)]


def make_tree(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            make_tree(next_node)
            tree[node].append(next_node)


make_tree(root)


children_counts = [0] * (nodes+1)


def count_child(node):
    children_count = 1

    for child in tree[node]:
        children_count += count_child(child)

    children_counts[node] = children_count

    return children_count


count_child(root)

answer = []
for _ in range(queries):
    node = int(readline())

    answer.append(children_counts[node])

print(*answer, sep="\n")
