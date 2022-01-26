# 약수의 합 2 문제와 매우 유사하다.
# 하드버젼 같은 건데, 약수의 합 2를 여러회 연산시키니 시간 초과가 난다.
# 연산은 동일하게 하되, 가장 큰 것을 기준으로 하여 각각에 대해서 추가해주면?
# 안될듯. n까지를 기준으로 하여 배수를 찾는 것이므로...


import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    temp = n
    for i in range(2, n+1):
        temp += i*(n//i)
    print(temp)
