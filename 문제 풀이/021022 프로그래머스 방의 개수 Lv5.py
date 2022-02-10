# 해당 지점을 통과하는데, 이미 통과한 지점일 때,
# 그리고 내가 지금 그리는 궤적이 이미 그려진 궤적이 아닐 때
# 방이 하나 발생한다.


import collections


def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    figures = 0
    trace = collections.defaultdict(set)
    # 궤적을 그려주는데, 어떤 점에서 어떤 점으로 이동했는지를 그린다.
    for i in arrows:
        for _ in range(2):
            # 대각선으로 교차하는 경우를 나타내기 위해, 각 방형으로 2번 움직인다.
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in trace:
                if (nx, ny) not in trace[(x, y)]:
                    trace[(x, y)].add((nx, ny))
                    trace[(nx, ny)].add((x, y))
                    figures += 1
            else:
                trace[(x, y)].add((nx, ny))
                trace[(nx, ny)].add((x, y))
            x, y = nx, ny
    return figures
