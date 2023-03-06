'''
외판원 순회 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	41063	10605	6309	27.433%
문제
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다. 
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. 
(길이 없을 수도 있다) 이
제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 
다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
단, 한 번 갔던 도시로는 다시 갈 수 없다. 
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. 
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 
비용은 대칭적이지 않다. 
즉, W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16) 다음 N개의 줄에는 비용 행렬이 주어진다. 
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

예제 입력 1 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
예제 출력 1 
35
'''
from collections import defaultdict
from heapq import heappop, heappush
from itertools import permutations
from sys import argv, stdin
input = stdin.readline


class heap(list):
    def hPush(self, item):
        return heappush(self, item)

    def hPop(self):
        return heappop(self)


def solution(N: int, distances: list[list[int]]):
    graph = [[] for _ in range(N+1)]
    for i, j in permutations(range(N), 2):
        if distances[i][j]:
            graph[i].append((j, distances[i][j]))

    # node, visited 순으로 참조한다.
    mins = [defaultdict(lambda: float('inf')) for _ in range(N)]
    queue = heap([(0, 0, 0, 0)])
    for i in range(N):
        mins[i][0] = 0

    done = (1 << (N)) - 1

    while queue:
        dist, node, visited, start = queue.hPop()
        if visited == done:
            return dist

        for nxt_node, nxt_dist in graph[node]:
            if visited & (1 << nxt_node):
                continue

            nxt_visited = visited | (1 << nxt_node)
            if nxt_node == start and nxt_visited != done:
                continue

            if mins[nxt_node][nxt_visited] > dist + nxt_dist:

                mins[nxt_node][nxt_visited] = dist+nxt_dist
                queue.hPush((dist+nxt_dist, nxt_node,
                            visited | (1 << nxt_node), start))


def main(args=argv) -> int:
    N = int(input())
    distances = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, distances))
    return 1


if __name__ == '__main__':
    main()
