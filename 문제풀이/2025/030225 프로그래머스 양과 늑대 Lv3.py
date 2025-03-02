LAMB = 0
WOLF = 1


def solution(info, edges):

    lamb_tree = [[] for _ in range(len(info))]
    graph = [[] for _ in range(len(info))]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * len(info)
    visited[0] = True

    dfs(0, graph, visited, lamb_tree, info, [], 0)

    curr_lamb = 1
    curr_wolf = 0

    reachable = lamb_tree[0][:]

    def cnt_unvisited_nodes(wolves, visited_nodes):
        len = 0
        for wolf in wolves:
            if (1 << (wolf - 1)) & visited_nodes:
                continue
            len += 1
        return len

    visited_possibilities = set([0])
    possibilities = [(0, curr_wolf, curr_lamb, lamb_tree[0][:])]
    answer = 1

    while possibilities:

        visited_nodes, curr_wolf, curr_lamb, reachable = possibilities.pop()

        for node, wolves in reachable:
            wolves_req = cnt_unvisited_nodes(wolves, visited_nodes)

            if curr_wolf + wolves_req >= curr_lamb:
                answer = max(answer, curr_lamb)
                continue

            new_curr_lamb = curr_lamb + 1
            new_curr_wolf = curr_wolf + wolves_req
            new_visited_nodes = visited_nodes | (1 << (node - 1))

            for wolf in wolves:
                new_visited_nodes = new_visited_nodes | (1 << (wolf - 1))
            if new_visited_nodes not in visited_possibilities:
                visited_possibilities.add(new_visited_nodes)
                answer = max(answer, new_curr_lamb)

                possibilities.append(
                    (
                        new_visited_nodes,
                        new_curr_wolf,
                        new_curr_lamb,
                        reachable + lamb_tree[node],
                    )
                )

    return answer


def dfs(
    node,
    graph,
    visited,
    lamb_tree,
    info,
    prev_wolves,
    last_lamb,
):
    for next in graph[node]:
        if visited[next]:
            continue
        visited[next] = True

        if info[next] == WOLF:
            dfs(next, graph, visited, lamb_tree, info, prev_wolves + [next], last_lamb)
        elif info[next] == LAMB:
            lamb_tree[last_lamb].append((next, prev_wolves[:]))
            dfs(next, graph, visited, lamb_tree, info, [], next)
        else:
            raise NotImplementedError()


if __name__ == "__main__":
    assert 5 == solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
    assert 5 == solution(
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [
            [0, 1],
            [0, 2],
            [1, 3],
            [1, 4],
            [2, 5],
            [2, 6],
            [3, 7],
            [4, 8],
            [6, 9],
            [9, 10],
        ],
    )
