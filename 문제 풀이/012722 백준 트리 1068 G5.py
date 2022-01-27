# 코드가 아주 지저분하다.
# leaf node인지 판별하는 방법에 대해서 공부가 필요하다.
# 우선, 이 풀이에서는 graph를 부모 : 자식 node로 구성하였고,
# 모든 node에 대해서 삭제된 노드가 아닐 경우 비교를 실시하였는데,
# 그 비교는 graph의 key에 존재하느냐, 아니면 자식 node가 없느냐 2가지 경우 모두 적었다.

'''
key에 존재하지 않으면 leaf로 하여 count하였더니 맞았다.
'''
'''
import sys
import collections
read = sys.stdin.readline

nodes = int(read())
relation = list(map(int, read().split()))
dele = int(read())
root = relation.index(-1)

def to_delete(node):
        stack = [node]
        to_del = [node]
        while stack:
            now = stack.pop()
            for i in graph[now]:
                if i in to_del:
                    continue
                else:
                    to_del.append(i)
                    stack.append(i)
        return to_del

if dele == root:
    print(0)

else:
    graph = collections.defaultdict(list)
    for i in range(len(relation)):
        graph[relation[i]].append(i) # 부모 : 자식
    del graph[-1]

    to_del = to_delete(dele)
    cnt = 0

    for i in to_del:
        relation[i] = None
    
    graph = collections.defaultdict(list)
    for i in range(len(relation)):
        if relation[i] == None:
            continue
        graph[relation[i]].append(i) # 부모 : 자식
    del graph[-1]

    keys = graph.keys()
    for i in range(len(relation)):
        if relation[i] != None: # << i번째 node는 실존하면.
            if i not in keys:
                cnt += 1

    print(cnt)
'''

import sys
import collections
read = sys.stdin.readline

nodes = int(read())
relation = list(map(int, read().split()))
dele = int(read())
root = relation.index(-1)

def to_delete(node):
        stack = [node]
        to_del = [node]
        while stack:
            now = stack.pop()
            for i in graph[now]:
                if i in to_del:
                    continue
                else:
                    to_del.append(i)
                    stack.append(i)
        return to_del

if dele == root:
    print(0)

else:
    graph = collections.defaultdict(list)
    for i in range(len(relation)):
        graph[relation[i]].append(i) # 부모 : 자식
    del graph[-1]

    to_del = to_delete(dele)
    cnt = 0

    for i in to_del:
        relation[i] = None
    
    for i in range(len(relation)): # 이 부분 수정
        if relation[i] != None:
            if i not in relation:
                cnt += 1

    print(cnt)