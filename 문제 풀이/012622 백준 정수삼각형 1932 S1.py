# 밑에서 두번째 줄부터 매 원소를 해당 원소까지 올라온 최대값으로 만들어준다.
# 그 후, 꼭대기 원소에서 둘 중의 더 큰 값을 선택하면 된다.

def solution(triangle):
    for i in range(len(triangle)-2, -1, -1) :
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
print(solution(triangle))