'''
소수 찾기
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 
return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.

'''
# https://programmers.co.kr/learn/courses/30/lessons/42839

# is_prime을 선언한 후, dfs를 통해 모든 가능한 경우를 배열에 담았다.
# 에라토스테네스의 체를 사용했으면 시간을 단축했을듯 하다.
# 길이가 7까지이니 1억까지 했어야 하니까...
# 메모리를 너무 많이 쓸지도?


def solution(numbers):
    def is_prime(number):
        if number == 2:
            return True
        elif number == 1:
            return False
        if not number % 2:
            return False
        for i in range(3, int(number**0.5 + 2), 2):
            if not number % i:
                return False
        return True

    def dfs(li):
        if li:
            cand.add(int(''.join(li)))
        if len(li) == len(numbers):
            return
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                li.append(numbers[i])
                dfs(li)
                li.pop()
                visited[i] = 0
    numbers = list(numbers)
    cand = set()
    visited = [0]*len(numbers)
    ans = 0
    dfs([])
    for num in cand:
        if num and is_prime(num):
            ans += 1
    return ans
