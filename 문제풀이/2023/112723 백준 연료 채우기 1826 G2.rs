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
    // 거리 가스 순
    let mut stations = input
        .drain(..n)
        .map(|line| (line[0], line[1]))
        .collect::<Vec<_>>();

    let town_gas = input.pop_front().unwrap();
    let (town_distance, initial_gas) = (town_gas[0], town_gas[1]);

    let mut heapq = BinaryHeap::new();
    stations.sort_unstable_by_key(|&station| station.0);

    let mut current_gas = initial_gas;
    let mut stopped = 0;
    let mut station_idx = 0;

    'sol: for (distance, quantity) in stations {
        while current_gas < distance {
            if let Some(max_quantity) = heapq.pop() {
                current_gas += max_quantity;
                stopped += 1;
            } else {
                break 'sol;
            }
        }

        heapq.push(quantity);
    }

    while current_gas < town_distance {
        if let Some(max_quantity) = heapq.pop() {
            current_gas += max_quantity;
            stopped += 1;
        } else {
            break;
        }
    }

    if current_gas < town_distance {
        println!("-1");
    } else {
        println!("{}", stopped);
    }
}
