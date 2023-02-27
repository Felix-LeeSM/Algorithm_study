from collections import deque
from sys import argv, stdin
input = stdin.readline


class inf(float):
    def __new__(self):
        return super(inf, self).__new__(self, 'inf')

    def __repr__(self):
        return '0'


enum = enumerate
vector = ((-1, 0), (1, 0), (0, -1), (0, 1))
INF = inf()


def Kruskal(edges, n):
    parents = list(range(n+1))

    def getP(x):
        a = x
        while parents[x] != x:
            x = parents[x]
        parents[a] = x
        return x

    def union(x, y):
        X, Y = getP(x), getP(y)
        if X < Y:
            parents[Y] = X
        else:
            parents[X] = Y

    ans = 0
    cnt = 0
    for d, i, j in sorted(edges):
        if getP(i) != getP(j):
            union(i, j)
            ans += d
            cnt += 1

    return ans if cnt == n-1 else -1


def solution(N: int, M: int, board: list[list[int]]) -> int:
    islands = [[0] * M for _ in range(N)]

    cur = 1
    for i in range(N):
        for j in range(M):
            if islands[i][j] or not board[i][j]:
                continue
            islands[i][j] = cur

            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + vector[d][0], y + vector[d][1]
                    if not (0 <= nx < N and 0 <= ny < M) or islands[nx][ny] or not board[nx][ny]:
                        continue

                    islands[nx][ny] = cur
                    queue.append((nx, ny))
            cur += 1

    queues = [deque() for _ in range(cur)]
    dists = [[INF] * cur for _ in range(cur)]

    for i in range(N):
        for j in range(M):
            if islands[i][j]:
                queues[islands[i][j]].extend([(0, d, i, j) for d in range(4)])

    for island in range(1, cur):
        queue = queues[island]

        while queue:
            dist, d, x, y = queue.popleft()

            dx, dy = vector[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if islands[nx][ny]:
                next_island = islands[nx][ny]
                if island == next_island or dist == 1:
                    continue
                if dists[island][next_island] > dist:
                    dists[island][next_island] = \
                        dists[next_island][island] = dist
            else:
                queue.append((dist+1, d, nx, ny))

    edges = [(dists[i][j], i, j) for i in range(1, cur-1)
             for j in range(i+1, cur) if dists[i][j] != INF]

    return Kruskal(edges, cur-1)


def main(args=argv) -> int:
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, M, board)
    print(answer)
    return 1


if __name__ == '__main__':

    main()
