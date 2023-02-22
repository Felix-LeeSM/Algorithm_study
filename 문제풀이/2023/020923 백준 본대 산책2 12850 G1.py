'''
본대 산책2 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	1267	1051	926	85.900%
문제
숭실 대학교 정보 과학관은 유배를 당해서  캠퍼스의 길 건너편에 있다. 
그래서 컴퓨터 학부 학생들은 캠퍼스를 ‘본대’ 라고 부르고 정보 과학관을 ‘정보대’ 라고 부른다. 
준영이 또한 컴퓨터 학부 소속 학생이라서 정보 과학관에 박혀있으며 항상 꽃 이 활짝 핀 본 대를 선망한다. 
어느 날 준영이는 본 대를 산책하기로 결심하였다. 숭실 대학교 캠퍼스 지도는 아래와 같다.

[
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]]

정보과학관을 0번 건물이라고 했을 때, 그래프는 위와 같다.
(편의 상 문제에서는 위 건물만 등장한다고 가정하자)

한 건물에서 바로 인접한 다른 건물로 이동 하는 데 1분이 걸린다. 
준영이는 산책 도중에 한번도 길이나 건물에 멈춰서 머무르지 않는다. 
준영이는 할 일이 많아서 딱 D분만 산책을 할 것이다. 
(산책을 시작 한 지 D분 일 때, 정보 과학관에 도착해야 한다.) 
이때 가능한 경로의 경우의 수를 구해주자.

입력
D 가 주어진다 (1 ≤ D ≤ 1,000,000,000) 

출력
가능한 경로의 수를 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
100000000
예제 출력 1 
261245548
'''
# https://www.acmicpc.net/problem/12850
from array import array
from sys import stdin
input = stdin.readline
DIV = 1_000_000_007


def solution(D: int) -> int:
    def dp(num: int) -> dict[int: array]:
        if num in cache:
            return

        left, right = num//2, num//2 + num % 2
        if left not in cache:
            dp(left)
        if right not in cache:
            dp(right)

        cache[num] = multiply(cache[left], cache[right])

    fr, to = 0, 0
    cache = {1: [
        array('L', [0, 1, 1, 0, 0, 0, 0, 0]),
        array('L', [1, 0, 1, 1, 0, 0, 0, 0]),
        array('L', [1, 1, 0, 1, 1, 0, 0, 0]),
        array('L', [0, 1, 1, 0, 1, 1, 0, 0]),
        array('L', [0, 0, 1, 1, 0, 1, 1, 0]),
        array('L', [0, 0, 0, 1, 1, 0, 0, 1]),
        array('L', [0, 0, 0, 0, 1, 0, 0, 1]),
        array('L', [0, 0, 0, 0, 0, 1, 1, 0])]}
    dp(D)
    return cache[D][fr][to]


def multiply(mat1, mat2, n=8) -> list[array]:
    ret = [array('L', [0] * n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += (mat1[i][k] * mat2[k][j]) % DIV
                ret[i][j] %= DIV
    return ret


def square(mat, n=8):
    return multiply(mat, mat, n)


def main() -> int:

    D = int(input())

    answer = solution(D)
    print(answer)

    return 1


if __name__ == '__main__':
    assert solution(1) == 0
    assert solution(2) == 2
    assert solution(3) == 2
    main()
