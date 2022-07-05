'''
나만 안되는 연애 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	3041	1507	1202	47.736%
문제
깽미는 24살 모태솔로이다. 
깽미는 대마법사가 될 순 없다며 자신의 프로그래밍 능력을 이용하여 미팅 어플리케이션을 만들기로 결심했다. 
미팅 앱은 대학생을 타겟으로 만들어졌으며 대학교간의 도로 데이터를 수집하여 만들었다.

이 앱은 사용자들을 위해 사심 경로를 제공한다. 이 경로는 3가지 특징을 가지고 있다.

사심 경로는 사용자들의 사심을 만족시키기 위해 남초 대학교와 여초 대학교들을 연결하는 도로로만 이루어져 있다.
사용자들이 다양한 사람과 미팅할 수 있도록 어떤 대학교에서든 모든 대학교로 이동이 가능한 경로이다.
시간을 낭비하지 않고 미팅할 수 있도록 이 경로의 길이는 최단 거리가 되어야 한다.
만약 도로 데이터가 만약 왼쪽의 그림과 같다면, 
오른쪽 그림의 보라색 선과 같이 경로를 구성하면 위의 3가지 조건을 만족하는 경로를 만들 수 있다.

이때, 주어지는 거리 데이터를 이용하여 사심 경로의 길이를 구해보자.

입력
입력의 첫째 줄에 학교의 수 N와 학교를 연결하는 도로의 개수 M이 주어진다. (2 ≤ N ≤ 1,000) (1 ≤ M ≤ 10,000)

둘째 줄에 각 학교가 남초 대학교라면 M, 여초 대학교라면 W이 주어진다.

다음 M개의 줄에 u v d가 주어지며 u학교와 v학교가 연결되어 있으며 이 거리는 d임을 나타낸다. (1 ≤ u, v ≤ N) , (1 ≤ d ≤ 1,000)

출력
깽미가 만든 앱의 경로 길이를 출력한다. (모든 학교를 연결하는 경로가 없을 경우 -1을 출력한다.)

예제 입력 1 
5 7
M W W W M
1 2 12
1 3 10
4 2 5
5 2 5
2 5 10
3 4 3
5 4 7
예제 출력 1 
34
'''

# https://www.acmicpc.net/problem/14621

n, e = map(int, input().split())
gender = [i == 'M' for i in input().split()]
edges = []
p = list(range(n+1))

for _ in range(e):
    s, e, d = map(int, input().split())
    if gender[s-1]+gender[e-1] == 1:
        edges.append((d, s, e))
edges.sort()


def getP(a):
    if p[a] == a:
        return a
    p[a] = getP(p[a])
    return p[a]


def uniP(a, b):
    a, b = getP(a), getP(b)
    if a < b:
        p[a] = b
    else:
        p[b] = a


dist = 0
for d, s, e in edges:
    if getP(s) != getP(e):
        dist += d
        uniP(s, e)

par = getP(p[1])
for i in range(1, n+1):
    if getP(p[i]) != par:
        print(-1)
        break
else:
    print(dist)
