import collections
    
def solution(maps):
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    queue = collections.deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(maps[0]) or ny >= len(maps) or nx < 0 or ny < 0 or maps[ny][nx] == 0:
                continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((nx, ny))
                continue
            else:
                if maps[ny][nx] <= maps[y][x] + 1:
                    continue
                else:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))
    return maps[-1][-1] if maps[-1][-1] != 1 else -1

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])