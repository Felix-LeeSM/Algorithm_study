'''
최소 스패닝 트리 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	50758	21181	11852	40.083%
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

예제 입력 1 
3 3
1 2 1
2 3 2
1 3 3
예제 출력 1 
3
'''

# https://www.acmicpc.net/problem/1197

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
edges = sorted([tuple(map(int, input().split()))
               for _ in range(m)], key=lambda x: x[-1])
p = list(range(n+1))


def getP(x):
    if p[x] == x:
        return x
    p[x] = getP(p[x])
    return p[x]


def uniP(x, y):
    x, y = getP(x), getP(y)
    if x < y:
        p[x] = y
    else:
        p[y] = x


cnt = 0

for x, y, d in edges:
    if getP(x) != getP(y):
        cnt += d
        uniP(x, y)
print(cnt)
