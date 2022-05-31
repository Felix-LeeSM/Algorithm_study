'''
문제
Recently Akim of some state decided to open exactly M music and S sports schools to support education in the state. 
There are N different cities in the state. 
For each of the cities both the number of students ready to study in music school 
and the number of students ready to study in sports school is known. Being a big fan of efficiency,
Akim doesn't want to open more than one school in any city 
(it's possible that he won't open any school in some cities).

You, as Akim's consultant, are given a task of developing a plan 
that would maximize the number of students that would study in the newly opened schools in the state.

입력
First line of input contains three integer numbers: 
N (1 ≤ N ≤ 300000), M, S (0 ≤ min(M, S), M + S ≤ N) - 
the number of cities in the state, the number of music and sports schools that Akim wishes to open respectively.

Each of the following N lines contains two integer numbers: Ai (1 ≤ Ai ≤ 105) and Bi (1 ≤ Bi ≤ 105) - 
the number of students in the i-th city that wish to study in music and sports school respectively.

출력
Output one integer number - the number of students that will study in the newly opened schools in an optimal plan.

예제 입출력

입력 1
3 1 1
5 2
4 1
6 4
출력 1
9

입력 2
7 2 3
9 8
10 6
3 5
1 7
5 7
6 3
5 4
출력 2
38



'''

import collections
# import sys

# input = sys.stdin.readline
# N, M, S = map(int, input().split())  # 도시, 음악, 스포츠 숫자
# cities = []
# for city in range(N):
#     m, s = map(int, input().split())
#     cities.append((m, s, city))


def solution(N, M, S, cities):
    music_order = sorted(cities, key=lambda x: (x[0], x[1]), reverse=True)
    sports_order = sorted(cities, key=lambda x: (x[1], x[0]), reverse=True)
    visited = [0]*N
    duplicate = collections.deque()
    ret = 0
    for idx in range(M):
        m, _, city = music_order[idx]
        ret += m
        visited[city] = 1

    for idx in range(S):
        _, s, city = sports_order[idx]
        ret += s
        if visited[city]:
            duplicate.append(sports_order[idx])
        visited[city] = 1

    cand_M, cand_S = M, S
    while duplicate:
        m, s, city = duplicate.popleft()
        if music_order[cand_M][0] + s >= sports_order[cand_S][1] + m:
            new_city = music_order[cand_M]
            ret += new_city[0]
            ret -= m
            if visited[new_city[-1]]:
                duplicate.append(new_city)
            visited[new_city[-1]] = 1
            cand_M += 1
        else:
            new_city = sports_order[cand_S]
            ret += new_city[1]
            ret -= s
            if visited[new_city[-1]]:
                duplicate.append(new_city)
            visited[new_city[-1]] = 1
            cand_S += 1

    return ret


print(solution(3, 1, 1, [(5, 2, 0), (4, 1, 1), (6, 4, 2)]))
print(solution(7, 2, 3, [(9, 8, 0), (10, 6, 1),
      (3, 5, 2), (1, 7, 3), (5, 7, 4), (6, 3, 5), (5, 4, 6)]))
