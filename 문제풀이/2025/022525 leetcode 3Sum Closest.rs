struct Solution;
impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums.clone();
        nums.sort();

        let mut min_diff = i32::MAX;

        for pre in 0..(nums.len() - 2) {
            let mut left = pre + 1;
            let mut right = nums.len() - 1;

            while left < right {
                let diff = nums[pre] + nums[left] + nums[right] - target;

                if min_diff.abs() > diff.abs() {
                    min_diff = diff;
                }

                if diff <= 0 {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }

        target + min_diff
    }
}

fn main() {
    assert_eq!(Solution::three_sum_closest(vec![-1, 2, 1, -4], 1), 2);
    assert_eq!(Solution::three_sum_closest(vec![0, 0, 0], 0), 0);
}
