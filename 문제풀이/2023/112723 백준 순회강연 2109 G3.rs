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

fn main() {
    let mut input = input::<usize>();

    let n = input.pop_front().unwrap()[0];

    // (price, date)
    let offers = input
        .drain(..n)
        .map(|offer| (offer[0], offer[1]))
        .collect::<Vec<_>>();

    let mut earned = 0;
    let mut heapq = BinaryHeap::from(offers);

    let mut visited = vec![false; 10001];

    while let Some((price, date)) = heapq.pop() {
        let mut date = date;
        while date > 0 && visited[date] {
            date -= 1;
        }

        if date > 0 {
            visited[date] = true;
            earned += price;
        }
    }

    println!("{}", earned);
}
