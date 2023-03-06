'''
가운데를 말해요 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	128 MB	49348	14351	10788	30.427%
문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면,
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 
동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

예제 입력 1 
7
1
5
2
10
-99
7
5
예제 출력 1 
1
1
2
2
2
2
5
'''
'''
class MinHeap(list):
    def hPush(self, item):
        return heappush(self, item)

    def hPop(self):
        return heappop(self)

    def getMost(self):
        if self:
            return self[0]
        return float('inf')


class MaxHeap(list):
    def hPush(self, item):
        return heappush(self, -item)

    def hPop(self):
        return -heappop(self)

    def getMost(self):
        if self:
            return -self[0]
        return -float('inf')


def solution(N: int, nums: list[int]):
    left, right = MaxHeap(), MinHeap()
    answer = []

    for num in nums:
        if len(left) > len(right):
            right.hPush(num)
        else:
            left.hPush(num)

        if left.getMost() >  right.getMost():
            left.hPush(right.hPop())
            right.hPush(left.hPop())

        if len(left) >= len(right):
            answer.append(left.getMost())
        else:
            answer.append(right.getMost())

    return answer
'''
from heapq import heappop, heappush
from sys import argv, stdin
input = stdin.readline


def solution(N: int, nums: list[int]):
    left, right = [], []
    answer = []

    for num in nums:
        if len(left) > len(right):
            heappush(right, num)
        else:
            heappush(left, -num)

        if len(right) and -left[0] > right[0]:
            heappush(right, -heappop(left))
            heappush(left, -heappop(right))

        if len(left) >= len(right):
            answer.append(-left[0])
        else:
            answer.append(right[0])

    return answer


def main(*args: list[str]) -> int:
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    answer = solution(N, nums)
    print(*answer, sep='\n')
    return 1


if __name__ == '__main__':
    main(*argv)
