# 051024 백준 Starwars 16366 P4.py
# https://www.acmicpc.net/problem/16366

from itertools import product
from sys import stdin
input = stdin.readline


def solution(N, W, C, H, M, controlled, bases, wormholes):
    is_controlled = [False] * (N+2)
    is_base = [False] * (N+2)
    for control in controlled:
        is_controlled[control] = True
    for base in bases:
        is_base[base] = True

    # graph[출발지] = [(인증서, 도착지)]
    graph = [[] for _ in range(N+2)]

    for start, cert, end in wormholes:
        graph[start].append((cert, end))

    # 가상의 노드를 사용한다.
    #   - 모든 controlled solar system으로 가는 N+1번 노드와
    #   - 모든 uncontrolled solar system으로 가는 N번 노드를 만든다.
    # 최초 노드에서는 이 노드에서만 unique하게 사용되는 0번 certificate를 사용한다.
    #   - 사실 이 부분은 N번과 N+1번 노드로 가는 웜홀은 존재하지 않으므로 필요없긴 하다.
    # ∴ 탐색을 한 번만 실행해도 모든 경우를 탐색할 수 있다.

    for solar_system in range(N):
        virtual_node = N + is_controlled[solar_system]
        graph[virtual_node].append((0, solar_system))

    stack = [(N+1, N)]
    visited = [[False] * (N+2) for _ in range(N+2)]
    visited[N+1][N] = True

    while stack:
        from_control, from_alien = stack.pop()

        if is_base[from_control] and is_base[from_alien]:
            return "YES"

        for (control_cert, control_dest), (alien_cert, alien_dest) in product(graph[from_control], graph[from_alien]):
            if visited[control_dest][alien_dest]:
                continue
            if control_cert == alien_cert:
                stack.append((control_dest, alien_dest))
                visited[control_dest][alien_dest] = True

    return "NO"


def main():
    N, W, C, H, M = map(int, input().split())
    controlled_solar_systems = list(map(int, input().split()))
    military_bases = list(map(int, input().split()))
    wormholes = [tuple(map(int, input().split())) for _ in range(W)]

    answer = solution(
        N, W, C, H, M, controlled_solar_systems, military_bases, wormholes
    )

    print(answer)

    return 0


if __name__ == '__main__':
    main()
