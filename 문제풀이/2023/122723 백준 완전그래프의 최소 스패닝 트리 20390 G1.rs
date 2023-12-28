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

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Cell {
    Connected,
    Unconnected(u128),
}

impl Cell {
    fn distance(&self) -> u128 {
        match self {
            Cell::Connected => 0,
            Cell::Unconnected(dist) => *dist,
        }
    }

    fn from_dist(dist: u128) -> Self {
        Cell::Unconnected(dist)
    }

    fn closer(&self, other: u128) -> bool {
        match self {
            Cell::Connected => false,
            Cell::Unconnected(dist) => *dist < other,
        }
    }
}

fn main() {
    let mut input = input::<u128, Vec<_>>();

    let n = input.pop_front().unwrap()[0];

    let line = input.pop_front().unwrap();
    let (a, b, c, d) = (line[0], line[1], line[2], line[3]);

    let a = a % c;
    let b = b % c;

    let nums = input.pop_front().unwrap();
    let get_dist = |node1: usize, node2: usize| -> u128 {
        if node1 < node2 {
            ((nums[node1] * a + nums[node2] * b) % c) ^ d
        } else {
            ((nums[node2] * a + nums[node1] * b) % c) ^ d
        }
    };

    let mut distances = vec![Cell::Unconnected(u128::MAX); n as usize];
    let mut last_connected = 0;
    let mut answer = 0;

    for _ in 0..(n - 1) {
        distances[last_connected] = Cell::Connected;

        let mut min_dist = u128::MAX;
        let mut min_dist_idx = 0;

        for next in 0..(n as usize) {
            match distances[next] {
                Cell::Connected => continue,
                Cell::Unconnected(prev_dist) => {
                    let curr_dist = get_dist(last_connected, next);

                    if curr_dist < prev_dist {
                        distances[next] = Cell::from_dist(curr_dist);
                    }

                    if distances[next].closer(min_dist) {
                        min_dist = distances[next].distance();
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
