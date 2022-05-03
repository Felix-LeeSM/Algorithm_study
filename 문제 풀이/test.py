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

N = int(input())
works =
