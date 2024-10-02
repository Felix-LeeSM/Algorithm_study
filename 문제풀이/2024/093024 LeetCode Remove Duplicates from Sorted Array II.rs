struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut last_num = -10001;
        let mut is_new = true;
        let mut new_idx = 0;

        for idx in 0..nums.len() {
            let num = nums[idx];

            if last_num == num && !is_new {
                continue;
            } else if last_num == num {
                is_new = false;
            } else {
                last_num = num;
                is_new = true;
            }

            nums[new_idx] = num;
            new_idx += 1;
        }

        new_idx as i32
    }
}







