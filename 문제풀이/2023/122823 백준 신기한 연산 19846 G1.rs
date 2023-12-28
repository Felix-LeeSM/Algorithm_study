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

const MAP: [char; 26] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
];

fn main() {
    let mut input = input::<usize, Vec<_>>();

    let line = input.pop_front().unwrap();

    let (kinds, length, _queries) = (line[0], line[1], line[2]);

    let mut answer = String::new();

    for &char in MAP
        .iter()
        .take(kinds)
        .flat_map(|char| [char, char])
        .cycle()
        .take(length)
    {
        answer.push(char);
    }

    println!("{}", answer);
}
