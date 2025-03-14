enum Cell {
    Wall,
    Empty,
    Entrance,
    Exit,
}

struct Solution;
impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let (er, ec) = (entrance[0] as usize, entrance[1] as usize);
        let r = maze.len();
        let c = maze[0].len();

        let map = maze
            .into_iter()
            .enumerate()
            .map(|(row, line)| {
                line.into_iter()
                    .enumerate()
                    .map(|(col, cell)| match (row, col, cell) {
                        (_, _, '+') => Cell::Wall,
                        (x, y, _) if (x == er && y == ec) => Cell::Entrance,
                        (x, _, _) if (x == 0) => Cell::Exit,
                        (_, y, _) if (y == 0) => Cell::Exit,
                        (x, _, _) if (x == r - 1) => Cell::Exit,
                        (_, y, _) if (y == c - 1) => Cell::Exit,
                        (_, _, _) => Cell::Empty,
                    })
                    .collect::<Vec<Cell>>()
            })
            .collect::<Vec<Vec<Cell>>>();

        let mut visited = vec![vec![false; c]; r];
        visited[er][ec] = true;
        let mut queue = std::collections::VecDeque::new();
        queue.push_back((er, ec, 0));
        let mut answer = i32::MAX;

        while let Some((x, y, d)) = queue.pop_front() {
            if x + 1 < r {
                if !visited[x + 1][y] {
                    visited[x + 1][y] = true;
                    match map[x + 1][y] {
                        Cell::Empty => {
                            queue.push_back((x + 1, y, d + 1));
                        }
                        Cell::Entrance => unreachable!(),
                        Cell::Exit => answer = answer.min(d + 1),
                        Cell::Wall => (),
                    }
                }
            }

            if y + 1 < c {
                if !visited[x][y + 1] {
                    visited[x][y + 1] = true;
                    match map[x][y + 1] {
                        Cell::Empty => {
                            queue.push_back((x, y + 1, d + 1));
                        }
                        Cell::Entrance => unreachable!(),
                        Cell::Exit => answer = answer.min(d + 1),
                        Cell::Wall => (),
                    }
                }
            }

            if 0 < y {
                if !visited[x][y - 1] {
                    visited[x][y - 1] = true;
                    match map[x][y - 1] {
                        Cell::Empty => {
                            queue.push_back((x, y - 1, d + 1));
                        }
                        Cell::Entrance => unreachable!(),
                        Cell::Exit => answer = answer.min(d + 1),
                        Cell::Wall => (),
                    }
                }
            }

            if 0 < x {
                if !visited[x - 1][y] {
                    visited[x - 1][y] = true;
                    match map[x - 1][y] {
                        Cell::Empty => {
                            queue.push_back((x - 1, y, d + 1));
                        }
                        Cell::Entrance => unreachable!(),
                        Cell::Exit => answer = answer.min(d + 1),
                        Cell::Wall => (),
                    }
                }
            }
        }

        if answer == i32::MAX {
            -1
        } else {
            answer
        }
    }
}

fn main() {
    assert_eq!(
        1,
        Solution::nearest_exit(
            vec![
                vec!['+', '+', '.', '+'],
                vec!['.', '.', '.', '+'],
                vec!['+', '+', '+', '.'],
            ],
            vec![1, 2],
        )
    );

    assert_eq!(
        2,
        Solution::nearest_exit(
            vec![
                vec!['+', '+', '+'],
                vec!['.', '.', '.'],
                vec!['+', '+', '+'],
            ],
            vec![1, 0],
        )
    );

    assert_eq!(
        -1,
        Solution::nearest_exit(vec![vec!['.', '+'],], vec![0, 0],)
    );

    println!("answer: {}", answer);
}
