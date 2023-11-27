use std::{
    cmp::Reverse,
    collections::{BinaryHeap, VecDeque},
    io::{self},
    str::FromStr,
};

fn input<T: FromStr>() -> VecDeque<Vec<T>>
where
    <T as FromStr>::Err: std::fmt::Debug,
{
    io::read_to_string(io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| {
            line.trim()
                .split_ascii_whitespace()
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

const DIRECTIONS: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
fn next_moves(x: usize, y: usize, n: usize) -> Vec<(usize, usize)> {
    DIRECTIONS
        .iter()
        .filter_map(|(dx, dy)| {
            let (nx, ny) = (x as isize + dx, y as isize + dy);
            if nx < 0 || ny < 0 || nx >= n as isize || ny >= n as isize {
                None
            } else {
                Some(((x as isize + dx) as usize, (y as isize + dy) as usize))
            }
        })
        .collect()
}

fn main() {
    let mut input = input::<usize>();
    let n = input.pop_front().unwrap()[0];

    let board = input
        .drain(..)
        .map(|line| line.into_iter().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut visited_min_max: Vec<Vec<Vec<usize>>> = vec![vec![vec![usize::MAX; 200]; n]; n];
    visited_min_max[0][0][board[0][0]] = board[0][0];

    let mut queue = BinaryHeap::new();

    // range, max, min, x, y
    queue.push(Reverse((0_usize, board[0][0], board[0][0], 0, 0)));

    while let Some(Reverse((range, max, min, x, y))) = queue.pop() {
        if x == n - 1 && y == n - 1 {
            println!("{}", range);

            break;
        }
        for (nx, ny) in next_moves(x, y, n) {
            let min = min.min(board[nx][ny]);
            let max = max.max(board[nx][ny]);
            let nrange = max - min;
            if visited_min_max[nx][ny][min] > max {
                visited_min_max[nx][ny][min] = max;
                queue.push(Reverse((nrange, max, min, nx, ny)))
            }
        }
    }
}
