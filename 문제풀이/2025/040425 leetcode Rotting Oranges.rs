struct Solution;

#[derive(PartialEq, Clone, Copy, Debug)]
enum Cell {
    Empty,
    Fresh,
    Rotten,
}

impl Cell {
    pub fn from_i32(num: i32) -> Self {
        match num {
            0 => Cell::Empty,
            1 => Cell::Fresh,
            2 => Cell::Rotten,
            _ => unreachable!(),
        }
    }
}

impl Solution {
    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let grid = grid
            .into_iter()
            .map(|line| line.into_iter().map(Cell::from_i32).collect::<Vec<_>>())
            .collect::<Vec<_>>();

        let n = grid.len();
        let m = grid[0].len();

        let mut rottens = vec![];

        for (x, line) in grid.iter().enumerate() {
            for (y, &cell) in line.iter().enumerate() {
                if cell == Cell::Rotten {
                    rottens.push((x, y));
                }
            }
        }

        let mut distances = vec![vec![i32::MAX; m]; n];
        let mut answer = 0;
        let mut queue = std::collections::VecDeque::new();

        for &(x, y) in &rottens {
            distances[x][y] = 0;
            queue.push_back((x, y));
        }

        while let Some((x, y)) = queue.pop_front() {
            let curr_distance = distances[x][y];
            if 0 < x && curr_distance + 1 < distances[x - 1][y] && grid[x - 1][y] == Cell::Fresh {
                distances[x - 1][y] = curr_distance + 1;
                queue.push_back((x - 1, y));
                answer = answer.max(curr_distance + 1);
            }

            if 0 < y && curr_distance + 1 < distances[x][y - 1] && grid[x][y - 1] == Cell::Fresh {
                distances[x][y - 1] = curr_distance + 1;
                queue.push_back((x, y - 1));
                answer = answer.max(curr_distance + 1);
            }

            if x < n - 1 && curr_distance + 1 < distances[x + 1][y] && grid[x + 1][y] == Cell::Fresh
            {
                distances[x + 1][y] = curr_distance + 1;
                queue.push_back((x + 1, y));
                answer = answer.max(curr_distance + 1);
            }

            if y < m - 1 && curr_distance + 1 < distances[x][y + 1] && grid[x][y + 1] == Cell::Fresh
            {
                distances[x][y + 1] = curr_distance + 1;
                queue.push_back((x, y + 1));
                answer = answer.max(curr_distance + 1);
            }
        }

        for (distances, cells) in std::iter::zip(distances, grid) {
            for (distance, cell) in std::iter::zip(distances, cells) {
                if cell == Cell::Fresh && distance == i32::MAX {
                    answer = -1;
                }
            }
        }

        answer
    }
}

fn main() {
    assert_eq!(
        4,
        Solution::oranges_rotting(vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]])
    );
    assert_eq!(
        -1,
        Solution::oranges_rotting(vec![vec![2, 1, 1], vec![0, 1, 1], vec![1, 0, 1]])
    );
    assert_eq!(0, Solution::oranges_rotting(vec![vec![0, 2]]));
}
