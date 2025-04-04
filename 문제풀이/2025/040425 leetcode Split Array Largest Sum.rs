struct Solution;

impl Solution {
    pub fn split_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut right = 1_000_000_000;

        while left < right {
            let mid = (left + right) / 2;

            let mut curr = mid + 1;
            let mut cnt = 0;

            for &num in &nums {
                if curr + num > mid {
                    curr = num;
                    cnt += 1;
                } else {
                    curr += num;
                }

                if num > mid {
                    cnt = 100_000_000;
                }
            }

            if k < cnt {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        right
    }
}

fn main() {
    assert_eq!(18, Solution::split_array(vec![7, 2, 5, 10, 8], 2));
    assert_eq!(9, Solution::split_array(vec![1, 2, 3, 4, 5], 2));
    assert_eq!(4, Solution::split_array(vec![1, 4, 4], 3));
}
