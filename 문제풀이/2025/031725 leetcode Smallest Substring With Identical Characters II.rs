struct Solution;

impl Solution {
    pub fn min_length(string: String, ops: i32) -> i32 {
        let (mut left, mut right) = (1, string.len() + 1);
        let (fragments, _prev_char, _cnt) = string.chars().chain("9".chars()).fold(
            (vec![], string.chars().next().unwrap(), 0),
            |(mut vec, prv_ch, cnt), ch| {
                if prv_ch == ch {
                    (vec, prv_ch, cnt + 1)
                } else {
                    vec.push(cnt);
                    (vec, ch, 1)
                }
            },
        );
        let chars = string.chars().collect::<Vec<_>>();

        while left < right {
            let mid = (left + right) / 2;

            if Self::op_req(&fragments, &chars, mid) <= ops {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }

    pub fn op_req(fragments: &Vec<usize>, chars: &Vec<char>, limit: usize) -> i32 {
        if limit == 1 {
            let cand = chars
                .iter()
                .map(|&char| char as usize)
                .enumerate()
                .map(|(idx, char)| idx % 2 == char - 48)
                .filter(|&is_fit| is_fit)
                .count();

            cand.min(chars.len() - cand) as i32
        } else {
            fragments
                .iter()
                .map(|fragment| fragment / (limit + 1))
                .map(|ops| ops as i32)
                .sum()
        }
    }
}

fn main() {
    assert_eq!(2, Solution::min_length(String::from("000001"), 1));
    assert_eq!(2, Solution::min_length(String::from("0110"), 1));
    assert_eq!(1, Solution::min_length(String::from("0011"), 2));
}
