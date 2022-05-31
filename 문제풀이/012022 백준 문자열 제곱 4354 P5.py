#우선, 각 s의 길이의 약수를 모두 구한 후, 큰 약수 순서대로 구한다.

def divisor(num : int) -> list[int]:
    ret = [1]
    if num == 1:
        return ret
    for i in range(2, num//2 +1):
        if num%i == 0:
            ret.append(i)
    ret.append(num)
    return ret

while True:
    s = input()
    if s == '.':
        break
    length = len(s)
    divisors = divisor(length)
    for i in divisors:
        if s[:i] * (length//i) == s:
            print(length//i)
            break