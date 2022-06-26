'''
문제
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 
민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 
두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 
이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 
좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

출력
첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

예제 입력 1 
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
예제 출력 1 
4
'''
# https://www.acmicpc.net/problem/2887

# dictionary를 이용한 방법

# import sys
# input = sys.stdin.readline
# N = int(input())
# X, Y, Z = [], [], []
# for i in range(N):
#     x, y, z = map(int, input().split())
#     X.append((x, i))
#     Y.append((y, i))
#     Z.append((z, i))
# X.sort()
# Y.sort()
# Z.sort()

# edges = dict()
# for i in range(N-1):
#     d1, s = X[i]
#     d2, e = X[i+1]
#     if tuple(sorted([s, e])) in edges:
#         edges[tuple(sorted([s, e]))] = min(edges[tuple(sorted([s, e]))], d2-d1)
#     else:
#         edges[tuple(sorted([s, e]))] = d2-d1
#     d1, s = Y[i]
#     d2, e = Y[i+1]
#     if tuple(sorted([s, e])) in edges:
#         edges[tuple(sorted([s, e]))] = min(edges[tuple(sorted([s, e]))], d2-d1)
#     else:
#         edges[tuple(sorted([s, e]))] = d2-d1
#     d1, s = Z[i]
#     d2, e = Z[i+1]
#     if tuple(sorted([s, e])) in edges:
#         edges[tuple(sorted([s, e]))] = min(edges[tuple(sorted([s, e]))], d2-d1)
#     else:
#         edges[tuple(sorted([s, e]))] = d2-d1
# p = list(range(N))


# def getP(a):
#     if p[a] == a:
#         return a
#     p[a] = getP(p[a])
#     return p[a]


# def uniP(a, b):
#     a, b = getP(a), getP(b)
#     if a < b:
#         p[a] = b
#     else:
#         p[b] = a


# dist = 0

# for (n1, n2), d in sorted(edges.items(), key=lambda x: x[-1]):
#     if getP(n1) != getP(n2):
#         uniP(n1, n2)
#         dist += d

# print(dist)

# 리스트를 이용한 방법

import sys
input = sys.stdin.readline
N = int(input())
X, Y, Z = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))
X.sort()
Y.sort()
Z.sort()

edges = []
for i in range(N-1):
    d1, s = X[i]
    d2, e = X[i+1]
    edges.append((d2-d1, s, e))
    d1, s = Y[i]
    d2, e = Y[i+1]
    edges.append((d2-d1, s, e))
    d1, s = Z[i]
    d2, e = Z[i+1]
    edges.append((d2-d1, s, e))

p = list(range(N))


def getP(a):
    if p[a] == a:
        return a
    p[a] = getP(p[a])
    return p[a]


def uniP(a, b):
    a, b = getP(a), getP(b)
    if a < b:
        p[a] = b
    else:
        p[b] = a


dist = 0

for d, n1, n2 in sorted(edges):
    if getP(n1) != getP(n2):
        uniP(n1, n2)
        dist += d

print(dist)


# 딕셔너리를 이용한 방법과 리스트를 이용한 방법 모두 시간은 비슷하게 걸렸다.
# 해시 함수가 차지하는 비중이 edge의 갯수를 1/3으로 줄인 것보다 더 많거나 비슷한 듯 하다.
