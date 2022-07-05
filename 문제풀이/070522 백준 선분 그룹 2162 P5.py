'''
선분 그룹 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	10623	2905	1839	25.609%
문제
N개의 선분들이 2차원 평면상에 주어져 있다. 선분은 양 끝점의 x, y 좌표로 표현이 된다.

두 선분이 서로 만나는 경우에, 두 선분은 같은 그룹에 속한다고 정의하며, 
그룹의 크기는 그 그룹에 속한 선분의 개수로 정의한다. 
두 선분이 만난다는 것은 선분의 끝점을 스치듯이 만나는 경우도 포함하는 것으로 한다.

N개의 선분들이 주어졌을 때, 이 선분들은 총 몇 개의 그룹으로 되어 있을까? 
또, 가장 크기가 큰 그룹에 속한 선분의 개수는 몇 개일까? 이 두 가지를 구하는 프로그램을 작성해 보자.

입력
첫째 줄에 N(1 ≤ N ≤ 3,000)이 주어진다. 
둘째 줄부터 N+1번째 줄에는 양 끝점의 좌표가 x1, y1, x2, y2의 순서로 주어진다.
각 좌표의 절댓값은 5,000을 넘지 않으며, 입력되는 좌표 사이에는 빈칸이 하나 있다.

출력
첫째 줄에 그룹의 수를, 둘째 줄에 가장 크기가 큰 그룹에 속한 선분의 개수를 출력한다.

예제 입력 1 
3
1 1 2 3
2 1 0 0
1 0 1 1
예제 출력 1 
1
3

예제 입력 2 
3
-1 -1 1 1
-2 -2 2 2
0 1 -1 0
예제 출력 2 
2
2
'''

# https://www.acmicpc.net/problem/2162

# ref https://www.adamsmith.haus/python/answers/how-to-check-if-two-line-segments-intersect-in-python

from collections import defaultdict
n = int(input())
p = list(range(n))
edges = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    edges.append(((x1, y1), (x2, y2)))


def getP(x):
    if p[x] == x:
        return x
    p[x] = getP(p[x])
    return p[x]


def uniP(x, y):
    x, y = getP(x), getP(y)
    if x < y:
        p[x] = y
    else:
        p[y] = x


def on_segment(p, q, r):
    # check if r lies on (p,q)
    if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):
        return True
    return False


def orientation(p, q, r):
    # return 0/1/-1 for colinear/clockwise/counterclockwise
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0
    if val > 0:
        return 1
    return -1


def intersects(seg1, seg2):
    # check if seg1 and seg2 intersect
    p1, q1 = seg1
    p2, q2 = seg2

    # find all orientations
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # check general case
    if o1 != o2 and o3 != o4:
        return True

    # check special cases
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q1, q2):
        return True
    if o3 == 0 and on_segment(p2, q2, p1):
        return True
    if o4 == 0 and on_segment(p2, q2, q1):
        return True

    return False


for i in range(n-1):
    for j in range(i+1, n):
        if intersects(edges[i], edges[j]):
            uniP(i, j)

cur_max = 0
ans = defaultdict(int)
for i in range(n):
    j = getP(i)
    ans[j] += 1
    cur_max = max(ans[j], cur_max)

print(len(ans.keys()))
print(cur_max)
