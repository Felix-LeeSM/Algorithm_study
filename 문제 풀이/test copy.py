'''
class binaryheap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) -1

    def _up_(self):
        i = len(self)
        parent = i//2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i//2

    def push(self, val):
        self.items.append(val)
        self._up_()

    def _down_(self, idx):
        left, right = idx*2, idx*2 +1
        small = idx

        if left <= len(self) and self.items[left] < self.items[small]:
            small = left
        if right <= len(self) and self.items[right] < self.items[right]:
            small = right
        if small != idx:
            self.items[idx], self.items[small] = self.items[small], self.items[idx]
            self._down_(small)

    def pop(self):
        self.items[1] = self.items[-1]
        ret = self.items.pop()
        self._down_(1)
        return ret

class my_list:
    def __init__(self, obj):
        self.items = obj

    def bubblesort(self):
        iters = len(self.items)-1

        for iter in range(iters):
            wall = iters - iter
            for cur in range(wall):
                if self.items[cur] > self.items[cur+1]:
                    self.items[cur], self.items[cur+ \
                        1] = self.items[cur+1], self.items[cur]
        return self.items

    def selectionssort(self):
        iters = len(self.items) -1
        for iter in range(iters):
            minimum = iter
            for cur in range(iter+1, len(self.items)):
                if self.items[cur] < self.items[minimum]:
                    minimum = cur

            if minimum != iter:
                self.items[iter], self.items[minimum] = self.items[minimum], self.items[iter]
        return self.items

    def insertionsort_my(self):
        for i in range(1, len(self.items)):
            if self.items[i-1] > self.items[i]:
                for j in range(i-1, -1, -1):
                    if self.items[j] > self.items[j+1]:
                        self.items[j], self.items[j+ \
                            1] = self.items[j+1], self.items[j]
                    else:
                        break
        return self.items

    def insertionsort(self):
        for cur in range(1, len(self.items)):
            for delta in range(1, cur+1):
                cmp = cur - delta
                if self.items[cmp] > self.items[cmp+1]:
                    self.items[cmp], self.items[cmp+ \
                        1] = self.items[cmp+1], self.items[cmp]
                else:
                    break

def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    visited = collections.defaultdict(list)
    figures = 0
    dup = False # 현재 위치가 이미 방문한 위치인가.
    on_line = False

    for i in arrows:
        x = x + dx[i]
        y = y + dy[i]
        if (x, y) in visited:
            if dup:
                dup = True
                continue
            else:
                figures += 1
                dup = True
        else:
            visited.append((x, y))
            dup = False

    return figures


def destination(n, moves):
    vect = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    x, y = 1, 1
    for move in moves:
        nx = x + dx[vect[move]]
        ny = y + dy[vect[move]]
        if nx < 1 or n < nx or ny < 1 or n < ny:
            continue
        else:
            x, y = nx, ny
    return (x, y)

print(destination(int(input()), input().split()))
'''

# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37
# import collections
# import sys
# input = sys.stdin.readline

# V = int(input())
# head = set()
# graph = collections.defaultdict(list)

# for _ in range(V):
#     node, *rest = map(int, input().split())
#     node -= 1
#     for i in range(0, len(rest)-1, 2):
#         n, d = rest[i], rest[i+1]
#         graph[node].append((n-1, d))

# # 아무거나 하나 잡고, 자식들을 끝까지 모두 보낸 후, 2개를 합쳐서 최대값을 뽑는다.

# print(graph)


'''
문제
때는 2020년, 백준이는 월드나라의 한 국민이다.
월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
(단 도로는 방향이 없으며 웜홀은 방향이 있다.)
웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때,
출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 각 테스트케이스의
첫 번째 줄에는 지점의 수
N(1 ≤ N ≤ 500),
도로의 개수
M(1 ≤ M ≤ 2500),
웜홀의 개수
W(1 ≤ W ≤ 200)이 주어진다.
그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다.
S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다.
그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데
S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다. T는 10,000보다 작거나 같은 자연수 또는 0이다.

두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

출력
TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.

예제 입력 1
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8
예제 출력 1
NO
YES
'''
'''
inf = float('inf')
N = int(input())


for _ in range(N):
    num_point, num_road, num_hole = map(int, input().split())
    roads = [[inf]*num_point for _ in range(num_point)]
    for i in range(num_point):
        roads[i][i] = 0

    for __ in range(num_road):
        s, e, t = map(int, input().split())
        roads[s-1][e-1] = roads[e-1][s-1] = min(roads[s-1][e-1], t)
    for __ in range(num_hole):
        s, e, t = map(int, input().split())
        roads[s-1][e-1] = min(roads[s-1][e-1], -t)

    for i in range(num_point):
        for j in range(num_point):
            for k in range(num_point):
                roads[i][j] = min(roads[i][j], roads[i][k]+roads[k][j])

    for i in range(num_point):
        for j in range(num_point):
            for k in range(num_point):
                if roads[j][i] + roads[i][j] < 0 and (roads[i][k] != inf or roads[j][k] != inf):
                    print('NO')
                    break
            else:
                continue
            break

        else:
            continue
        break
    else:
        print('YES')
'''

# hole로 플루이드 워셜을 만들고, 해당 결과를 반영해서 holes를 이용해서 다시 플루이드 워셜을 만든다?
# 갔다가 오는데, 감소한다면

# 파이썬 기본 자료구조 작동 코드 보기

'''
문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때
필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고,
B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고,
costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다.
즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
입출력 예 설명

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.
'''

# def solution(n, costs):
#     inf = float('inf')
#     answer = 0
#     board = [[inf]*n for _ in range(n)]
#     for cost in costs:
#         board[cost[0]][cost[1]] = board[cost[1]][cost[0]] = cost[-1]
#     print(board)
#     # 0~n-1 을 연결하는데,
#     return answer


# solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])

'''
두 개의 문자열 A와 B가 주어졌을 떄, 문자열 A를 편집하여 문자열 B로 만들고자 합니다.
문자열 A를 편집할 때는 다음의 세 연산 중에서 한 번에 하나씩 선택하여 이용할 수 있습니다.
    1. 삽입(Insert): 특정한 위치에 하나의 문자를 삽입합니다.
    2. 삭제(Remove): 특정한 위치에 있는 하나의 문자를 삭제합니다.
    3. 교체(Replace): 특정한 위치에 있는 하나의 문자를 다른 문자로 교체합니다.
이떄 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미합니다.
문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하는 프로그램을 작성하세요.
예를 들어 "sunday"와 "saturday"의 최소 편집 거리는 3입니다.

입력 조건
  - 두 문자열 A와 B가 한 줄에 하나씩 주어집니다.
  - 각 문자열은 영문 알파벳으로만 구성되어 있으며, 각 문자열의 길이는 1보다 크거나 같고, 5,000보다 작거나 같습니다.
출력 조건
  - 최소 편집 거리를 출력합니다.

입력 예시 1
cat
cut
출력 예시 1
1

입력 예시 2
sunday
saturday
출력 예시 2
3
'''
'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다.
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다.
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다.
임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.
(2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
(1 ≤ c ≤ 1,000)
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

예제 입력 1
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
예제 출력 1
7
'''

'''1'''

# 1. 문자열에 'AWS'가 속해있는지 검사한다.
# 2. 'AWS'를 제거하고, 1을 반복한다.
# 3. 문자열에 'AWS'가 없을 때 빈 문자열이면 '-1'을, 아니면 'AWS'가 제거된 문자열을 반환해라

# def getFinalString(s):
#     li = []
#     for i in s:
#         li.append(i)
#         if len(li) >= 3 and li[-3:] == ['A', 'W', 'S']:
#             li.pop()
#             li.pop()
#             li.pop()
#     return ''.join(li) if li else '-1'

'''2'''

# 숫자가 들어온다. 하나의 digit이 버그가 나서 다른 digit으로 변해버린다. 그 종류 통째로
# 이 때, 최대값과 최소값의 차이를 구하라

# def findRange(num):
#     num = str(num)

#     def getMax(s: str):
#         for idx in range(len(s)):
#             if s[idx] != '9':
#                 break
#         else:
#             return int(s)
#         return int(s.replace(s[idx], '9'))

#     def getMin(s: str):
#         if s[0] == '1':
#             for idx in range(1, len(s)):
#                 if s[idx] not in ['0', '1']:
#                     tar = s[idx]
#                     to = '0'
#                     break
#             else:
#                 return int(s)
#         else:
#             tar = s[0]
#             to = '1'
#         return int(s.replace(tar, to))
#     return getMax(num)-getMin(num)

'''3'''

# 숫자 어레이 받아서 합이 k 이하인 최대 subset 길이

# import collections
# def maxLength(num, k):
#     total = 0
#     ret = collections.deque()
#     answer = 0
#     for i in range(len(num)):
#         total += num[i]
#         ret.append(num[i])
#         while total > k:
#             total -= ret.popleft()
#         answer = max(answer, len(ret))
#     return answer


# print(maxLength([1, 2, 3], 4))
# print(maxLength([3, 1, 2, 1], 4))


'''4'''

# 1 철자만 다른 단어는 이동 가능하다
# 이동 가능한 단어들을 이었을 때, 가장 길게 연결된 사슬의 길이+1을 구하라


# import heapq
# import itertools
# import collections
# def longestChain(n, words):
#     def check(a, b):
#         ai, bi = 0, 0
#         while ai < len(a):
#             if bi-ai > 1:
#                 return False
#             if a[ai] == b[bi]:
#                 ai += 1
#             bi += 1
#         return True

#     lengths = collections.defaultdict(list)
#     graph = collections.defaultdict(list)
#     words.sort(key=lambda x: len(x))

#     for word in enumerate(words):
#         lengths[len(word[1])].append(word)

#     for i in lengths.keys():
#         if i-1 in lengths:
#             fr = lengths[i]
#             to = lengths[i-1]
#             for i_f, w_f in fr:
#                 for i_t, w_t in to:
#                     if check(w_t, w_f):  # 짧, 긴
#                         graph[i_f].append(i_t)

#     board = [1]*n
#     for i in range(n+1, -1, -1):
#         for j in graph[i]:
#             board[j] = max(board[j], board[i]+1)
#     return max(board)


# print(longestChain(6, ['a', 'b', 'ba', 'bca', 'bda', 'bdca']))

'''5'''

# 1 ~ n까지 가되, visitNodes를 한번 이상 방문해라
# n은 node 갯수


# def minimumTreePath(n, edges, visitNodes):
#     if not edges:
#         return 0

#     graph = collections.defaultdict(list)
#     for s, e in map(lambda x: (x[0]-1, x[1]-1), edges):
#         graph[s].append(e)
#         graph[e].append(s)

#     dj = [float('inf')]*n
#     dj[-1] = 0
#     que = [(n-1, 0)]
#     while que:
#         node, dist = heapq.heappop(que)
#         for end in graph[node]:
#             if dj[end] > dist+1:
#                 dj[end] = dist+1
#                 heapq.heappush(que, (end, dist+1))

#     board = [float('inf')]*n

#     def sol(start, toVisit, cost):
#         if toVisit:
#             return min([sol(i, toVisit-{i}, cost+1) for i in graph[start]])
#         return dj[start]

#     return sol(0, set(visitNodes), 0)


# def minimumTreePath(n, edges, visitNodes):
#     inf = float('inf')

#     graph = collections.defaultdict(list)
#     for s, e in edges:
#         graph[s].append(e)
#         graph[e].append(s)

#     def shortest(fr, to):
#         board = [inf]*(n+1)
#         board[fr] = 0
#         que = [(0, fr)]
#         while que:
#             d, st = heapq.heappop(que)
#             if st == to:
#                 return d
#             for mid in graph[st]:
#                 if board[mid] > d+1:
#                     board[mid] = d+1
#                     heapq.heappush(que, (d+1, mid))
#         return inf

#     ret = inf
#     for i in itertools.permutations(visitNodes, len(visitNodes)):
#         cnt = 0
#         node = 1
#         for j in i:
#             cnt += shortest(node, j)
#             if cnt >= inf:
#                 break
#             node = j
#         cnt += shortest(node, n)
#         ret = min(cnt, ret)
#     return ret


# def minimumTreePath(n, edges, visitNodes):
#     inf = float('inf')

#     graph = collections.defaultdict(list)
#     for s, e in edges:
#         graph[s].append(e)
#         graph[e].append(s)

#     def shortest(fr, to):
#         board = [inf]*(n+1)
#         board[fr] = 0
#         que = [(0, fr)]
#         while que:
#             d, st = heapq.heappop(que)
#             if st == to:
#                 return d
#             for mid in graph[st]:
#                 if board[mid] > d+1:
#                     board[mid] = d+1
#                     heapq.heappush(que, (d+1, mid))
#         return inf

#     ret = inf
#     for i in itertools.permutations(visitNodes, len(visitNodes)):
#         cnt = 0
#         node = 1
#         for j in i:
#             cnt += shortest(node, j)
#             if cnt >= inf:
#                 break
#             node = j
#         cnt += shortest(node, n)
#         ret = min(cnt, ret)
#     return ret


# print(minimumTreePath(3, [(1, 2), (1, 3)], [2]))


# def solution(s, k):
#     ret = float('inf')
#     lth = len(s)-1
#     par = -1
#     for idx in range(lth+1):
#         if idx <= par:
#             continue
#         if s[idx] >= ret:
#             continue
#         temp = s[idx]
#         l, r = idx, idx
#         while r-l < k:
#             # 왼쪽으로 가는 경우:
#             # 오른쪽으로 못 갈 때
#             # 왼쪽이 더 작을 떄
#             if r >= lth or (l > 0 and s[l-1] <= s[r]):
#                 l -= 1
#                 if s[l] >= ret:
#                     par = l
#                 if s[l] > temp:
#                     break
#             else:
#                 if s[r] >= ret:
#                     par = r
#                 if s[r] > temp:
#                     break
#                 r += 1
#         else:
#             ret = temp
#     print(ret)
#     return ret


# solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)


'''
백준 내리막길
https://www.acmicpc.net/problem/1520

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if temp[x][y] >= 0:
        return temp[x][y]
    temp[x][y] = 0
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < board[x][y]:
                temp[x][y] += dfs(nx, ny)
    return temp[x][y]

m, n = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(m)]

temp = [[-1]*n for _ in range(m)]
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

    
print(dfs(0, 0))
'''

'''
문제
n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 
그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 
그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다.
이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 
어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 
우리의 임무는 이 사육사를 도와주는 것이다. n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

입력
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 
그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 
대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 
대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.

예제 입력 1 
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
예제 출력 1 
4
'''
