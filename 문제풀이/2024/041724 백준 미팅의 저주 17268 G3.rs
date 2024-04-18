// https://www.acmicpc.net/problem/17268

use std::{
    collections::{HashMap, VecDeque},
    iter::FromIterator,
    str::FromStr,
};

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

const DIV: usize = 987654321;

fn solve(num: usize, cache: &mut HashMap<usize, usize>) -> usize {
    if let Some(cached) = cache.get(&num) {
        *cached
    } else {
        let result = (0..(num / 2))
            .map(|i| solve(num - 2 * i - 2, cache) * solve(2 * i, cache) % DIV)
            .sum::<usize>()
            % DIV;

        cache.insert(num, result);

        result
    }
}

fn main() {
    let mut input: VecDeque<Vec<usize>> = input();

    let n = input.pop_front().unwrap()[0];

    let mut cache: HashMap<usize, usize> = HashMap::new();
    cache.insert(0, 1);
    cache.insert(2, 1);
    cache.insert(4, 2);

    let answer = solve(n, &mut cache);

    println!("{}", answer);
}
