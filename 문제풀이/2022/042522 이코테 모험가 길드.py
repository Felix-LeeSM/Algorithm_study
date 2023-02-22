import collections
import sys
input = sys.stdin.readline
N = int(input())
people = list(map(int, input().split()))
sheet = collections.Counter(people)
remain = 0
groups = 0
for fear, person in sorted(sheet.items()):
    groups += (remain+person)//fear
    remain = (remain+person) % fear
print(groups)
