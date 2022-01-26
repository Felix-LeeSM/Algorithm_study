'''
def dfs_permutation(lst,n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack  = []
    for i in idx:
        stack.append([i])

    while stack:
        cur = stack.pop()
#         print('cur', cur)
        for i in idx:
            if i not in cur:
                temp=cur+[i]
#                 print('temp', temp)
                if len(temp)==n: 
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)
    return ret

'''
import this