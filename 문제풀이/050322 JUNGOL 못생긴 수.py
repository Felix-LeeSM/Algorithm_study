# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=597&sca=50&sfl=wr_subject&stx=%EB%AA%BB%EC%83%9D%EA%B8%B4&sop=and
'''
문제
못생긴 수란, 소인수분해 했을 경우 나오는 소인수가 2, 3 그리고 5뿐인 수를 이야기 하며, 이를 수열로 늘어놓으면 다음과 같다.
1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
이는 처음나오는 10개의 못생긴 수이며, 편의상 1을 포함하도록 하자. 정수 n이 주어졌을 때, n번째 못생긴 수를 출력하는 프로그램을 작성하라.

입력형식
한 줄에 양의 정수 n(n≤1, 500)이 주어진다. 입력에 0 이 주어질 때까지 계속 한다.

출력형식
출력에는 n번째 못생긴 수를 출력한다.


입력 예
1
2
9
0
출력 예
1
2
10
'''
import heapq
dp = []
li = [(1, (0, 0, 0))]
while True:
    n = int(input())
    if not n:
        break
    if len(dp) >= n:
        print(dp[n-1])
        continue
    while len(dp) < n:
        num, expos = heapq.heappop(li)
        if not dp or num > dp[-1]:
            dp.append(num)
            heapq.heappush(li, (num*2, (expos[0]+1, expos[1], expos[2])))
            heapq.heappush(li, (num*3, (expos[0], expos[1]+1, expos[2])))
            heapq.heappush(li, (num*5, (expos[0], expos[1], expos[2]+1)))
    print(dp[n-1])
