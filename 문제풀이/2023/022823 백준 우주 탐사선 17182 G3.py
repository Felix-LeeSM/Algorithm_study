from collections import defaultdict
from sys import argv, stdin
from heapq import heappop, heappush
input = stdin.readline


class Heap(list):
    def hPush(self, item):
        heappush(self, item)

    def hPop(self):
        return heappop(self)


def solution(N: int, distances: list[list[int]], start: int) -> str:

    # visited_distance[node][history] = distance
    # 해당 노드에서 해당 history를 가진 상태에서의 최단거리
    visited_distance = [[float('inf')] * (1 << N) for _ in range(N)]

    done = (1 << N) - 1
    queue = Heap()
    queue.append((0, start, 1 << start))
    while queue:
        path, node, history = queue.hPop()
        if history == done:
            return path

        for next_node in range(N):
            next_history = history | (1 << next_node)

            if visited_distance[next_node][next_history] > path + distances[node][next_node]:
                visited_distance[next_node][next_history] \
                    = path + distances[node][next_node]
                queue.hPush(
                    (path + distances[node][next_node], next_node, next_history))


def main(args=argv) -> int:

    N, start = map(int, input().split())

    distances = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, distances, start)
    print(answer)

    return 1


if __name__ == '__main__':
    main()
