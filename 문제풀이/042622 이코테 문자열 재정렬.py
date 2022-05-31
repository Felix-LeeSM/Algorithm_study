line = input()
chars = [i for i in line if i.isalpha()]
num = sum([int(i) for i in line if i.isdigit()])
print(''.join(sorted(chars)), num, sep='')

'''
line = input()
chars = []
nums = []
for i in line:
    if i.isalpha():
        chars.append(i)
    else:
        nums.append(i)
print(''.join(sorted(chars)), sum(map(int, nums)), sep='')
'''
