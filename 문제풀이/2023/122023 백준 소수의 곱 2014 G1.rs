use std::{
    collections::{BinaryHeap, VecDeque},
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
    let (_k, n) = (line[0], line[1]);

    let nums: Vec<(isize, usize)> = input
        .pop_front()
        .unwrap()
        .into_iter()
        .enumerate()
        .map(|(idx, num)| (num as isize, idx))
        .collect();

    let mut queue: BinaryHeap<(isize, usize)> =
        BinaryHeap::from_iter(nums.iter().map(|&(num, idx)| (-num, idx)));
    let mut cnt = 0;

    while let Some((num, idx)) = queue.pop() {
        cnt += 1;

        if cnt == n {
            println!("{}", -num);
            break;
        }

        nums[idx..].iter().for_each(|&(n, idx)| {
            queue.push((num * n, idx));
        });
    }
}
