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
    let mut input = input::<isize, Vec<_>, VecDeque<_>>();

    let n = input.pop_front().unwrap()[0] as usize;

    let mut solutions = input.pop_front().unwrap();
    solutions.sort();

    let (mut left, mut right) = (0, n - 1);
    let mut answer = (solutions[left], solutions[right]);

    while left < right {
        if (solutions[left] + solutions[right]).abs() < (answer.0 + answer.1).abs() {
            answer = (solutions[left], solutions[right]);
        }

        if (solutions[left + 1] + solutions[right]).abs()
            <= (solutions[left] + solutions[right - 1]).abs()
        {
            left += 1
        } else {
            right -= 1
        }
    }

    println!("{} {}", answer.0, answer.1);
}
