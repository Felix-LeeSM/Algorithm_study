# 하나씩 하나씩 옮겨가면서, 높은 게 나오면 stack에 index와 높이를 넣고, 낮은 게 나오면 pop을 해서 너비를 비교, 저장한다.
# 이렇게 하면, O(n)에 정리할 수 있다.
# 왜 되지...?
import sys
read = sys.stdin.readline

while True:
    histogram = read().strip().split()
    if len(histogram) == 1:
        break
    ans = 0

    histogram = list(map(int, histogram[1:]))
    histogram.append(0)
    stack = [(-1, -1)]

    for idx in range(len(histogram)):

        while histogram[idx] <= stack[-1][1]:
            width, height = stack.pop()
            ans = max(ans, height*(idx-stack[-1][0]-1))
            print(height*(idx-stack[-1][0]-1))
            print(stack)
            # 뽑아온 걸 가지고 구하지 말고
            # 남은 걸 기준으로 했어야 했는데
            # ans = max(ans, height*(idx-width-1))
        stack.append((idx, histogram[idx]))
    print(ans)
