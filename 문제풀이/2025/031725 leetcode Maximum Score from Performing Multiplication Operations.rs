struct Solution;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        let m = multipliers.len();
        let mut dp = vec![vec![i32::MIN; 301]; 301];
        dp[0][0] = 0;

        for op in 0..m {
            for left in 0..=op {
                let right = op - left;

                dp[left][right + 1] = dp[left][right + 1]
                    .max(dp[left][right] + nums[nums.len() - 1 - right] * multipliers[op]);

                dp[left + 1][right] =
                    dp[left + 1][right].max(dp[left][right] + nums[left] * multipliers[op]);
            }
        }

        (0..=m)
            .map(|left| (left, m - left))
            .map(|left, right| dp[left][right])
            .max()
    }
}

fn main() {
    assert_eq!(14, Solution::maximum_score(vec![1, 2, 3], vec![3, 2, 1]));
    assert_eq!(
        102,
        Solution::maximum_score(vec![-5, -3, -3, -2, 7, 1], vec![-10, -5, 3, 4, 6])
    );
    assert_eq!(
        -300,
        Solution::maximum_score(vec![-10, -10, -10], vec![10, 10, 10])
    );
}
