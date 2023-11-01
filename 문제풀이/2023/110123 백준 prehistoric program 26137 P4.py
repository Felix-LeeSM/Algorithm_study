# https://www.acmicpc.net/problem/26137

from sys import stdin
def input(): return stdin.readline().rstrip()


N = int(input())
answer = [0]*N

ben_ps_list, neg_ps_list = [], []
opened, closed = 0, 0

for idx in range(N):
    req, ben = 0, 0
    for p in input():
        if p == "(":
            ben += 1
        else:
            ben -= 1
            if ben < req:
                req = ben

    if ben >= 0:
        ben_ps_list.append((-req, ben, idx))
    else:
        neg_ps_list.append((-req+ben, -ben, idx))

ben_ps_list.sort(key=lambda x: x[0])
neg_ps_list.sort(key=lambda x: (x[0], -x[1], -x[2]))

for ord, (req, ben, idx) in enumerate(ben_ps_list):
    if req > opened:
        print("impossible")
        exit(0)

    opened += ben
    answer[ord] = idx + 1

for ord, (req, ben, idx) in zip(range(N-1, -1, -1), neg_ps_list):
    if req > closed:
        print("impossible")
        exit(0)

    closed += ben
    answer[ord] = idx + 1

if opened != closed:
    print("impossible")
    exit(0)

print(*answer, sep="\n")
