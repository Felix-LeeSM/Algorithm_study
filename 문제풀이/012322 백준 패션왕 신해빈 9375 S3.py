import sys
import collections
for _ in range(int(sys.stdin.readline())):
    wearable = collections.defaultdict(int)
    for __ in range(int(sys.stdin.readline())):
        wearable[sys.stdin.readline().strip().split()[1]] += 1
    t = wearable.values()
    cnt = 1
    if t:
        for i in t:
            cnt *= (i + 1)
    print(cnt-1)