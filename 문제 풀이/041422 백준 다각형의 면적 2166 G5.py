'''
문제
2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 
이 다각형의 면적을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 
좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

출력
첫째 줄에 면적을 출력한다. 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.
'''

'''
신발끈 공식을 활용하여 문제를 풀었다.
출력 형식에 대해서 확인이 필요하다...
'''

import sys
input = sys.stdin.readline
coords = list()
area = 0
dots = int(input())
for _ in range(dots):
    coords.append(tuple(map(int, input().split())))
for idx in range(dots):
    area += coords[idx-1][0]*coords[idx][1] - coords[idx][0]*coords[idx-1][1]
area = abs(area) / 2
print('%.1f' % round(area, 1))
