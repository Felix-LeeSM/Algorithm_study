import sys
input = sys.stdin.readline
nums = list(map(int, list(input())))
idx = 0
ans = 0
for i in nums:
    if not ans or i < 2:
        ans += i
    else:
        ans *= i
print(ans)


# nums = input()
# if int(nums):
#     nums = list(map(int, list(nums)))
#     ans = 0
#     idx = 0
#     while not ans:
#         ans += nums[idx]
#         idx += 1
#     for i in nums[idx:]:
#         if i < 2:
#             ans += i
#         else:
#             ans *= i
# else:
#     ans = 0
# print(ans)