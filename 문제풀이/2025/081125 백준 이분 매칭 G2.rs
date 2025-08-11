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

    let line = input.pop_front().unwrap();
    let (a, b) = (line[0], line[1]);

    let m = input.pop_front().unwrap()[0];

    let mut answer = a / 2 + b / 2;

    if 0 < (a % 2) * (b % 2)
        && input
            .drain(0..m)
            .find(|line| ((line[0] % 2) * (line[1] % 2)) == 1)
            .is_some()
    {
        answer += 1;
    }

    println!("{}", answer);
}
