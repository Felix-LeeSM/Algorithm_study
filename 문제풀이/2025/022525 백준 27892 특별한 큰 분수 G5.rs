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

fn main() {
    let mut input = input::<usize, Vec<_>>();

    let line = input.pop_front().unwrap();
    let (start, n) = (line[0], line[1]);

    let next = |an: usize| {
        if an % 2 == 0 {
            (an / 2) ^ 6
        } else {
            (an * 2) ^ 6
        }
    };

    let mut dp: HashMap<usize, usize> = HashMap::new();
    dp.insert(start, 0);

    let mut cycle = 0;
    let mut curr = start;

    'iteration: loop {
        cycle += 1;
        curr = next(curr);

        if dp.contains_key(&curr) {
            let cycle_length = cycle - dp.get(&curr).unwrap();
            let remaining = n - cycle;
            cycle += (remaining / cycle_length) * cycle_length;
        }

        dp.insert(curr, cycle);

        if cycle == n {
            println!("{}", curr);
            break 'iteration;
        }
    }
}
