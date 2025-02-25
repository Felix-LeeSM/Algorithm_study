use std::{collections::VecDeque, iter::FromIterator, str::FromStr};

fn parse<T1: FromStr, T2: FromIterator<T1>>(line: &str) -> T2
where
    <T1 as FromStr>::Err: std::fmt::Debug,
{
    line.trim()
        .split_ascii_whitespace()
        .map(|word| T1::from_str(word).unwrap())
        .collect()
}

fn input<T1: FromStr, T2: FromIterator<T1>>() -> VecDeque<T2>
where
    <T1 as FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(parse::<T1, T2>)
        .collect::<VecDeque<_>>()
}

fn main() {
    let mut input = input::<usize, Vec<_>>();

    let n: usize = input.pop_front().unwrap().pop().unwrap();
    let board: Vec<Vec<usize>> = input.drain(..n).collect::<Vec<_>>();
    let mut target = vec![vec![false; n]; n];
    let mut dp = vec![vec![[0, 0]; n]; n];
    dp[0][0][0] = board[0][0];

    let p: usize = input.pop_front().unwrap().pop().unwrap();
    input
        .drain(..p)
        .map(|coordinate| (coordinate[0], coordinate[1]))
        .for_each(|(x, y)| target[x - 1][y - 1] = true);

    let mut queue = VecDeque::new();
    queue.push_back((0, 0, false));

    while let Some((x, y, did_visit)) = queue.pop_front() {
        [(0, 1), (1, 0)]
            .iter()
            .map(|(dx, dy)| (x + dx, y + dy))
            .filter(|&(nx, ny)| nx < n && ny < n)
            .for_each(|(nx, ny)| match (did_visit, target[nx][ny]) {
                (false, false) => {
                    if dp[nx][ny][0] < dp[x][y][0] + board[nx][ny] {
                        dp[nx][ny][0] = dp[x][y][0] + board[nx][ny];
                        queue.push_back((nx, ny, false));
                    }
                }
                (false, true) => {
                    if dp[nx][ny][0] < dp[x][y][0] + board[nx][ny] {
                        dp[nx][ny][0] = dp[x][y][0] + board[nx][ny];
                    }
                    if dp[nx][ny][1] < dp[x][y][0] + board[nx][ny] {
                        dp[nx][ny][1] = dp[x][y][0] + board[nx][ny];
                        queue.push_back((nx, ny, true));
                    }
                }

                (true, false) => {
                    if dp[nx][ny][0] < dp[x][y][0] + board[nx][ny] {
                        dp[nx][ny][0] = dp[x][y][0] + board[nx][ny];
                    }
                    if dp[nx][ny][1] < dp[x][y][1] + board[nx][ny] {
                        dp[nx][ny][1] = dp[x][y][1] + board[nx][ny];
                        queue.push_back((nx, ny, true));
                    }
                }

                (true, true) => {
                    if dp[nx][ny][0] < dp[x][y][0] + board[nx][ny] {
                        dp[nx][ny][0] = dp[x][y][0] + board[nx][ny];
                    }
                    if dp[nx][ny][1] < dp[x][y][1] + board[nx][ny] {
                        dp[nx][ny][1] = dp[x][y][1] + board[nx][ny];
                        queue.push_back((nx, ny, true));
                    }
                }
            });
    }

    // dp.iter().for_each(|row| println!("{:?}", row));
    // board.iter().for_each(|row| println!("{:?}", row));

    println!("{}", dp[n - 1][n - 1][1]);
}
