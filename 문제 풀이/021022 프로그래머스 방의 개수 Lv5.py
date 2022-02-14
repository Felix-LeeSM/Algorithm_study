# 최초 풀이 : 틀림
# 찾은 반례:
# 중복된 지점에서 중복된 지점으로 이동하는 경우를 모두 제외하기 때문에
# ㄱ형태의 구조에 \ 형태의 선이 그어지는 것을 감지할 수 없음.

'''
def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    visited = [(0, 0)]
    figures = 0
    dup = False # 현재 위치가 이미 방문한 위치인가.
    
    for i in arrows:
        x = x + dx[i]
        y = y + dy[i]
        if (x, y) in visited:
            if dup:
                dup = True
                continue
            else:
                figures += 1
                dup = True
        else:
            visited.append((x, y))
            dup = False
    
    return figures
'''

# 수정 필요 사항 :
# 현재 상태에 대한 추가 정보가 필요함
# 이미 그어진 직선 상에 존재하는 것인지에 대한 여부.
# on_stream 같은 변수로 받으면 좋을 듯.
# 또한, 매번 visited를 찾아보는 것은 시간적으로 손해인듯 함.
# 시간 초과가 뜸.

'''
def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    clines = (2, 1, 0, -1, 2, 1, 0, -1)
    visited = collections.defaultdict(list)
    figures = 0
    dup = False # 현재 위치가 이미 방문한 위치인가.
    
    for i in arrows:
        nx = x + dx[i]
        ny = y + dy[i]
        cline = clines[i]
        visited[(nx, ny)].append(cline) # 한 번만 append해야 할 것으로 생각됨. 

        
        
        
        if (x, y) in visited:
            if dup:
                dup = True
                continue
            else:
                figures += 1
                dup = True
        else:
            visited.append((x, y))
            dup = False
    
    return figures
'''

# 정리 -
# 해당 지점을 통과하는데, 이미 통과한 지점일 때,
# 그리고 내가 지금 그리는 궤적이 이미 그려진 궤적이 아닐 때
# 방이 하나 발생한다.




import collections
def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    figures = 0
    trace = collections.defaultdict(set)
    # 궤적을 그려주는데, 어떤 점에서 어떤 점으로 이동했는지를 그린다.
    for i in arrows:
        for _ in range(2):
            # 대각선으로 교차하는 경우를 나타내기 위해, 각 방형으로 2번 움직인다.
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in trace:
                if (nx, ny) not in trace[(x, y)]:
                    trace[(x, y)].add((nx, ny))
                    trace[(nx, ny)].add((x, y))
                    figures += 1
            else:
                trace[(x, y)].add((nx, ny))
                trace[(nx, ny)].add((x, y))
            x, y = nx, ny
    return figures
