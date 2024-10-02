struct Solution;
impl Solution {
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let mut counts = vec![0; k as usize];
        arr.into_iter()
            .for_each(|num| counts[num.rem_euclid(k) as usize] += 1);

        let k = k as usize;
        for num in 1..k {
            if counts[k - num] != counts[num] {
                return false;
            }
        }

        if k % 2 == 0 && (counts[k / 2] % 2 != 0 || counts[0] % 2 != 0) {
            false
        } else {
            true
        }
    }
}
