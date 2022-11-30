'''
문제 설명

  1 2 3
  4 5 6
  7 8 9
  * 0

위와 같은 모양으로 배열된 숫자 자판이 있습니다.
숫자 타자 대회는 이 동일한 자판을 사용하여
숫자로만 이루어진 긴 문자열을 누가 가장 빠르게 타이핑하는지 겨루는 대회입니다.

대회에 참가하려는 민희는 두 엄지 손가락을 이용하여 타이핑을 합니다.
민희는 항상 왼손 엄지를 4 위에, 오른손 엄지를 6 위에 두고 타이핑을 시작합니다.
엄지 손가락을 움직여 다음 숫자를 누르는 데에는 일정 시간이 듭니다.
민희는 어떤 두 숫자를 연속으로 입력하는 시간 비용을 몇몇 가중치로 분류하였습니다.

이동하지 않고 제자리에서 다시 누르는 것은 가중치가 1입니다.
상하좌우로 인접한 숫자로 이동하여 누르는 것은 가중치가 2입니다.
대각선으로 인접한 숫자로 이동하여 누르는 것은 가중치가 3입니다.
같지 않고 인접하지 않은 숫자를 누를 때는 위 규칙에 따라 가중치 합이 최소가 되는 경로를 따릅니다.
예를 들어 1 위에 있던 손가락을 0 으로 이동하여 누르는 것은 2 + 2 + 3 = 7 만큼의 가중치를 갖습니다.
단, 숫자 자판은 버튼의 크기가 작기 때문에 같은 숫자 버튼 위에 동시에 두 엄지 손가락을 올려놓을 수 없습니다.
즉, 어떤 숫자를 눌러야 할 차례에 그 숫자 위에 올려져 있는 손가락이 있다면 반드시 그 손가락으로 눌러야 합니다.

숫자로 이루어진 문자열 numbers가 주어졌을 때
최소한의 시간으로 타이핑을 하는 경우의 가중치 합을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 100, 000
numbers는 아라비아 숫자로만 이루어진 문자열입니다.
입출력 예
numbers	result
"1756"	10
"5123"	8
입출력 예 설명
입출력 예  # 1
왼손 엄지로 17, 오른손 엄지로 56을 누르면 가중치 10으로 최소입니다.

입출력 예  # 2
오른손 엄지로 5, 왼손 엄지로 123을 누르거나
오른손 엄지로 5, 왼손 엄지로 1, 오른손 엄지로 23을 누르면 가중치 8로 최소입니다.
'''

from heapq import heappush, heappop

# cost[n][m] == n번에서 m번으로 이동할 때 가중치
cost = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]


def solution(numbers):
    visited = [[[False]*10 for _ in range(10)] for _ in range(len(numbers))]
    queue = [(0, -len(numbers), 4, 6)]
    while queue:
        fee, nxt, l, r = heappop(queue)
        if not nxt:
            return fee
        next_num = int(numbers[nxt])
        if next_num == l or next_num == r:
            heappush(queue, (fee+1, nxt+1, l, r))
            continue

        if visited[nxt+1][next_num][r] == False or visited[nxt+1][next_num][r] > fee+cost[l][next_num]:
            heappush(queue, (fee+cost[l][next_num], nxt+1, next_num, r))
            visited[nxt+1][next_num][r] = fee+cost[l][next_num]

        if visited[nxt+1][l][next_num] == False or visited[nxt+1][l][next_num] > fee+cost[r][next_num]:
            heappush(queue, (fee+cost[r][next_num], nxt+1, l, next_num))
            visited[nxt+1][l][next_num] = fee+cost[r][next_num]
