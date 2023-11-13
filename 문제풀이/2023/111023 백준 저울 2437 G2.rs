use std::{
    collections::{BinaryHeap, HashSet, VecDeque},
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

    let mut weights = input.pop_front().unwrap();
    weights.sort();

    let mut impossible_weight = 1;

    for weight in weights {
        if weight > impossible_weight {
            break;
        }

        impossible_weight += weight
    }

    println!("{}", impossible_weight);
}
