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

    let n = input.pop_front().unwrap()[0];

    let costs = input
        .drain(0..n)
        .map(|line| [line[0], line[1], line[2]])
        .collect::<Vec<_>>();

    let mut answer = usize::MAX;

    for i in 0..3 {
        let mut dp = vec![[Option::None; 3]; n];
        dp[0][i] = Some(costs[0][i]);

        for house in 1..n {
            dp[house][0] =
                option_min(dp[house - 1][1], dp[house - 1][2]).map(|val| val + costs[house][0]);
            dp[house][1] =
                option_min(dp[house - 1][0], dp[house - 1][2]).map(|val| val + costs[house][1]);
            dp[house][2] =
                option_min(dp[house - 1][0], dp[house - 1][1]).map(|val| val + costs[house][2]);
        }

        dp[n - 1][i] = None;

        option_min(option_min(dp[n - 1][0], dp[n - 1][1]), dp[n - 1][2])
            .map(|val| answer = answer.min(val));
    }

    println!("{}", answer);
}

fn option_min<T: Ord>(one: Option<T>, two: Option<T>) -> Option<T> {
    match (one, two) {
        (Some(one), Some(two)) => Some(one.min(two)),
        (Some(one), None) => Some(one),
        (None, Some(two)) => Some(two),
        (None, None) => None,
    }
}
