struct Solution;

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let (n, m) = (grid.len(), grid[0].len());

        let mut end_grid = vec![vec![-100_000; m]; n];

        for x in (0..n).rev() {
            for y in (0..m).rev() {
                let mut curr = end_grid[x][y];
                if x < n - 1 {
                    curr = curr.max(end_grid[x + 1][y]).max(grid[x + 1][y])
                }

                if y < m - 1 {
                    curr = curr.max(end_grid[x][y + 1]).max(grid[x][y + 1])
                }

                end_grid[x][y] = curr;
            }
        }

        let mut answer = i32::MIN;

        for x in 0..n {
            for y in 0..m {
                answer = answer.max(end_grid[x][y] - grid[x][y])
            }
        }

        answer
    }
}

fn main() {
    assert_eq!(
        9,
        Solution::max_score(vec![
            vec![9, 5, 7, 3],
            vec![8, 9, 6, 1],
            vec![6, 7, 14, 3],
            vec![2, 5, 3, 1]
        ])
    );
    assert_eq!(-1, Solution::max_score(vec![vec![4, 3, 2], vec![3, 2, 1]]))
}
