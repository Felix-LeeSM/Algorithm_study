struct Solution;

impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        let mut prev: Vec<usize> = vec![0; s.len()];

        let mut indexes: Vec<Vec<usize>> = vec![vec![]; 26];

        for index in indexes.iter_mut() {
            index.push(0)
        }
        for (i, ch) in s.chars().enumerate() {
            indexes[ch as usize - 97].push(i + 1)
        }

        let len = s.len();

        for index in indexes.into_iter() {
            for j in 1..(index.len()) {
                let prev_idx = index[j - 1];
                let curr_idx = index[j];

                prev[curr_idx - 1] = prev_idx;
            }
        }

        let mut ret = 0_usize;
        for i in 0..s.len() {
            let nth = i + 1;
            ret += (nth - prev[i]) * (len + 1 - nth)
        }

        ret as i64
    }
}
fn main() {
    assert!(Solution::appeal_sum("abbca".to_string()) == 28);
    assert!(Solution::appeal_sum("code".to_string()) == 20);
}
