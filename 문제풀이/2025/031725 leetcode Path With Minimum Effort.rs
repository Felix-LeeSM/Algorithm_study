struct Solution;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let (n, m) = (heights.len(), heights[0].len());

        let mut efforts = vec![vec![i32::MAX; m]; n];
        efforts[0][0] = 0;

        let mut queue: std::collections::BinaryHeap<(std::cmp::Reverse<i32>, usize, usize)> =
            std::collections::BinaryHeap::new();

        queue.push((std::cmp::Reverse(0), 0, 0));

        while let Some(next) = queue.pop() {
            let (std::cmp::Reverse(effort), x, y) = next;

            for (nx, ny) in Self::next_coords(x, y, n, m) {
                let new_effort = (heights[nx][ny] - heights[x][y]).abs().max(effort);

                if efforts[nx][ny] > new_effort {
                    efforts[nx][ny] = new_effort;
                    queue.push((std::cmp::Reverse(new_effort), nx, ny));
                }
            }
        }

        efforts[n - 1][m - 1]
    }

    pub fn next_coords(x: usize, y: usize, n: usize, m: usize) -> Vec<(usize, usize)> {
        let mut coords = vec![];

        if 0 < x {
            coords.push((x - 1, y))
        }

        if x < n - 1 {
            coords.push((x + 1, y));
        }

        if 0 < y {
            coords.push((x, y - 1))
        }

        if y < m - 1 {
            coords.push((x, y + 1))
        }

        coords
    }
}
fn main() {
    assert_eq!(
        2,
        Solution::minimum_effort_path(vec![vec![1, 2, 2], vec![3, 8, 2], vec![5, 3, 5]])
    );
    assert_eq!(
        1,
        Solution::minimum_effort_path(vec![vec![1, 2, 3], vec![3, 8, 4], vec![5, 3, 5]])
    );
    assert_eq!(
        0,
        Solution::minimum_effort_path(vec![
            vec![1, 2, 1, 1, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 2, 1, 2, 1],
            vec![1, 1, 1, 2, 1]
        ])
    );
    assert_eq!(
        9,
        Solution::minimum_effort_path(vec![vec![1, 10, 6, 7, 9, 10, 4, 9]])
    );
}
