// https://www.acmicpc.net/problem/17071
use std::collections::{HashSet, VecDeque};
use std::io::{self};

fn input() -> VecDeque<Vec<usize>> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|line| {
            line.split(' ')
                .map(|string| string.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

fn main() {
    let line = input().pop_front().unwrap();
    let n = line[0];
    let mut k = line[1];

    let mut traces = [[false; 2]; 500_001];
    traces[n][0] = true;

    let mut positions: VecDeque<HashSet<usize>> =
        VecDeque::from([HashSet::from([n]), HashSet::new()]);

    for time in 0_usize.. {
        let mut current_positions = positions.pop_front().unwrap();
        let next_positions = positions.front_mut().unwrap();

        k += time;

        if k > 500_000 {
            print!("-1");
            break;
        }
        if traces[k][time % 2] {
            println!("{}", time);
            break;
        }

        current_positions.iter().for_each(|x| {
            if *x > 0 && !traces[x - 1][(time + 1) % 2] {
                traces[x - 1][(time + 1) % 2] = true;
                next_positions.insert(x - 1);
            }

            if *x < 500_000 && !traces[x + 1][(time + 1) % 2] {
                traces[x + 1][(time + 1) % 2] = true;
                next_positions.insert(x + 1);
            }

            if 2 * x <= 500_000 && !traces[2 * x][(time + 1) % 2] {
                traces[2 * x][(time + 1) % 2] = true;
                next_positions.insert(2 * x);
            }
        });

        current_positions.clear();

        positions.push_back(current_positions);
    }
}
