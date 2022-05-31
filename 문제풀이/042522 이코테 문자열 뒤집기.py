import sys
input = sys.stdin.readline
string = input()
print(min(len([i for i in string.split('0') if i]),
      len([i for i in string.split('1') if i])))
