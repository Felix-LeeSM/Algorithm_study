'''
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

돌리고 옮겨서 맞춰봐야 함.
'''

def solution(key, lock):
    lk, ll = len(key), len(lock)
    holes = list()
    up = list()
    for i in range(ll): # 채워줄 것들
        for j in range(ll):
            if lock[i][j] == 0:
                holes.append((i, j))

    for i in range(lk): # 채울 것들
        for j in range(lk):
            if key[i][j] == 1:
                up.append((i, j))

    for _ in range(4): # 4번 회전
        for g1 in range(-ll+1, ll): # 회전이동
            for g2 in range(-ll+1, ll):
                check = [(i[0]+g1, i[1]+g2) for i in up] # 움직여준 key
                for c in holes:
                    if c not in check: # 못 채워주면
                        break
                else:
                    for c in check:
                        if c not in holes and 0<=c[0]<ll and 0<=c[1]< ll:
                            break
                    else:
                        return True
        up = [(i[1], lk -i[0] -1) for i in up] # key를 회전시킴 # x, y >> y, n-1-x [2][0] > [0][0]
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))