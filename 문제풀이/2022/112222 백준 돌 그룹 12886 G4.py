'''
돌 그룹 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	9182	2847	1853	28.377%
문제
오늘 강호는 돌을 이용해 재미있는 게임을 하려고 한다. 
먼저, 돌은 세 개의 그룹으로 나누어져 있으며 각각의 그룹에는 돌이 A, B, C개가 있다. 
강호는 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.

강호는 돌을 단계별로 움직이며, 각 단계는 다음과 같이 이루어져 있다.

크기가 같지 않은 두 그룹을 고른다. 그 다음, 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라고 정한다. 
그 다음, X에 있는 돌의 개수를 X+X개로, Y에 있는 돌의 개수를 Y-X개로 만든다.

A, B, C가 주어졌을 때, 강호가 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 주어진다. (1 ≤ A, B, C ≤ 500)

출력
돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력한다.

예제 입력 1 
10 15 35
예제 출력 1 
1
예제 입력 2 
1 1 2
예제 출력 2 
0
'''

from collections import defaultdict, deque


def solution(A, B, C):
    def operation(tup):
        queue.append(tup)
        visited[tup] = 1
    tot = A+B+C
    if tot % 3:
        return 0

    goal = tot//3
    visited = defaultdict(int)
    visited[(goal, goal, goal)] = 1

    queue = deque([(goal, goal, goal)])
    while queue:
        a, b, c = queue.popleft()

        for _ in range(3):
            a, b, c = b, c, a
            if a % 2 == 0:
                next = tuple(sorted([a//2, b+a//2, c]))
                visited[next] or operation(next)
                next = tuple(sorted([a//2, b, c+a//2]))
                visited[next] or operation(next)

    if visited[tuple(sorted([A, B, C]))]:
        return 1
    return 0


print(solution(*map(int, input().split())))
