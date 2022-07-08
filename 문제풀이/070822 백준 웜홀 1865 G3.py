import sys
input = sys.stdin.readline
INF = 1e9


def neg_cycle(N, edges):
    dists = [0]*(N+1)
    for _ in range(N-1):
        for s, e, t in edges:
            if dists[e] > dists[s] + t:
                dists[e] = dists[s]+t

    for s, e, t in edges:
        if dists[e] > dists[s] + t:
            return True
    return False


def solution():
    N, M, W = map(int, input().split())
    edges = set()
    board = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        board[s][e] = board[e][s] = min(board[s][e], t)
        edges.add((s, e))
        edges.add((e, s))
    for _ in range(W):
        s, e, t = map(int, input().split())
        board[s][e] = min(board[s][e], -t)
        edges.add((s, e))

    edges = {(s, e, board[s][e]) for s, e in edges}

    if neg_cycle(N, edges):
        print('YES')
        return
    print('NO')


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solution()
