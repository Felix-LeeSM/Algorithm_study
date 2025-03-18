struct Solution;

impl Solution {
    pub fn largest_vals_from_labels(
        values: Vec<i32>,
        labels: Vec<i32>,
        num_wanted: i32,
        use_limit: i32,
    ) -> i32 {
        let mut num_wanted = num_wanted;
        let mut pairs = values
            .into_iter()
            .zip(labels.into_iter().map(|label| label as usize))
            .collect::<Vec<_>>();

        pairs.sort_unstable_by_key(|&pair| std::cmp::Reverse(pair));

        let mut visited = [0; 20_001];
        let mut answer = 0;

        for (num, label) in pairs {
            if num_wanted == 0 {
                break;
            }

            if visited[label] < use_limit {
                answer += num;
                visited[label] += 1;
                num_wanted -= 1;
            }
        }

        answer
    }
}
fn main() {
    assert_eq!(
        9,
        Solution::largest_vals_from_labels(vec![5, 4, 3, 2, 1], vec![1, 1, 2, 2, 3], 3, 1)
    );
    assert_eq!(
        12,
        Solution::largest_vals_from_labels(vec![5, 4, 3, 2, 1], vec![1, 3, 3, 3, 2], 3, 2)
    );
    assert_eq!(
        16,
        Solution::largest_vals_from_labels(vec![9, 8, 8, 7, 6], vec![0, 0, 0, 1, 1], 3, 1)
    );
}
