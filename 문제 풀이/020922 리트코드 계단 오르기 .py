'''
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# 피보나치 수열 꼬아서 낸 문제이다.


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1, 1]
        par = 1
        while par < n:
            ans.append(sum(ans[-2:]))
            par += 1
        return ans[-1]
