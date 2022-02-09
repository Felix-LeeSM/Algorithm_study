'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
# ret 배열은, 해당 집까지 고려했을 때의 최대 값이다.
# n개의 집을 고려하여 최대값을 냈다면, n+1개의 집을 고려할 때에는
# n-1개를 고려한 경우와 n개를 고려한 경우를 이용해
# 도출해낼 수 있다.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = [0]*len(nums)
        ret[0] = nums[0]
        if len(nums) == 1:
            return ret[0]
        ret[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            ret[idx] = max(ret[idx-2]+nums[idx], ret[idx-1])
        return max(ret[-2:])
