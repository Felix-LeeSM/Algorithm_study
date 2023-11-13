use std::{
    collections::{BinaryHeap, VecDeque},
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
            line.split(' ')
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

fn main() {
    let mut input = input::<usize>();

    let n = input.pop_front().unwrap()[0];

    let mut assignments_on_days: Vec<Vec<usize>> = vec![vec![]; 1001];
    let mut current_possible: BinaryHeap<usize> = BinaryHeap::new();

    input
        .iter()
        .for_each(|x| assignments_on_days[x[0]].push(x[1]));

    let mut result = 0;
    assignments_on_days
        .into_iter()
        .skip(1)
        .rev()
        .for_each(|assignments| {
            current_possible.extend(assignments);
            if let Some(x) = current_possible.pop() {
                result += x;
            }
        });

    println!("{}", result);
}
