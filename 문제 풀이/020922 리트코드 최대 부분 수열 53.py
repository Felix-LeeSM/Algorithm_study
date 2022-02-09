'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''


# 기초적인 dp문제이지만, 어려웠다..
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            # idx에 대해서 계산할 때, nums의 [idx]는 nums[:idx+1] 배열의 최대 부분 수열의 합이 된다.
            nums[idx] = max(nums[idx-1]+nums[idx], nums[idx])
        return max(nums)


test = Solution()
test.maxSubArray([-1])
