use std::collections::{BinaryHeap, VecDeque};

fn input<T: std::str::FromStr>() -> VecDeque<Vec<T>>
where
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| {
            line.trim()
                .split_ascii_whitespace()
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

fn get_parent(parents: &mut Vec<usize>, x: usize) -> usize {
    if parents[x] != x {
        parents[x] = get_parent(parents, parents[x]);
    }

    parents[x]
}

fn union_parent(parents: &mut Vec<usize>, a: usize, b: usize) {
    let a = get_parent(parents, a);
    let b = get_parent(parents, b);

    if a < b {
        parents[b] = a;
    } else {
        parents[a] = b;
    }
}

fn main() {
    let mut input = input::<usize>();

    let n = input.pop_front().unwrap()[0];

    // (price, date)
    let offers = input
        .drain(..n)
        .map(|offer| (offer[1], offer[0]))
        .collect::<Vec<_>>();

    let mut earned = 0;
    let mut heapq = BinaryHeap::from(offers);

    let mut parents = Vec::from_iter(0..(n + 1));

    while let Some((price, date)) = heapq.pop() {
        let possible_date = get_parent(&mut parents, date);

        if possible_date != 0 {
            earned += price;
            union_parent(&mut parents, possible_date, possible_date - 1);
        }
    }

    println!("{}", earned);
}
