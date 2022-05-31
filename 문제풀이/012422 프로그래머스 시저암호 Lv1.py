# 오늘 새로 풀어본 방식

def solution(st, n):
    ret = ''
    for i in st:
        if i == ' ':
            ret += ' '
        elif ord(i) < ord('a'):
            j = ord(i) + n if ord(i) + n < ord('Z') + 1 else ord(i) + n - 26
            ret += chr(j)
        else:
            j = ord(i) + n if ord(i) + n < ord('z') + 1 else ord(i) + n - 26
            ret += chr(j)
    return ret

# 과거의 내가 풀었던 방식

def solution(s, n):
    lilo, liup = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = [i for i in s]
    for i in range(len(s)) :
        if s[i].isupper() :
            s[i] = liup[(liup.index(s[i]) + n) % 26]
        elif s[i].islower() :
            s[i] = lilo[(lilo.index(s[i]) + n) % 26]
    a = ""
    for ii in s :
        a += ii
    return a

# 과거의 내가 풀었던 방식을 refine한 것 

def solution(s, n):
    lilo, liup = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = list(s)
    for i in range(len(s)) :
        if s[i].isupper() :
            s[i] = liup[(liup.index(s[i]) + n) % 26]
        elif s[i].islower() :
            s[i] = lilo[(lilo.index(s[i]) + n) % 26]
    return "".join(s)