use std::collections::VecDeque;

const DIRECTIONS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

#[derive(Copy, Clone)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn from_usize(n: usize) -> Self {
        match n {
            1 => Self::Right,
            2 => Self::Left,
            3 => Self::Down,
            4 => Self::Up,
            _ => panic!("Invalid direction"),
        }
    }

    fn to_vector(direction: Direction) -> (isize, isize) {
        match direction {
            Self::Up => (-1, 0),
            Self::Down => (1, 0),
            Self::Left => (0, -1),
            Self::Right => (0, 1),
        }
    }
}

fn main() {
    assert_eq!(
        Solution::min_cost(vec![
            vec![1, 1, 1, 1],
            vec![2, 2, 2, 2],
            vec![1, 1, 1, 1],
            vec![2, 2, 2, 2]
        ]),
        3
    );
    assert_eq!(
        Solution::min_cost(vec![vec![1, 1, 3], vec![3, 2, 2], vec![1, 1, 4]]),
        0
    );
    assert_eq!(Solution::min_cost(vec![vec![1, 2], vec![4, 3]]), 1);
}

struct Solution;
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let board: Vec<Vec<_>> = grid
            .into_iter()
            .map(|row| {
                row.into_iter()
                    .map(|x| x as usize)
                    .map(Direction::from_usize)
                    .collect()
            })
            .collect();

        let n = board.len();
        let m = board[0].len();

        let mut visited = vec![vec![i32::MAX; m]; n];
        visited[0][0] = 0;

        let mut queues = VecDeque::new();
        let mut current_queue = VecDeque::new();
        current_queue.push_back((0, 0, 0));
        queues.push_back(current_queue);
        queues.push_back(VecDeque::new());

        loop {
            let mut current_queue: VecDeque<(usize, usize, i32)> = queues.pop_front().unwrap();
            let mut next_queue = queues.pop_front().unwrap();
            if current_queue.is_empty() {
                queues.push_back(next_queue);
                queues.push_back(current_queue);
                continue;
            }

            let (x, y, c) = current_queue.pop_front().unwrap();
            if x == n - 1 && y == m - 1 {
                break c;
            }

            let dir: Direction = board[x][y];
            let (cdx, cdy) = Direction::to_vector(dir);

            for (dx, dy) in DIRECTIONS.iter().copied() {
                let (nx, ny) = (x as isize + dx, y as isize + dy);
                if nx < 0 || ny < 0 || nx >= n as isize || ny >= m as isize {
                    continue;
                }

                let (nx, ny) = (nx as usize, ny as usize);
                let cost: i32 = if dx == cdx && dy == cdy { 0 } else { 1 };

                if visited[nx][ny] > c + cost {
                    visited[nx][ny] = c + cost;
                    if cost == 0 {
                        current_queue.push_front((nx, ny, c));
                    } else {
                        next_queue.push_back((nx, ny, c + 1));
                    }
                }
            }

            queues.push_back(current_queue);
            queues.push_back(next_queue);
        }
    }
}
