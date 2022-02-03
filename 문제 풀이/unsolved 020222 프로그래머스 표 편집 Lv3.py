# 시간 초과로 개박살이 났다...
'''
def solution(n, k, cmd):
    ans = ['O']*n
    cur = k
    dele = []
    for i in range(len(cmd)):
        i = cmd[i].split()
        if i[0] == 'U':
            par = int(i[1])
            while par > 0:
                cur -= 1
                if ans[cur] == 'O':
                    par -= 1

        elif i[0] == 'D':
            par = int(i[1])
            while par > 0:
                cur += 1
                if ans[cur] == 'O':
                    par -= 1

        elif i[0] == 'C':
            ans[cur] = 'X'
            dele.append(cur)
            par = 1
            if 'O' in ans[cur:]:
                while par > 0:
                    cur += 1
                    if ans[cur] == 'O':
                        par -= 1
            else:
                while par > 0:
                    cur -= 1
                    if ans[cur] == 'O':
                        par -= 1
                    
        else: # 되돌리기
            idx = dele.pop()
            ans[idx] = 'O'
            
    else:
        return ''.join(ans)
'''

def solution(n, cur, cmds):
    ans = list(range(n))
    dele = list()
    for cmd in cmds:
        cmd = cmd.split()
        if cmd[0] == 'U':
            cur -= int(cmd[1])
        elif cmd[0] == 'D':
            cur += int(cmd[1])
        elif cmd[0] == 'C':
            dele.append((cur, ans[cur]))
            del ans[cur]
            cur = max(0, cur-1)
        else:
            idx, val = dele.pop()
            ans.insert(idx, val)
            if idx <= cur:
                cur += 1
                
    ret = ""
    mkr = 0
    par = 0
    while mkr < len(ans):
        if ans[mkr] == par:
            ret += 'O'
            mkr += 1
            par += 1
        else:
            ret += 'X'
            par += 1
    return ret
