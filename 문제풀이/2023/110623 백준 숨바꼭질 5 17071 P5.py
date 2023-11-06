# https://www.acmicpc.net/problem/17071
n, k = map(int, input().split())

traces = [[False, False] for _ in range(500_001)]
traces[n][0] = True
positions = (set([n]), set())

for time in range(500_000):
    k += time

    if k > 500_000:
        print(-1)
        exit()

    if traces[k][time % 2]:
        print(time)
        exit()

    curr, nxt = positions

    while curr:
        pos = curr.pop()
        if pos > 0 and not traces[pos - 1][(time + 1) % 2]:
            nxt.add(pos - 1)
            traces[pos - 1][(time + 1) % 2] = True

        if pos < 500_000 and not traces[pos + 1][(time + 1) % 2]:
            nxt.add(pos + 1)
            traces[pos + 1][(time + 1) % 2] = True

        if pos * 2 <= 500_000 and not traces[pos * 2][(time + 1) % 2]:
            nxt.add(pos * 2)
            traces[pos * 2][(time + 1) % 2] = True
    positions = (nxt, curr)
