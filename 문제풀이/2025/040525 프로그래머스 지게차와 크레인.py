# https://school.programmers.co.kr/learn/courses/30/lessons/388353


from typing import List, Set


def solution(storage: List[str], requests: List[str]) -> int:
    storage = [list(line) for line in storage]

    n = len(storage)
    m = len(storage[0])

    deleted: Set[str] = set()

    def external(char: str) -> None:
        if char in deleted:
            return

        visited = [[False] * m for _ in range(n)]
        border = []
        for i in (-1, n):
            for j in range(m):
                border.append((i, j))

        for j in (-1, m):
            for i in range(n):
                border.append((i, j))

        to_del = []

        while border:
            x, y = border.pop()
            if x == 3 and y == 4:
                pass
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny]:
                        if storage[nx][ny] == '':
                            visited[nx][ny] = True
                            border.append((nx, ny))
                        elif storage[nx][ny] == char:
                            visited[nx][ny] = True
                            to_del.append((nx, ny))

        for x, y in to_del:
            storage[x][y] = ''

    def whole(char: str) -> None:
        if char in deleted:
            return
        deleted.add(char)

        for i, line in enumerate(storage):
            for j, ch in enumerate(line):
                if ch == char:
                    storage[i][j] = ''

    for req in requests:
        if len(req) == 1:
            external(req)
        else:
            whole(req[0])

    answer = 0
    for i in range(n):
        for j in range(m):
            if storage[i][j]:
                answer += 1
    return answer


assert 11 == solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])
assert 4 == solution(["HAH", "HBH", "HHH", "HAH", "HBH"],
                     ["C", "B", "B", "B", "B", "H"])
