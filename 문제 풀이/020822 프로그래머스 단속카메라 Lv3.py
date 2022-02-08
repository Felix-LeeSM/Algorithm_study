# 그리디 알고리즘 문제이다.
# 먼저 나가는 친구들 이 앞에 오게 정렬 한 후,
# 그 나가는 지점에 카메라를 한대 씩 추가해주면 된다.

def solution(routes):
    routes.sort(key=lambda x: x[-1])
    cams = []
    for _, right in routes:
        if cams[-1] <= right:
            break
        else:
            cams.append(right)
    return len(cams)
