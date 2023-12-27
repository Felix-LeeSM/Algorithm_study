use std::{collections::VecDeque, iter::FromIterator, ops::BitXor, str::FromStr};

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

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Cell {
    Connected,
    Unconnected(usize),
}

impl Cell {
    fn distance(&self) -> usize {
        match self {
            Cell::Connected => 0,
            Cell::Unconnected(dist) => *dist,
        }
    }

    fn from_dist(dist: usize) -> Self {
        Cell::Unconnected(dist)
    }
}

fn mul_modulo(a: usize, b: usize, modulo: usize) -> usize {
    let mut res = 0;

    let mut a = a;
    let mut b = b;

    while b > 0 {
        if b & 1 == 1 {
            res = (res + a).rem_euclid(modulo);
        }

        a = (a << 1).rem_euclid(modulo);
        b >>= 1;
    }

    res
}
fn main() {
    let mut input = input::<usize, Vec<_>>();

    let n = input.pop_front().unwrap()[0];

    let line = input.pop_front().unwrap();
    let (a, b, c, d) = (line[0], line[1], line[2], line[3]);
    let a = a % c;
    let b = b % c;

    let nums = input.pop_front().unwrap();
    let get_dist = |node1: usize, node2: usize| -> usize {
        if node1 < node2 {
            ((mul_modulo(nums[node1], a, c) + mul_modulo(nums[node2], b, c)).rem_euclid(c))
                .bitxor(d)
        } else {
            ((mul_modulo(nums[node2], a, c) + mul_modulo(nums[node1], b, c)).rem_euclid(c))
                .bitxor(d)
        }
    };

    let mut distances = vec![Cell::Unconnected(usize::MAX); n];
    let mut last_connected = 0;
    let mut answer = 0;

    for _ in 0..(n - 1) {
        distances[last_connected] = Cell::Connected;

        let mut min_dist = usize::MAX;
        let mut min_dist_idx = 0;

        for next in 0..n {
            match distances[next] {
                Cell::Connected => continue,
                Cell::Unconnected(prev_dist) => {
                    let curr_dist = get_dist(last_connected, next);
                    if curr_dist < prev_dist {
                        distances[next] = Cell::from_dist(curr_dist);
                    }

                    let dist = distances[next].distance();
                    if min_dist > dist {
                        min_dist = dist;
                        min_dist_idx = next;
                    }
                }
            }
        }

        last_connected = min_dist_idx;
        answer += min_dist;
    }

    println!("{}", answer);
}
