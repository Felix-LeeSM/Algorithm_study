# 상대적으로 먼 거리의 풍선을 선택할 때 발생하는 손실을 최소화한다는 아이디어를 잡고, 
# 그 손실이 많은 것 부터 해결하는 방식으로 문제에 접근하였다.
tNum, inA, inB = map(int, input().split())
teams = list()
ret = 0
for _ in range(tNum) :
    each_team = list(map(int, input().split()))
    teams.append(each_team)

teams.sort(key = lambda x : -abs(x[1]-x[2]))
print(teams)
for team in teams :
    for _ in range(team[0]) :
        if inA and inB:
            if team[1] >= team[2] :
                inB -= 1
                ret += team[2]
            else :
                inA -= 1
                ret += team[1]
        else :
            if inA :
                ret += team[1]
            else :
                ret += team[2]
print(ret)