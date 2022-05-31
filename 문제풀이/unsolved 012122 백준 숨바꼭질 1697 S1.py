#십빠이!
'''n, k = map(int, input().split())
count = 0
while n!=k:
    count+=1
    if abs(n-k) > abs(n*2-k):
        if abs(n*2-k) > abs(n*2-k-2):
            n-=1
        elif abs(n*2-k) > abs(n*2-k+2):
            n+=1
        else:    
            n*=2
    else:
        if n>k:
            n-=1
        else:
            n+=1
print(count)
'''

