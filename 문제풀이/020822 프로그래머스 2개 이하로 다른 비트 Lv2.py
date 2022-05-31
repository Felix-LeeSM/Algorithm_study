'''
양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.

x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
예를 들어,

f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
수	비트	다른 비트의 개수
2	000...0010	
3	000...0011	1
f(7) = 11 입니다. 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
수	비트	다른 비트의 개수
7	000...0111	
8	000...1000	4
9	000...1001	3
10	000...1010	3
11	000...1011	2
정수들이 담긴 배열 numbers가 매개변수로 주어집니다. numbers의 모든 수들에 대하여 각 수의 f 값을 
배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

입출력 예
입력
[2,7]

출력
[3,11]
'''


from collections import deque


# appendleft를 위해 deque를 썼다.
# 전부가 1로 되어 있거나, 0이 마지막에 있거나, 아니면 중간에 있거나 3가지 경우이다.
def solution(numbers):
    answer = list()
    for number in numbers:
        if not (number % 2):
            answer.append(number+1)
            continue
        number = deque(list(bin(number)[2:]))
        ind = 0
        for i in range(len(number)-1, 0, -1):
            if number[i] == '0':
                ind = i
                break
        if ind:
            number[ind] = '1'
            if ind != len(number)-1:
                number[ind+1] = '0'
        else:
            number[0] = '0'
            number.appendleft('1')
        answer.append(int(''.join(number), 2))
    return answer


# 인터넷의 코드를 참고하여 간결하게 적어본 코드
def solution(numbers):
    answer = list()
    for number in numbers:
        if not (number % 2):
            answer.append(number+1)
            continue
        number = '0' + bin(number)[2:]
        idx = number.rfind('0')
        number = list(number)
        number[idx], number[idx+1] = '1', '0'
        answer.append(int(''.join(number), 2))

    return answer


# 내가 참고한 code
def sol(numbers):
    def f(x):
        if x % 2 == 0:  # 짝수면 비트 끝 자리가 무조건 0이기 때문에 한 비트 차이나는 가장 작은 값은 +1한 값
            return x+1
        y = '0' + bin(x)[2:]
        idx = y.rfind('0')
        y = list(y)
        y[idx] = '1'
        y[idx+1] = '0'
        return int(''.join(y), 2)

    return [f(i) for i in numbers]
