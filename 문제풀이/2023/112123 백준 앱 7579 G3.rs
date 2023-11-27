use std::{
    collections::VecDeque,
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

fn main() {
    let mut input = input::<usize>();
    let n_m = input.pop_front().unwrap();
    let (n, m) = (n_m[0], n_m[1]);

    let gains = input.pop_front().unwrap();
    let costs = input.pop_front().unwrap();

    let length = costs.iter().fold(1, |acc, curr| acc + curr);

    let mut dp = vec![vec![0; length]; n];

    let (gain, cost) = (gains[0], costs[0]);
    for budget in cost..length {
        dp[0][budget] = gain;
    }

    for idx in 1..n {
        let (gain, cost) = (gains[idx], costs[idx]);

        for budget in 0..cost {
            dp[idx][budget] = dp[idx - 1][budget];
        }

        for budget in cost..length {
            dp[idx][budget] = dp[idx - 1][budget].max(dp[idx - 1][budget - cost] + gain);
        }
    }

    let answer = dp
        .pop()
        .unwrap()
        .into_iter()
        .position(|memory| memory >= m)
        .unwrap();

    println!("{answer}");
}
