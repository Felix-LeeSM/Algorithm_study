'''
문제
민서는 강원대학교 컴퓨터공학과의 신임 교수이다. 
그녀가 저술한 효율적인 택배 배달을 위한 최적 경로 설계에 관한 연구 논문은 아직도 널리 인용되고 있다. 
오늘도 열심히 강의를 하던 민서는 놀라 자빠질 수밖에 없었다. 
한 학생이 꾸벅꾸벅 졸다가 책상에 머리를 아주 세게 박았기 때문이다. 
한시라도 수술이 시급한 상황, 민서는 의사가 되어 수술을 집도하기로 결심하였다.

사람의 뇌는 수백억 개의 뉴런으로 구성되며, 각 뉴런은 시냅스를 통하여 연결된다. 
민서의 진찰 결과, 학생은 뇌 속의 일부 뉴런의 연결이 끊어져 잠이 든 것으로 확인되었다. 
끊어진 시냅스만 복구된다면 학생은 잠에서 깨어나겠지만, 알다시피 민서는 컴퓨터공학과 교수이다.

민서는 끊어진 시냅스를 복구하는 대신 뇌 속의 모든 뉴런을 하나의 트리 형태로 연결해보고자 한다. 
여기서 트리란 사이클이 존재하지 않는 연결 그래프를 의미한다.

민서는 손기술이 뛰어나기 때문에 다음과 같은 연산을 무한히 수행할 수 있다. 
연결되지 않은 두 뉴런을 연결하거나 이미 연결된 두 뉴런의 연결을 끊는다.

뉴런의 연결 정보가 주어졌을 때, 모든 뉴런을 하나의 트리 형태로 연결하기 위하여 필요한 최소 연산 횟수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 뉴런의 개수 N과 시냅스의 개수 M이 주어진다.

이후 M개의 줄에 걸쳐 시냅스로 연결된 두 뉴런의 번호 u, v가 주어진다.

모든 입력은 공백으로 구분되어 주어진다.

출력
첫 번째 줄에 모든 뉴런을 트리 형태로 연결하기 위하여 필요한 최소 연산 횟수를 출력한다.

제한
2 ≤ N ≤ 100,000
1 ≤ M ≤ min(N x (N - 1) / 2, 100,000)
1 ≤ u, v ≤ N
u ≠ v
두 뉴런 사이에는 최대 1개의 시냅스만 존재한다.
예제 입력 1 
4 2
1 2
3 4
예제 출력 1 
1
'''


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = list(range(n+1))


def get_parent(x):
    if parents[x] == x:
        return x
    return get_parent(parents[x])


def union(a, b):
    a, b = get_parent(a), get_parent(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    if get_parent(a) == get_parent(b):
        cnt += 1
    else:
        union(a, b)

for i in range(1, n):
    if get_parent(i) != get_parent(i+1):
        union(i, i+1)
        cnt += 1
print(cnt)
