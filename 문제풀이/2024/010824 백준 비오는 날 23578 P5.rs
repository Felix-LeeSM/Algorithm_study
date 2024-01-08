
use std::{
    cmp::Reverse,
    collections::{BinaryHeap, VecDeque},
    iter::FromIterator,
    str::FromStr,
};

#[derive(Eq, PartialEq)]
struct Node {
    students: usize,
    degree: usize,
}

impl Node {
    fn next(&self) -> Self {
        Self {
            students: self.students,
            degree: self.degree + 1,
        }
    }

    fn next_cost(&self) -> usize {
        self.students * (self.degree + 1).pow(2)
    }

    fn curr_cost(&self) -> usize {
        self.students * self.degree.pow(2)
    }
}

impl Ord for Node {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        (self.next_cost() - self.curr_const()).cmp(&other.next_cost())
    }
}
impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.next_cost().cmp(&other.next_cost()))
    }
}

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

    let n = input.pop_front().unwrap().pop().unwrap();
    let students = input.pop_front().unwrap();

    if n == 1 {
        return println!("0");
    }

    let mut heap = BinaryHeap::new();
    for &student in students.iter() {
        heap.push(Reverse(Node {
            students: student,
            degree: 1,
        }));
    }

    let mut sum = students.into_iter().sum::<usize>();

    for _ in 0..(n - 2) {
        if let Some(Reverse(node)) = heap.pop() {
            sum += node.next_cost();
            sum -= node.curr_cost();

            heap.push(Reverse(node.next()));
        }
    }

    println!("{}", sum);
}
