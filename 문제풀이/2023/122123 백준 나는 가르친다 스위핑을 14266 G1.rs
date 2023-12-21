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

#[derive(PartialEq, PartialOrd, Debug)]
struct NotNaN(f64);
impl Eq for NotNaN {}
impl Ord for NotNaN {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(other).unwrap()
    }
}

fn main() {
    let mut input = input::<usize, Vec<_>>();

    let n = input.pop_front().unwrap()[0];

    let mut heap = BinaryHeap::new();

    input.drain(0..n).for_each(|line| {
        let (x_1, y_1, x_2, y_2) = (line[0], line[1], line[2], line[3]);

        let incli1 = NotNaN(y_1 as f64 / x_1 as f64);
        let incli2 = NotNaN(y_2 as f64 / x_2 as f64);

        if incli1 >= incli2 {
            heap.push((incli1, 1));
            heap.push((incli2, -1));
        } else {
            heap.push((incli1, -1));
            heap.push((incli2, 1));
        }
    });

    let mut curr_count = 0;
    let mut answer = 0;
    while let Some((_, var)) = heap.pop() {
        curr_count += var;
        answer = answer.max(curr_count);
    }

    println!("{}", answer);
}
