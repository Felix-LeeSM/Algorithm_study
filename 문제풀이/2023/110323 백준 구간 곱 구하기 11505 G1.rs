use std::collections::VecDeque;
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

#[derive(Debug)]
enum Command {
    Query((usize, usize)),
    Mutate((usize, usize)),
}

const MOD: usize = 1_000_000_007;
fn multiply(a: usize, b: usize) -> usize {
    ((a % MOD) * (b % MOD)) % MOD
}

fn main() {
    let mut input = input();
    let line = input.pop_front().unwrap();

    let (n, m, k) = (line[0], line[1], line[2]);

    let mut nums: Vec<usize> = vec![];

    for _ in 0..n {
        nums.push(input.pop_front().unwrap()[0]);
    }

    let mut commands: Vec<Command> = vec![];

    for _ in 0..(m + k) {
        let line = input.pop_front().unwrap();
        let command = line[0];
        let from = line[1];
        let to = line[2];

        match command {
            1 => commands.push(Command::Mutate((from, to))),
            2 => commands.push(Command::Query((from, to))),
            _ => panic!("Invalid command"),
        }
    }

    let mut seg_tree: Vec<usize> = vec![1; n + 1];
    seg_tree.append(&mut nums);
    seg_tree.push(1);

    for idx in (1..(n + 1)).rev() {
        seg_tree[idx] = (seg_tree[idx * 2] * seg_tree[idx * 2 + 1]) % MOD;
    }

    for command in commands {
        if let Command::Mutate((position, value)) = command {
            seg_tree[position + n] = value;
            let mut index = (position + n) / 2;
            while index > 0 {
                seg_tree[index] = multiply(seg_tree[index * 2], seg_tree[index * 2 + 1]);
                index /= 2;
            }
        } else if let Command::Query((from, to)) = command {
            let mut result = 1;
            let mut left = from + n;
            let mut right = to + n;

            while left <= right {
                if left % 2 == 1 {
                    result = multiply(result, seg_tree[left]);
                    left += 1;
                }

                if right % 2 == 0 {
                    result = multiply(result, seg_tree[right]);
                    right -= 1;
                }

                left /= 2;
                right /= 2;
            }

            println!("{}", result);
        }
    }
}
