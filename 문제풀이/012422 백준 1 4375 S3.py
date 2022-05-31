# 혹시나 싶어서 무식하게 풀었는데 풀렸다.
# 어째서 2와 5로 나누어지지 않는 수는 
# 1로만 이루어진 배수를 가지는 지에 대해서 고민해보자.


import sys

def operator(num):
    temp = '1'
    while True:
        if int(temp)%num:
            temp += '1'
        else:
            return len(temp)

while True:
    try:
        n = int(sys.stdin.readline())
        print(operator(n))
    except:
        break