# 백준 행렬 복원 행렬을 그림으로 그려보고, 연산이 가해진 부위를 되돌려주는 식으로 접근하미
def restoration(B, h, w, x, y):
    if x >= h or y >= w :
        pass
    else :
        for i in range(x, h):
            for j in range(y, w):
                B[i][j] -= B[i-x][j-y]
    answer = []
    for i in range(h):
        answer.append(B[:w])
    return answer