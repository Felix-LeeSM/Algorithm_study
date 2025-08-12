use std::collections::VecDeque;

fn parse<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>>(line: &str) -> T2
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    line.trim()
        .split_ascii_whitespace()
        .map(|word| T1::from_str(word).unwrap())
        .collect()
}

fn input<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>, T3: std::iter::FromIterator<T2>>(
) -> T3
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(parse::<T1, T2>)
        .collect::<T3>()
}


fn main() {
    let mut input = input::<usize, Vec<_>, VecDeque<_>>();
    let mut answers = vec![];

    loop {
        let line = input.pop_front().unwrap();

        let (n, m) = (line[0], line[1]);

        if n == 0 || m == 0 {
            break;
        }

        let board = input
            .drain(0..n)
            .collect::<Vec<Vec<_>>>();

        let answer = solve(n, m, board);
        answers.push(answer);
    }

    println!(
        "{}",
        answers
            .into_iter()
            .map(|num| num.to_string())
            .collect::<Vec<_>>()
            .join("\n")
    )
}

fn solve(n: usize, m: usize, board: Vec<Vec<usize>>) -> usize {
    let mut dp = vec![vec![0; m]; n];

    for i in 0..n {
        if board[i][0] == 1 {
            dp[i][0] = 1
        }
    }

    for j in 0..m {
        if board[0][j] == 1 {
            dp[0][j] = 1
        }
    }

    for i in 1..n {
        for j in 1..m {
            if board[i][j] == 1 {
                dp[i][j] = dp[i-1][j].min(dp[i][j-1]).min(dp[i-1][j-1]) + 1
            }
        }
    }

    dp.into_iter().map(|line| line.into_iter().max().unwrap()).max().unwrap()
}