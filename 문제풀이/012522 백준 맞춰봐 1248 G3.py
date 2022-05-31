# 시간 초과가 난다.
# is_ok로 백트래킹 하는 부분을 더 간단하게 손봐야 할 것 같은데...
'''
import sys

def solution(num, result):
    board = [''] * num

    sums = []
    for _ in range(num):
        sums.append(['']*num) 
    par = 0
    for i in range(num):
        for j in range(i, num):
            sums[i][j] = result[par]
            par += 1
    #sums[i][j]는 i~j까지의 합이다. (index 기준.)

    def is_ok(ind): # << 얘를 손봐야 하는데...
        for l in range(ind):
            ts = sum(board[l:ind+1])
            if (ts > 0 and sums[l][ind] == '+') or (ts < 0 and sums[l][ind] == '-') or (ts == 0 and sums[l][ind] == '0') :
                continue
            else:
                return False    
        return True

    def dfs(i): # i번째 수를 채운다.
        if i >= num:
            raise NotImplementedError
        else:
            for j in range(10, -11, -1):
                p = sums[i][i]
                if (p == '+' and j > 0) or(p == '-' and j < 0) or (p == '0' and j == 0):
                    board[i] = j
                    if is_ok(i):
                        dfs(i+1)
    try:
        dfs(0)
        return 
    except:
        for i in board:
            print(i, end=" ")
        return
num = int(sys.stdin.readline())
result = sys.stdin.readline().strip()
solution(num, result)
'''


'''
import sys

def solution(num, result):
    board = [''] * num

    sums = []
    for _ in range(num):
        sums.append(['']*num) 
    par = 0
    for i in range(num):
        for j in range(i, num):
            sums[i][j] = result[par]
            par += 1
    #sums[i][j]는 i~j까지의 합이다. (index 기준.)

    def is_ok(ind): # << 얘를 손봐야 하는데...
        for l in range(ind):
            ts = sum(board[l:ind+1])
            if (ts > 0 and sums[l][ind] == '+') or (ts < 0 and sums[l][ind] == '-') or (ts == 0 and sums[l][ind] == '0') :
                continue
            else:
                return False    
        return True

    def dfs(i): # i번째 수를 채운다.
        if i >= num:
            raise NotImplementedError
        else:
            if sums[i][i] == '+': # << 이쪽을 추가함.
                for j in range(1, 11):
                    board[i] = j
                    if is_ok(i):
                        dfs(i+1)
            elif sums[i][i] == '-':
                for j in range(-10, 0):
                    board[i] = j
                    if is_ok(i):
                        dfs(i+1)
            else:
                board[i] = 0
                if is_ok(i):
                    dfs(i+1)
    
    try:
        dfs(0)
        return 
    except:
        for i in board:
            print(i, end=" ")
        return
num = int(sys.stdin.readline())
result = sys.stdin.readline().strip()
solution(num, result)
'''


'''
import sys

def solution(num, result):
    board = [0] * num

    sums_idx = []
    for _ in range(num):
        sums_idx.append([' ']*num) 
    par = 0
    for i in range(num):
        for j in range(i, num):
            sums_idx[i][j] = 1 if result[par] == '+' else -1 if result[par] == '-' else 0
            par += 1
    #sums[i][j]는 i~j까지의 합이다. (index 기준.)

    def is_ok(ind): # << 얘를 손봐야 하는데...
        for l in range(ind):
            if (sum(board[l:ind+1]) * sums_idx[l][ind] > 0) or 0 == sums_idx[l][ind] == sum(board[l:ind+1]):
                continue
            else:
                return False    
        return True

    def dfs(i): # i번째 수를 채운다.
        if i >= num:
            raise NotImplementedError
        else:
            if sums_idx[i][i] == 0:
                board[i] = 0
                if is_ok(i):
                    dfs(i+1)
            else:
                for j in range(1, 11):
                    board[i] = sums_idx[i][i]*j
                    if is_ok(i):
                        dfs(i+1)
    
    try:
        dfs(0)
        return 
    except:
        for i in board:
            print(i, end=" ")
        return
num = int(sys.stdin.readline())
result = sys.stdin.readline().strip()
solution(num, result)
'''
############### 시간초과.....


import sys

def solution(num, result):
    board = [0] * num

    sums = []
    for _ in range(num):
        sums.append(['']*num) 
    par = 0
    for i in range(num):
        for j in range(i, num):
            sums[i][j] = 1 if result[par] == '+' else -1 if result[par] == '-' else 0
            par += 1
    #sums[i][j]는 i~j까지의 합이다. (index 기준.)

    def is_ok(ind): # << 얘를 손봐야 하는데...
        for l in range(ind):
            if (sum(board[l:ind+1]) * sums[l][ind] > 0) or sum(board[l:ind+1]) == sums[l][ind] == 0 :
                continue
            else:
                return False    
        return True

    def dfs(i): # i번째 수를 채운다.
        if i >= num:
            raise NotImplementedError
        else:
            if sums[i][i] == 0:
                board[i] = 0
                if is_ok(i):
                    dfs(i+1)
            else:
                for j in range(1, 11):
                    board[i] = sums[i][i]*j
                    if is_ok(i):
                        dfs(i+1)
    
    try:
        dfs(0)
        return 
    except:
        for i in board:
            print(i, end=" ")
        return
num = int(sys.stdin.readline())
result = sys.stdin.readline().strip()
solution(num, result)

#이전에 틀린 코드를 pypy로 입력하니 통과했다.