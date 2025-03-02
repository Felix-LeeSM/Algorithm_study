struct Solution;
impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>) -> i64 {
        let mut answer: i64 = nums[0] as i64;
        let mut prefix_sum: i64 = 0;
        let mut lowest: i64 = 0;
        let mut dp = std::collections::HashMap::new();
        dp.insert(0, 0);

        // 기본 골조
        // kadane 알고리즘
        //   1. 숫자를 순회하면서, 누적합을 계산한다.
        //   2. 지금까지 누적합의 최소값을 저장한다.
        //   3. 누적합 - 최소값을 계산하면, 현재까지의 최대값이 나온다.
        // dp는 누적합의 최소값을 저장한다. 단, 음수의 경우, 이걸 제외한 경우에 대해서 보정한 누적합의 최소를 저장한다.
        // dp[&0]은 아무것도 제외하지 않은 경우에서의 누적합의 최소값이다.
        for num in nums.into_iter().map(|num| num as i64) {
            prefix_sum += num;
            answer = std::cmp::max(answer, prefix_sum - lowest);

            if num < 0 {
                if let Some(&low) = dp.get(&num) {
                    dp.insert(num, std::cmp::min(low, dp[&0]) + num);
                } else {
                    dp.insert(num, dp[&0] + num);
                }

                lowest = std::cmp::min(lowest, dp[&num]);
            }

            dp.insert(0, std::cmp::min(dp[&0], prefix_sum));
            lowest = std::cmp::min(lowest, dp[&0]);
        }

        answer
    }
}
fn main() {
    assert_eq!(Solution::max_subarray_sum(vec![-1, 2, 3, -4, 5, 10]), 20);
    assert_eq!(
        Solution::max_subarray_sum(vec![1, 2, 3, 4, -2, 3, 4, 5, -10]),
        22
    );

    assert_eq!(
        Solution::max_subarray_sum(vec![3, 5, -10, 6, -10, -6, -6, -6, -3, 9]),
        14
    );

    assert_eq!(Solution::max_subarray_sum(vec![-3, 2, -2, -1, 3, -2, 3]), 7);
    assert_eq!(Solution::max_subarray_sum(vec![1, 2, 3, 4]), 10);
}
