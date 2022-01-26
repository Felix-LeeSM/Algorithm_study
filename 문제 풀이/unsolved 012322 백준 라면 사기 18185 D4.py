# 수행 시간이 매우 짧아 최적화를 잘 해야하는 그리디 알고리즘.
import sys
length = int(sys.stdin.readline())
needed = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
ind = 0
while ind < length-2:
    if needed[ind] == 0:
        ind += 1
        continue
    else :
        key = min(needed[ind:ind+3])
        cnt += key*7
        # 추가 작업이 필요하고, 한다고 해서 돌아갈 지는 모름...


for i in range(0, len(needed)-2, 3):
    while needed[i] > 0:
        if needed[i+1] > 0:
            if needed[i+2] > 0:
                k = min(needed[i], needed[i+1], needed[i+2])
                needed[i] -= k
                needed[i+1] -= k
                needed[i+2] -= k
                cnt += 7*k
            else:
                k = min(needed[i], needed[i+2])
                needed[i] -= k
                needed[i+1] -= k
                cnt += 5*k
        else:
            cnt += 3 * needed[i]
            needed[i] = 0
end = needed[-2:]
k = min(end)
cnt += 5*k
cnt += 3*(sum(end)-2*k)
print(cnt)