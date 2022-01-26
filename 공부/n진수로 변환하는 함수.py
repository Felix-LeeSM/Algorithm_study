def knarydigit(n, k):
    if k == 10 :
        return str(n)
    ret = ""
    par = 1
    while True :
        ret += str(n % (k**par))
        n //= (k**(par))
        if n == 0 :
            return ret[::-1]

print('0b' + knarydigit(1013424, 2), bin(1013424), sep = "\n")