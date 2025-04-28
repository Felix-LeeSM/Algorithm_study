// https://leetcode.com/problems/distinct-subsequences/description

struct Solution;

impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let start = s.chars().collect::<Vec<_>>();
        let to = t.chars().collect::<Vec<_>>();

        let mut dp = vec![vec![0; to.len()]; start.len()];

        if start[0] == to[0] {
            dp[0][0] = 1;
        }

        for i in 1..start.len() {
            if start[i] == to[0] {
                dp[i][0] += 1;
            }
            dp[i][0] += dp[i - 1][0];

            for j in 1..=i.min(to.len() - 1) {
                if start[i] == to[j] {
                    dp[i][j] += dp[i - 1][j - 1];
                }

                dp[i][j] += dp[i - 1][j];
            }
        }

        *dp.last().unwrap().last().unwrap() as i32
    }
}

fn main() {
    assert_eq!(
        3,
        Solution::num_distinct("arabbbit".to_string(), "rabbit".to_string())
    );

    assert_eq!(
        3,
        Solution::num_distinct("rabbbit".to_string(), "rabbit".to_string())
    );

    assert_eq!(
        5,
        Solution::num_distinct("babgbag".to_string(), "bag".to_string())
    );
}
