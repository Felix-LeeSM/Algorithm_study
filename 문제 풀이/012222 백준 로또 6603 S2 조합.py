# itertools의 combination을 이용했다.
# 그 외엔 출력 형식을 맞춰주는 것 정도.
import sys
import itertools
while True:
    nums = list(map(int, sys.stdin.readline().split()))[1:]
    if len(nums) < 6:
        break
    candis = itertools.combinations(nums, 6)
    for i in candis:
        for j in i:
            print(j, end=" ")
        print()
    print()