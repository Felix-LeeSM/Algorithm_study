# https://school.programmers.co.kr/learn/courses/30/lessons/388354


from typing import List, Tuple


def parse_tree(graph: List[List[int]], entry: int, visited: List[bool]) -> Tuple[int, int]:
    # 숫자 홀짝, 자식 홀짝
    odd_odd = []
    odd_even = []
    even_odd = []
    even_even = []

    stack = [entry]
    visited[entry] = True

    while stack:
        node = stack.pop()
        if node % 2:
            if len(graph[node]) % 2:
                odd_even.append(node)
            else:
                odd_odd.append(node)
        else:
            if len(graph[node]) % 2:
                even_even.append(node)
            else:
                even_odd.append(node)

        for child in graph[node]:
            if visited[child]:
                continue

            visited[child] = True
            stack.append(child)

    return (+(len(even_odd) + len(odd_even) == 1), +(len(odd_odd) + len(even_even) == 1))


def solution(nodes: List[int], edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    graph = [[] for _ in range(1_000_001)]
    visited: List[bool] = [False] * 1_000_001

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    odd_even = 0
    rev_odd_even = 0

    for node in nodes:
        if visited[node]:
            continue

        oe, roe = parse_tree(graph, node, visited)
        odd_even += oe
        rev_odd_even += roe

    return [odd_even, rev_odd_even]


assert solution([9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]]) == [1, 0]
assert solution([9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10], [[5, 14], [1, 4], [
                9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]) == [2, 1]
