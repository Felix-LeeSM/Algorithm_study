import sys
read = sys.stdin.readline
row, col = map(int, read().split())
arr = [list(map(int, list(read().strip()))) for _ in range(row)]


def solution(arr, row, col):
    for side in range(min(row, col)-1, -1, -1):
        for i in range(row-side):
            for j in range(col-side):
                if arr[i][j] == arr[i+side][j] == arr[i][j+side] == arr[i+side][j+side]:
                    return (side+1)**2


print(solution(arr, row, col))
