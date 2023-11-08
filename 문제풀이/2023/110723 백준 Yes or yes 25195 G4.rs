use core::panic;
use std::{
    collections::{HashSet, VecDeque},
    fmt::Debug,
    io::{self},
    str::FromStr,
};

fn input<T: FromStr>() -> VecDeque<Vec<T>>
where
    <T as FromStr>::Err: Debug,
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
    let ne = input.pop_front().unwrap();
    let (nodes, edges) = (ne[0], ne[1]);

    let mut graph: Vec<Vec<usize>> = vec![vec![]; nodes];
    (0..edges).for_each(|_| {
        let edge = input.pop_front().unwrap();
        let (from, to) = (edge[0] - 1, edge[1] - 1);
        graph[from].push(to);
    });

    let fans: HashSet<usize> = HashSet::from_iter(input.pop_back().unwrap().iter().map(|x| x - 1));

    let mut queue: VecDeque<usize> = VecDeque::new();
    let mut answer = 1;
    queue.push_back(0);

    while !queue.is_empty() {
        let node = queue.pop_front().unwrap();

        if fans.contains(&node) {
            continue;
        }

        if graph[node].len() == 0 {
            answer = 0;
            break;
        }

        for nxt in graph[node].iter() {
            if !fans.contains(nxt) {
                queue.push_back(*nxt);
            }
        }
    }

    match answer {
        0 => print!("yes"),
        1 => print!("Yes"),
        _ => panic!("IMPOSSIBLE"),
    }
}
