'''
숨바꼭질 4 성공스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	26313	8962	6279	32.144%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
'''

# https://www.acmicpc.net/problem/13913

''' trial 1 - 최초 탐색에서 경로를 들고 간다.
            - 실패 - 시간초과
            - 매번 새로 배열을 만드는 것은 시간이 오래 걸린다.
            
visited = [0]*100001
fr, to = map(int, input().split())
visited[to] = 1

queue = deque([(to, [to])])

while queue:
    node, cache = queue.popleft()

    if node == fr:
        print(len(cache)-1)
        print(*cache[::-1])
        break

    if node >= 1 and visited[node-1] == 0:
        visited[node-1] = 1
        queue.append((node-1, cache[:] + [node-1]))

    if node < 100000 and visited[node+1] == 0:
        visited[node+1] = 1
        queue.append((node+1, cache[:] + [node+1]))

    if node % 2 == 0 and visited[node//2] == 0:
        visited[node//2] = 1
        queue.append((node//2, cache[:] + [node//2]))

'''

''' trial 2 - 배열로 도착 여부 관리
            - 성공했다.
            
setrecursionlimit(100000)

visited = [-3]*100001
fr, to = map(int, input().split())
visited[to] = 0

queue = deque([(to, 1)])

while queue:
    node, turn = queue.popleft()

    if node == fr:
        break

    if node >= 1 and visited[node-1] == -3:
        visited[node-1] = turn
        queue.append((node-1, turn+1))

    if node < 100000 and visited[node+1] == -3:
        visited[node+1] = turn
        queue.append((node+1, turn+1))

    if node % 2 == 0 and visited[node//2] == -3:
        visited[node//2] = turn
        queue.append((node//2, turn+1))

print(visited[fr])
cache = [fr]
par = False


def dfs(node, turn):
    if node == to:
        return True

    if node >= 1 and visited[node-1] == turn-1:
        cache.append(node-1)
        if dfs(node-1, turn-1):
            return True
        cache.pop()

    if node < 100000 and visited[node+1] == turn-1:
        cache.append(node+1)
        if dfs(node+1, turn-1):
            return True
        cache.pop()

    if node <= 50000 and visited[node*2] == turn-1:
        cache.append(node*2)
        if dfs(node*2, turn-1):
            return True
        cache.pop()


dfs(fr, visited[fr])
print(*cache)
'''


from collections import deque
from sys import setrecursionlimit
setrecursionlimit(1000000)

visited = {}
fr, to = map(int, input().split())
visited[to] = 0

queue = deque([(to, 1)])

while queue:
    node, turn = queue.popleft()

    if node == fr:
        break

    if node >= 1 and node-1 not in visited:
        visited[node-1] = turn
        queue.append((node-1, turn+1))

    if node < 100000 and node+1 not in visited:
        visited[node+1] = turn
        queue.append((node+1, turn+1))

    if node % 2 == 0 and node//2 not in visited:
        visited[node//2] = turn
        queue.append((node//2, turn+1))

print(visited[fr])
cache = [fr]
par = False


def dfs(node, turn):
    if node == to:
        return True

    if node-1 in visited and visited[node-1] == turn-1:
        cache.append(node-1)
        if dfs(node-1, turn-1):
            return True
        cache.pop()

    if node+1 in visited and visited[node+1] == turn-1:
        cache.append(node+1)
        if dfs(node+1, turn-1):
            return True
        cache.pop()

    if node*2 in visited and visited[node*2] == turn-1:
        cache.append(node*2)
        if dfs(node*2, turn-1):
            return True
        cache.pop()


dfs(fr, visited[fr])
print(*cache)

# visited는 list와 dict 모두 비슷한 메모리와 비슷한 시간을 소요했다.