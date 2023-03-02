from itertools import permutations


class INF(float):
    def __new__(self):
        return super(INF, self).__new__(self, 'inf')

    def __repr__(self):
        return '0'


N = 100
inf = INF()

dist = [[inf]*N for _ in range(N)]

for k, i, j in permutations(range(N), 3):
    if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]
