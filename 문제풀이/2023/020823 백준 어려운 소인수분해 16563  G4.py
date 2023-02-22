'''
어려운 소인수분해 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	5500	1608	905	25.000%
문제
지원이는 대회에 출제할 문제에 대해서 고민하다가 소인수분해 문제를 출제해야겠다고 마음을 먹었다. 
그러나 그 이야기를 들은 동생의 반응은 지원이의 기분을 상하게 했다.

"소인수분해? 그거 너무 쉬운 거 아니야?"

지원이는 소인수분해의 어려움을 알려주고자 엄청난 자신감을 가진 동생에게 2와 500만 사이의 자연수 N개를 주고 소인수분해를 시켰다. 
그러자 지원이의 동생은 기겁하며 쓰러졌다. 힘들어하는 지원이의 동생을 대신해서 여러분이 이것도 쉽다는 것을 보여주자!

입력
첫째 줄에는 자연수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 자연수 ki (2 ≤ ki ≤ 5,000,000, 1 ≤ i ≤ N)가 N개 주어진다.

출력
N줄에 걸쳐서 자연수 ki의 소인수들을 오름차순으로 출력하라.

예제 입력 1 
5
5 4 45 64 54
예제 출력 1 
5
2 2
3 3 5
2 2 2 2 2 2
2 3 3 3
'''

from sys import maxsize, stdin
input = stdin.readline
INF = maxsize


def solution(N: int, nums: list[int]) -> list[list[int]]:
    max_num = max(nums)+1
    min_fctrs = list(range(0, max_num))
    for num in range(2, max_num):
        for mltplr in range(2*num, max_num, num):
            if min_fctrs[mltplr] == mltplr:
                min_fctrs[mltplr] = num

    for num in nums:
        temp = []

        fctr = min_fctrs[num]
        while num > 1:
            temp.append(fctr)
            num //= fctr
            fctr = min_fctrs[num]

        print(*temp)


def main() -> int:
    N = int(input())
    nums = list(map(int, input().split()))

    solution(N, nums)

    return 1


if __name__ == '__main__':
    main()
