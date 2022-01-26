
'''문제 해결 로직'''
# 1을 루트로 시작하여, queue에 자식 node를 append하는 것으로 시작한다.
# 각 트리의 부모 노드를 parents에 기록한다.
# parents에 기록된 node에 연결된 node를 찾아 기록한다. 
# 기록된 적이 없는 것들만 건들이므로, 다시 부모 노드에 영향을 미치지 않는다.

# -------------------------------------------------------------------------------------------------
'''접근 방법'''
# 최초에 문제에 접근했을 때에는, edge에 대한 정보를 입력해줄 때, 부모 노드와 자식 노드 순으로
# 입력된다고 생각하고, 간단하게 입력받은 node를 list에 저장하여 출력하려 했습니다.

# 그러나, 입력 받는 값은 순서가 없이 그래프와 같은 형태로 주어지는 것으로, 결과에 오류가 발생했습니다.
# 그래서, 그래프를 만들어준 후, 각 노드의 부모 노드를 탐사하는 방향으로 문제 해결 방향을 틀었습니다.

# root node가 1번이기 때문에, 1번 node를 기준으로 하여 탐사하는 방향으로 문제 해결 방향을 결정하였고,
# 그래프 탐색과 유사하다고 판단하였습니다.

# 그러나, 여전히 그래프에서는 부모와 자식을 구별지을만한 방향성이 없기 때문에, 백트래킹에서 아이디어를 
# 떠올려 부모 노드에 대해서는 연산이 진행되지 않도록 하는 방법을 떠올렸습니다.

# N Queen 문제와 비슷하게 list를 하나 두어 부모 노드를 기록한 후, 기록된 부모 노드가 있으면 이미 탐색이 
# 완료된 노드라고 판단할 수 있도록 하였습니다.

# 또한, 한 층씩 내려가면서 탐색하는 것이 BFS와 유사하다고 생각하여 queue를 이용해서 구현하였습니다.

# -------------------------------------------------------------------------------------------------
'''주석과 코드'''

import sys # 파이썬 기본 input()의 경우, 입력받은 값을 처리하는 과정이 있어 
           # sys.stdin.readline()보다 더 느립니다.
import collections


nodes = int(sys.stdin.readline()) # 최초로 입력되는 NODE의 갯수를 받아주기 위한 변수

edges = collections.defaultdict(list) # 입력받은 인접 노드들의 관계를 그래프처럼 저장하기 위해 
                                      # defaultdict를 이용합니다.
                                      # 기본 dictionary를 이용하되, if문을 통해 if (key) in edges와 else로 나누어 처리해주어도
                                      # in을 통한 탐색의 경우 key를 대상으로 하기 때문에 문제가 발생하지 않습니다.

parents = [-1]*2+[0]*(nodes-1) # NODE의 번호가 0이 아니라 1부터 시작되므로, 편하게 계산하기 위해서 NODES + 1개로 합니다.
                               # 단, 루트 node가 1번이므로 0번과 1번 index는 0이 아닌 -1로 두어 허수를 제거합니다.
queue = collections.deque() # queue를 이용한 방식으로 구현하여 collections package의 deque를 이용합니다.
queue.append(1) # 최초 실행을 위해 루트 node인 1번 node를 queue에 추가합니다.

for _ in range(nodes-1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

while queue: # BFS와 유사한 방식으로 진행하여 queue를 이용합니다.

    now = queue.popleft() # 현재 내가 찾고자 하는 자식노드들의 부모를 입력받습니다.

    for kid in edges[now]: # edges[now]는 해당 부모노드의 예비 자식노드들입니다.

        if parents[kid] == 0: # 이 if문을 통해 now node의 자식 node에 대해서만 연산을 진행할 수 있습니다.

                              # 연결관계만으로 가져온 정보이기 때문에 
                              # 예비 자식노드에는 부모노드가 포함되어 있을 수 있습니다.
                              # 그러나, 한 층 한 층 내려가는 구조로 코드가 짜여 있어서
                              # 해당 노드가 부모노드일 경우, 이미 그 부모노드의 부모노드가 
                              # parents에 입력되어 0일 수 없습니다. << root node인 1번 node의 경우,
                              # 이런 경우에 포함되지 않습니다.
                              # 따라서, 최초에 parents list를 선언할 때, 허수가 되는 0번과 부모 node가 없는
                              # 1번의 경우 -1로 선언하여 문제가 발생하지 않도록 하였습니다.

            parents[kid] = now # 해당 자식 노드에 부모 노드를 기록합니다.

            queue.append(kid) # 이제 해당 자식 노드의 자식 노드를 탐사하기 위해서
                              # queue에 kid를 append합니다.

for i in parents[2:]: # 0번 index와 1번 index는 허수이기 때문에, 2번 index부터 출력합니다.
    print(i)

# -------------------------------------------------------------------------------------------------
'''주석이 없는 코드''' # queue를 이용한 BFS

import sys
import collections

nodes = int(sys.stdin.readline())
edges = collections.defaultdict(list)
parents = [-1]*2+[0]*(nodes-1)
queue = collections.deque()
queue.append(1)

for _ in range(nodes-1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

while queue:
    now = queue.popleft()
    for kid in edges[now]:
        if parents[kid] == 0:
            parents[kid] = now
            queue.append(kid) 

for i in parents[2:]:
    print(i)

# -------------------------------------------------------------------------------------------------
'''주석이 없는 코드''' # stack을 이용한 DFS

import sys
import collections

nodes = int(sys.stdin.readline())
edges = collections.defaultdict(list)
parents = [-1]*2+[0]*(nodes-1)
stack = list()
stack.append(1)

for _ in range(nodes-1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

while stack:
    now = stack.pop()
    for kid in edges[now]:
        if parents[kid] == 0:
            parents[kid] = now
            stack.append(kid) 

for i in parents[2:]:
    print(i)

# -------------------------------------------------------------------------------------------------
# 재귀 함수로 풀이

import sys
import collections

sys.setrecursionlimit(10**7)

nodes = int(sys.stdin.readline())
edges = collections.defaultdict(list)
parents = [-1]*2+[0]*(nodes-1)
queue = collections.deque()

for _ in range(nodes-1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])


def dfs(node):
    kids = edges[node]
    for kid in kids:
        if parents[kid] == 0:
            parents[kid] = node
            dfs(kid)
    return

dfs(1)

for i in parents[2:]:
    print(i)
    