'''
커피숍2 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	15209	4656	3494	29.896%
문제
모두 알다시피 동호는 커피숍의 마담이다. (마담이 무엇인지는 본인에게 물어보도록 하자.)

어느 날 커피숍의 손님 A씨가 동호에게 게임을 하자고 했다.

그 게임은 다음과 같은 규칙을 갖는다.

N개의 정수가 있으면, 동호는 다음과 같이 말한다. “3~7번째 수의 합은 무엇이죠?” 그러면 상대방은 “그 답은 000입니다. 
그리고 8번째 수를 2로 고치도록 하죠” 그러면 동호는 “네 알겠습니다.”라고 한 뒤에 
다시 상대방이 동호가 했던 것처럼 “8~9번째 수의 합은 무엇이죠?”라고 묻게된다. 이 것을 번갈아 가면서 반복하는 게임이다.

당신은 이 게임의 심판 역을 맡았다. 요컨대, 질문에 대한 답들을 미리 알아야 한다는 것이다.

당신의 머리가 출중하다면 10만개 가량 되는 정수와 10만턴 정도 되는 게임을 기억할 수 있을 것이다. 
몇판 이 게임을 즐기던 동호는 많은 사람들이 이 게임을 하기를 바라게 되었고, 당신에게 심판 프로그램을 구현해달라고 요청했다.

입력
첫째 줄에 수의 개수 N과 턴의 개수 Q가 주어진다.(1 ≤ N, Q ≤ 100,000) 둘째 줄에는 처음 배열에 들어가 있는 정수 N개가 주어진다. 
세 번째 줄에서 Q+2번째 줄까지는 x y a b의 형식으로 x~y까지의 합을 구하여라, a번째 수를 b로 바꾸어라 라는 뜻의 데이터가 주어진다.

입력되는 모든 수는 -231보다 크거나 같고, 231-1보다 작거나 같은 정수이다.

출력
한 턴마다 구한 합을 한 줄마다 한 개씩 출력한다.

예제 입력 1 
5 2
1 2 3 4 5
2 3 3 1
3 5 4 1
예제 출력 1 
5
10
노트
x~y는 당연히 x번째 부터 y번째가 맞다. 하지만, 이 문제에서는 x > y인 경우 y번째 부터 x번째이다.

'''
from array import array
from itertools import repeat
from sys import argv, stdin
input = stdin.readline


def solution(N: int, nums: list[int], queries: list[tuple[int, int, int, int]]) -> str:
    arr = array('l', repeat(0, N+1))
    tree = array('l', repeat(0, N+1))
    ret = []

    def update(idx, dif):
        while idx <= N:
            tree[idx] += dif
            idx += (idx & -idx)

    def accum(idx):
        result = 0
        while idx > 0:
            result += tree[idx]
            idx -= (idx & -idx)
        return result

    def query(start, end):
        if end < start:
            return query(end, start)
        return accum(end) - accum(start-1)

    for idx, num in enumerate(nums, 1):
        arr[idx] = num
        update(idx, num)

    for x, y, a, b in queries:
        ret.append(query(x, y))
        update(a, b-arr[a])
        arr[a] = b

    return ret


def main(args=argv) -> int:
    N, Q = map(int, input().split())
    nums = array('l', map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    answer = solution(N, nums, queries)
    for line in answer:
        print(line)
    return 1


if __name__ == '__main__':
    main()
