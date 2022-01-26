# n회만에 갈 수 있는 최대 거리 이하이면 return하는 방식으로 접근함.
for _ in range(int(input())):
    left, right = map(int, input().split())
    distance = right-left
    n = 0
    while True:
        n += 1
        a = n//2
        if n%2 == 0:
            if distance <= (a**2 + a):
                print(n)
                break
        else:
            if distance <= (a**2 + 2*a + 1):
                print(n)
                break

