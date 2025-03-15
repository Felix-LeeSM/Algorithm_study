struct Solution;
impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();

        let mut answer = std::i32::MIN;
        let mut nums = nums.into_iter().collect::<std::collections::VecDeque<_>>();

        while let Some(one) = nums.pop_front() {
            let another = nums.pop_back().unwrap();

            answer = answer.max(one + another);
        }

        answer
    }
}
fn main() {
    assert_eq!(
        6,
        Solution::min_pair_sum(vec![5, 2, 1, 1, 4, 4, 1, 2, 1, 5])
    );
    assert_eq!(7, Solution::min_pair_sum(vec![3, 5, 2, 3]));
    assert_eq!(8, Solution::min_pair_sum(vec![3, 5, 4, 2, 4, 6]));
}
