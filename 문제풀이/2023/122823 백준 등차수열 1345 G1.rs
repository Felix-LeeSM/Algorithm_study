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
    let mut input = input::<isize, Vec<_>>();

    let line = input.pop_front().unwrap();
    let (n, a0) = (line[0], line[1]);

    if n == 0 {
        println!("0");
        return;
    }

    let sequence = input.pop_front().unwrap();

    let mut sequence = sequence.into_iter().map(|num| num - a0);

    let mut minimum = 0.0;
    let mut maximum = f64::MAX;

    for n in 1..(n + 1) {
        let n = n as f64;
        let nd = sequence.next().unwrap();

        let min = nd as f64 / n;
        let max = (nd + 1) as f64 / n;

        if min > minimum {
            minimum = min;
        }
        if max < maximum {
            maximum = max;
        }
    }

    if maximum > minimum {
        println!("{}", minimum);
    } else {
        println!("-1");
    }
}
