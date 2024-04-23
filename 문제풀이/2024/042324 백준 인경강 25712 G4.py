from sys import stdin
input = stdin.readline

# n행 m열
m, n = map(int, input().split())
lengths = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(n)]

for idx, line in enumerate(lines):
    lines[idx] = [line[i:i+2]
                  for i in range(0, len(line), 2)]

starts = [(0, idx) for idx in range(len(lines[0]))]
visited = {coord for coord in starts}


while starts:
    row, idx = starts.pop()
    start, end = lines[row][idx]

    if row == n-1:
        print('YES')
        exit()

    for next_idx, (next_start, next_end) in enumerate(lines[row+1]):
        if next_start <= start <= next_end or next_start <= end <= next_end or start <= next_start <= end or start <= next_end <= end:
            if (row+1, next_idx) not in visited:
                starts.append((row+1, next_idx))
                visited.add((row+1, next_idx))


print('NO')
