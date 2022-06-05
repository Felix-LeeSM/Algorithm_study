'''
삼각 달팽이
문제 설명
정수 n이 매개변수로 주어집니다. 
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

examples.png

제한사항
n은 1 이상 1,000 이하입니다.
입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

문제 예시와 같습니다.
입출력 예 #3

문제 예시와 같습니다.
'''

# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3


def solution(n):
    goal = n*(n+1)//2
    temp = [[0]*i for i in range(1,n+1)]
    temp.append([1]*(n+1))
    for i in range(n+1):
        temp[i].append(1)
    tail = n-1
    dir = 1
    cur = 0
    idx = 0
    for num in range(1, goal+1):
        temp[cur][idx] = num
        cur += dir
        idx -= dir == -1
        if temp[cur][idx]:
            if dir == -1:
                dir = 1
                cur += 2
                idx += 1
            else:
                cur -= cur-1 == tail
                idx += 1
                if temp[cur][idx]:
                    idx -= 2
                    dir = -1
                    cur -= 1
                    tail -= 1
    # 리스트 컴프리헨션의 순서를 잘못 알고 있었다.
    # 마치 for문을 돌릴 때처럼
    # 큰 것을 먼저 쪼개줘야
    # 뒤에서 쪼갠 것을 더 쪼갤 수 있다.
    return [i for line in temp[:-1] for i in line[:-1]]
    

# 인터넷에서 발견한 더 깔끔한 풀이...
def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return [i for line in answer for i in line]