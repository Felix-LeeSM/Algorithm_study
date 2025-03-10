struct Solution;
impl Solution {
    pub fn kth_smallest_path(destination: Vec<i32>, k: i32) -> String {
        let mut v_cnt = destination[0] as usize;
        let mut h_cnt = destination[1] as usize;
        let mut k = k as usize;
        let length = v_cnt + h_cnt;

        let mut answer = Vec::new();
        let mut cache = vec![vec![None; 31]; 31];
        for i in 1..31 {
            cache[i][0] = Some(1);
            cache[i][i] = Some(1);
        }

        for _ in 0..length {
            if h_cnt == 0 {
                answer.push("V");
                v_cnt -= 1;
                continue;
            }

            if v_cnt == 0 {
                answer.push("H");
                h_cnt -= 1;
                continue;
            }

            let ways_if_h = Solution::combination(h_cnt + v_cnt - 1, v_cnt, &mut cache);

            if k <= ways_if_h {
                answer.push("H");
                h_cnt -= 1;
            } else {
                answer.push("V");
                v_cnt -= 1;
                k -= ways_if_h;
            }
        }

        answer.join("")
    }

    pub fn combination(n: usize, r: usize, cache: &mut Vec<Vec<Option<usize>>>) -> usize {
        if let Some(combination) = cache[n][r] {
            combination
        } else {
            let combination =
                Solution::combination(n - 1, r, cache) + Solution::combination(n - 1, r - 1, cache);
            cache[n][r] = Some(combination);
            cache[n][n - r] = Some(combination);
            combination
        }
    }
}
fn main() {
    assert_eq!(
        "HHHVV".to_string(),
        Solution::kth_smallest_path(vec![2, 3], 1)
    );
    assert_eq!(
        "HVHHV".to_string(),
        Solution::kth_smallest_path(vec![2, 3], 4)
    );
}
