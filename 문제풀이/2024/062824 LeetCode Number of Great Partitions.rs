// https://leetcode.com/problems/number-of-great-partitions/description/

struct Solution;
const MODULO: usize = 1_000_000_007;

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let nums = nums.into_iter().map(|num| num as usize).collect::<Vec<_>>();
        let len = nums.len();
        let mut answer = 0;
        let total: usize = nums.iter().sum();

        if total >= 2 * k {
            let mut dp = [[0_usize; 1001]; 1001];
            dp[0][0] = 1;

            for (idx, num) in nums.into_iter().enumerate() {
                for sum in 0..(k + 1) {
                    let next = k.min(sum + num);

                    dp[idx + 1][next] = (dp[idx + 1][next] + dp[idx][sum]) % MODULO;
                    dp[idx + 1][sum] = (dp[idx + 1][sum] + dp[idx][sum]) % MODULO;
                }
            }

            answer += dp[len][k] + MODULO;
            answer -= dp[len].into_iter().take(k).sum::<usize>() % MODULO;
            answer %= MODULO;
        }

        answer as i32
    }
}

fn main() {
    assert!(Solution::count_partitions(vec![1, 2, 3, 4], 4) == 6);
    assert!(Solution::count_partitions(vec![3, 3, 3], 4) == 0);
    assert!(Solution::count_partitions(vec![6, 6], 2) == 2);
}
