struct Solution;
impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals
            .into_iter()
            .map(|interval| (interval[0], interval[1]))
            .collect::<Vec<_>>();

        intervals.sort();

        let mut groups: std::collections::BinaryHeap<std::cmp::Reverse<i32>> =
            std::collections::BinaryHeap::new();

        for (start, end) in intervals {
            if let Some(&std::cmp::Reverse(last_end)) = groups.peek() {
                if start > last_end {
                    groups.pop();
                }
            }
            groups.push(std::cmp::Reverse(end));
        }

        groups.len() as i32
    }
}

fn main() {
    assert_eq!(
        Solution::min_groups(vec![vec![1, 2], vec![2, 3], vec![2, 5]]),
        3
    );
    assert_eq!(
        Solution::min_groups(vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![4, 5]]),
        2
    );
    assert_eq!(
        Solution::min_groups(vec![vec![1, 2], vec![1, 2], vec![1, 2]]),
        3
    );
    assert_eq!(
        Solution::min_groups(vec![
            vec![5, 10],
            vec![6, 8],
            vec![1, 5],
            vec![2, 3],
            vec![1, 10]
        ]),
        3
    );
    assert_eq!(
        Solution::min_groups(vec![vec![1, 3], vec![5, 6], vec![8, 10], vec![11, 13]]),
        1
    );
}
