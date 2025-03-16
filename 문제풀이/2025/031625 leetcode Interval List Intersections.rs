struct Solution;

impl Solution {
    pub fn interval_intersection(
        first_list: Vec<Vec<i32>>,
        second_list: Vec<Vec<i32>>,
    ) -> Vec<Vec<i32>> {
        let mut times = first_list
            .into_iter()
            .chain(second_list)
            .map(|time| (time[0], time[1]))
            .collect::<Vec<_>>();

        times.sort();

        let mut prev_end = -1;
        let mut overlaps = vec![];

        for (start, end) in times {
            if start <= prev_end {
                overlaps.push(vec![start, end.min(prev_end)]);
                prev_end = end.max(prev_end);
            } else {
                prev_end = end;
            }
        }

        overlaps
    }
}

fn main() {
    assert_eq!(
        vec![
            vec![1, 2],
            vec![5, 5],
            vec![8, 10],
            vec![15, 23],
            vec![24, 24],
            vec![25, 25]
        ],
        Solution::interval_intersection(
            vec![vec![0, 2], vec![5, 10], vec![13, 23], vec![24, 25]],
            vec![vec![1, 5], vec![8, 12], vec![15, 24], vec![25, 26]]
        )
    );

    assert_eq!(
        vec![],
        Solution::interval_intersection(vec![vec![1, 3], vec![5, 9]], vec![])
    );
}
