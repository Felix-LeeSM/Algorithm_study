struct Solution;

const MOD: usize = 1_000_000_007;

impl Solution {
    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32 {
        let mut dp = [[0; 201]; 201];
        dp[0][0] = 1;

        let nums = nums.into_iter().map(|num| num as usize).collect::<Vec<_>>();

        let max = nums
            .iter()
            .map(|&num| num)
            .fold(usize::MIN, |max, num| max.max(num))
            + 1;

        let dp = nums
            .into_iter()
            .map(|num| num as usize)
            .fold(dp, |dp, num| {
                let mut next_dp = [[0; 201]; 201];
                (0..max).for_each(|one| {
                    (0..max).for_each(|another| {
                        let new_one = Self::gcd(one, num);
                        let new_another = Self::gcd(another, num);

                        next_dp[new_one][another] =
                            (next_dp[new_one][another] + dp[one][another]) % MOD;
                        next_dp[one][new_another] =
                            (next_dp[one][new_another] + dp[one][another]) % MOD;
                        next_dp[one][another] = (next_dp[one][another] + dp[one][another]) % MOD;
                    });
                });

                next_dp
            });

        (1..max)
            .map(|num| dp[num][num])
            .fold(0, |acc, cnt| (acc + cnt) % MOD) as i32
    }

    fn gcd(mut a: usize, mut b: usize) -> usize {
        while b > 0 {
            (a, b) = (b, a % b)
        }
        a
    }
}
fn main() {
    let nums1 = vec![1, 2, 3, 4];
    assert_eq!(10, Solution::subsequence_pair_count(nums1));

    let nums2 = vec![10, 20, 30];
    assert_eq!(2, Solution::subsequence_pair_count(nums2));

    let nums3 = vec![1, 1, 1, 1];
    assert_eq!(50, Solution::subsequence_pair_count(nums3));
}
