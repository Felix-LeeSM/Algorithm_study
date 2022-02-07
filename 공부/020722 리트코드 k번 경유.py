# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200

import sys
from typing import List
import collections
import heapq
INF = int(10e10)  # 최소값 비교를 위한 큰 수.


# 나의 코드

# 발생할 수 있는 문제는, n번 경유하여 도달한 가격이 그보다 더 많이 경유해서 도달한 가격보다 더 저렴한 경우,
# 더 적게 경유한 경우에 대해서 n번 경유한, 즉 더 저렴한 가격을 이용해서 연산이 실시되는 것이 문제였습니다.
# 이를 해결하기 위해서 저는 경유한 횟수를 기준으로 하여 heap 자료구조를 형성하였습니다.
# 횟수가 더 짧은 경우가 더 먼저 연산되기 때문에, 저의 문제 풀이의 경우에는 도착지에 도달한다고 하더라도
# 그 경우가 가장 가격이 싼 경우라고 할 수 없습니다.
# 따라서 모든 연산을 종료한 후에 그 최소값을 취하는 방식으로

class Solution:
    def findCheapestPrice(self, nodes: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dep_to_arr = collections.defaultdict(list)  # 간선과 가중치를 담아줄 dictionary
        prices = [INF]*nodes  # src에서 해당 지점까지 최저값을 담아 줄 list
        prices[src] = 0  # 시작점의 cost는 0이다.

        for departure, arrival, cost in flights:  # dictionary에 간선과 가중치를 담아준다.
            dep_to_arr[departure].append((arrival, cost))

        queue = []
        queue.append((0, 0, src))  # 0번 경유했고, cost가 0이고, src에서 출발한다.
        # 원소의 개수가 하나인 경우, append나 heappush나 결과가 동일하여 append를 한다.
        while queue:
            nth, value, dep = heapq.heappop(queue)  # nth번 경유하여 dep에 도착함.
            if nth <= k:
                for arr, cost in dep_to_arr[dep]:
                    if prices[arr] > value + cost:
                        prices[arr] = value + cost  # nth+1번 경유하여 arr에 도착함.
                        heapq.heappush(queue, (nth+1, prices[arr], arr))

        ret = prices[dst]
        print(ret)
        return ret if ret != INF else -1


test = Solution()
assert test.findCheapestPrice(nodes=3, flights=[[0, 1, 100], [1, 2, 100], [
    0, 2, 500]], src=0, dst=2, k=1) == 200
assert test.findCheapestPrice(5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [
    3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2) == 7
assert test.findCheapestPrice(5, [[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [
    3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]], 0, 4, 1) == 5


# 책의 풀이...

# 책의 경우에는 cost를 기준으로 하되, 경유할 수 있는 횟수가 더 많은 경우에도 갱신을 해주어
# 경유를 더 많이 하고, 더 저렴한 비용을 소요한 경우를 먼저 진행해준 후, 경유를 덜 한, 그러나 더 비싼
# 경우를 갱신해주어 문제를 해결하였습니다.
# 가격을 기준으로 heqp 구조가 형성되어 있기 때문에, 더 많이 경유하고, 더 저렴한 비용을 소요한 경우를 먼저
# 연산해주어, 그 다음에 더 비싸지만 직항으로 도달한 경우로 갱신을 해주더라도 앞서 나간 경우가 같은 루트를 밟더라도
# 항상 앞서서 연산되기 때문에 문제가 발생하지 않습니다.

# 또한, 가격을 기준으로 연산이 진행되기 때문에, 도착지에 도달하는 경우가 바로 가장 싼 경우이고, 따라서 바로
# return을 해주어도 문제가 발생하지 않습니다.
class Solution_book:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, K)] * n
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or k-1 >= weight[v][1]:
                        # 더 싸거나, 경유를 덜 한 경우에 갱신해준다
                        # 경유를 덜 한 것이 더 비싼 경우에는 더 나중에 연산된다.
                        # 경유를 더 많이 하고 더 싼 경우가 앞서 나가기 때문에
                        # 갱신이 되더라도 영향을 받지 않는다.
                        weight[v] = (alt, k-1)
                        heapq.heappush(Q, (alt, v, k - 1))
        return -1
