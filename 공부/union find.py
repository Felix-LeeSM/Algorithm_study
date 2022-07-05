n = 5
p = list(range(n+1))


def getP(a):
    if p[a] == a:
        return a
    p[a] = getP(p[a])
    return p[a]


def getP(x):
    a = x
    while p[x] != x:
        x = p[x]
    p[a] = x
    return x


def uniP(a, b):
    a, b = getP(a), getP(b)
    if a > b:
        p[a] = b
    else:
        p[b] = a
