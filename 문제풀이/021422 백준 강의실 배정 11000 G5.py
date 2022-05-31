'''
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

예제 입력 1 
3
1 3
2 4
3 5
예제 출력 1 
2
'''
import heapq
import sys
input = sys.stdin.readline

N = int(input())
using = []
classes = []

for _ in range(N):
    s, t = map(int, input().split())
    classes.append((s, t))
classes.sort()

par = 0
ans = 0
for i in range(N):
    s, t = classes[i]
    while using and using[0] <= s:  # 가장 빨리 끝나는 친구가 더 빨리 끝난다면? pop한다
        heapq.heappop(using)
        par -= 1
    heapq.heappush(using, t)
    par += 1
    ans = max(par, ans)
print(ans)
