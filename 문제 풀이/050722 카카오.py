# 1번 문제
# choices에는 1~7의 숫자의 배열이,
# survey에는 'AN', 'MJ', 'JM', 'RT' 등의 문자열의 배열이 주어진다.
# 앞의 글자가 1쪽, 뒤의 글자가 7쪽이며 4일 때 0점을 준다.
# survey[i]는 choices[i]에 대응된다.

import math
import heapq
import collections


def solution(survey, choices):
    Points = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    ret = ['' for _ in range(4)]
    # 1 비동의 7 동의
    # survey 비동의, 동의 순
    for i in range(len(choices)):
        s, c = survey[i], choices[i]
        key = s[0]
        if c > 4:
            key, c = s[1], 8-c  # 5가 되면, 2가 됨 (동의)
        Points[key] += 4-c
    ret[0] = 'R' if Points['R'] >= Points['T'] else 'T'
    ret[1] = 'C' if Points['C'] >= Points['F'] else 'F'
    ret[2] = 'J' if Points['J'] >= Points['M'] else 'M'
    ret[3] = 'A' if Points['A'] >= Points['N'] else 'N'

    return ''.join(ret)

# 2번 문제
# queue1과 queue2가 주어진다.
# 하나의 queue에서 popleft()한 후, 다른 queue에 append()하는 연산을 수행할 수 있다.
# 이 연산을 활용하여 2개 queue의 sum이 일치하도록 하려 할 때, 최소 몇회의 연산이 필요한 지 return
# 불가능하다면 -1을 return하라.
# 단, popleft()와 append()를 합쳐서 1회의 연산으로 계산한다.

# 둘 다 맞는 풀이

# def solution(queue1, queue2):
#     total = sum(queue1) + sum(queue2)
#     if total % 2:
#         return -1
#     target = total//2
#     if sum(queue1) == target:
#         return 0
#     l1, l2 = len(queue1), len(queue2)
#     w = l1+l2
#     case1 = queue1+queue2  # l1 + l2 꼴

#     ret = float('inf')

#     l, r, mid = 0, 1, case1[0]
#     while r < w and l < r:
#         if mid == target:
#             if not l and r < l1:
#                 ret = min(ret, r+l2)
#             elif not l and l1 < r < w:
#                 ret = min(ret, r-l1)
#             elif 0 < l < l1 and r < l1:
#                 ret = min(ret, w+l)
#             elif 0 < l < l1 and r == l1:
#                 ret = min(ret, l)
#             elif 0 < l < l1 and l1 < r < w:
#                 ret = min(ret, r+l-l1)
#             elif 0 < l < l1 and r == w:
#                 ret = min(ret, l)
#             elif l == l1 and l1 < r < w:
#                 ret = min(ret, r-l)
#             elif l1 < l and l1 < r < w:
#                 ret = min(ret, r+l-l1)
#             elif l1 < l and r == w:
#                 ret = min(ret, l)
#         if mid < target:
#             mid += case1[r]
#             r += 1
#         else:
#             mid -= case1[l]
#             l += 1

#     return -1 if ret == float('inf') else ret


def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2:
        return -1
    target = total // 2
    sum_arr = queue1 + queue2
    l, r = 0, len(queue1)
    temp = sum(queue1)
    answer = 0
    while r < len(queue1) + len(queue2) and l < r:
        if temp == target:
            return answer
        elif temp < target:
            temp += sum_arr[r]
            r += 1
        else:
            temp -= sum_arr[l]
            l += 1
        answer += 1
    else:
        return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))


# 3번 a, b, 문제의 배열이 주어짐
# 배열 속의 문제는 a요구랑, b요구량, a증가량, b증가량, cost 주어진다. ex) [[0, 0, 15, 15, 3], ... ]
# 해당 문제를 풀 경우, cost를 소모하여 a와 b가 증가량만큼 각각 증가한다.
# 모든 문제를 풀 수 있게 하려 하지만, 최소의 cost를 투여하고자 한다.
# 이 때의 cost를 return하라.

# 손도 못 댐
# 아래 풀이 몹시 틀림
def solution(alp, cop, problems):
    a_t, c_t = alp, cop
    for p in problems:
        a_t, c_t = max(a_t, p[0]), max(c_t[1])
    answer = 0
    que = [(0, alp, cop, o_a, o_b) for r_a, r_b, o_a, o_b,
           cost in problems if r_a >= alp and r_b >= cop]
    # cost, a력, b력, a
    temp_a, temp_b = 0, 0
    for problem in problems:
        temp_a = max(temp_a, problem[0])
        temp_b = max(temp_b, problem[1])
    while que:
        pass
    return answer


# 4번 문제이다.
# n은 노드의 갯수이다.
# paths는 간선의 배열이며 노드, 노드, 거리 순으로 주어진다.
# gates는 시작점이다.
# summits는 봉우리이다
# 한 gate에서 봉우리를 거쳐 동일 gate로 돌아오되, 거쳐가는 간선의 최대치가 가장 작도록 한다.
# 이 때의 간선의 최대치와 봉우리를 return하면 된다.
# 간선의 최대치가 같은 경우가 둘 이상인 경우, 봉우리는 가장 작은 것을 기준으로 한다.

# def solution(n, paths, gates, summits):
#     gates = set(gates)
#     summits = set(summits)
#     graph = collections.defaultdict(list)
#     for s, e, t in sorted(paths, key=lambda x: x[1]):
#         graph[s].append((e, t))
#         graph[e].append((s, t))
#     for k, v in graph.items():
#         graph[k] = sorted(v)
#     temp = theSummit = math.inf
#     visited = {node: {node: 0} for node in gates}
#     que = [(0, s, s) for s in gates]
#     # 최소 거리, 현재 노드, 시작 게이트
#     heapq.heapify(que)
#     while que:
#         intensity, now, started = heapq.heappop(que)
#         if temp <= intensity:
#             break
#         if now in summits:
#             temp = intensity
#             theSummit = min(theSummit, now)
#             stack = [started]
#             while stack:
#                 node = heapq.heappop(stack)
#                 for n, d in graph[node]:
#                     if d > temp:
#                         continue
#                     if n in gates:
#                         continue
#                     if n in summits:
#                         return [n, temp]
#             continue

#         for next, dist in graph[now]:
#             if dist > temp:
#                 continue
#             if next in gates:
#                 continue
#             if next in visited[started] and visited[started][next] <= max(intensity, dist):
#                 continue
#             visited[started][next] = max(intensity, dist)
#             heapq.heappush(que, (max(intensity, dist), next, started))
#     return [theSummit, temp]


# 바꾼 풀이.. ㅠㅠ 아마 맞을듯?


def solution(n, paths, gates, summits):
    graph = collections.defaultdict(list)
    for s, e, t in sorted(paths, key=lambda x: x[1]):
        graph[s].append((e, t))
        graph[e].append((s, t))

    summits.sort()
    visited = {node: {node: 0} for node in summits}
    que = [(0, s, s) for s in summits]
    summits = set(summits)
    gates = set(gates)
    # 최소 거리, 현재 노드, 시작 게이트
    heapq.heapify(que)
    while que:
        intensity, now, started = heapq.heappop(que)
        if now in gates:
            return [now, intensity]
        for next, dist in graph[now]:
            if next in summits or next in gates:
                continue
            temp_intensity = max(intensity, dist)
            if next in visited[started] and visited[started][next] <= temp_intensity:
                continue
            visited[started][next] = temp_intensity
            heapq.heappush(que, (temp_intensity, next, started))


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
      3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [
      2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [
      4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4],
      [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))


# 5번 문제이다
# 2차원 행렬과 operations가 주어진다.
# operations는 Rotate와 ShiftRow로 구성된다.
# Rotate의 경우, 2차원 행렬의 테투리를 시계방향으로 한칸 돌린다.
# ShiftRow의 경우, 가장 밑의 행을 가장 위로 이동시키며 나머지 행을 한칸씩 밑으로 이동시킨다.
# 모든 operation이 종료된 후, 완성된 행렬을 return하면 된다.

# 못 풀었음
def solution(rc, oper):
    i, j = len(rc), len(rc[0])
    q = collections.deque()
    for line in rc:
        q.append(collections.deque(line))

    def ro(n):
        n %= i*j
        for _ in range(n):
            for idx in range(1, i):
                q[idx-1].appendleft(q[idx].popleft())
            for idx in range(i-1, 0, -1):
                q[idx].append(q[idx-1].pop())

    def sh(n):
        q.rotate(n)

    temp = oper[0]
    cnt = 1
    for o in oper[1:]:
        if temp == o:
            cnt += 1
        else:
            if temp[0] == 'R':
                ro(cnt)
            else:
                sh(cnt)
    else:
        if temp[0] == 'R':
            ro(cnt)
        else:
            sh(cnt)
    return [list(i) for i in q]


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ['Rotate']))
