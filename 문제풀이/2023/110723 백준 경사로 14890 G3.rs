use std::{
    collections::VecDeque,
    io::{self},
};

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
    let mut input = input();
    let nl = input.pop_front().unwrap();
    let (n, l) = (nl[0], nl[1]);

    let graph = input;

    let mut answer = 0_usize;

    for r in 0..n {
        let mut last_height = graph[r][0];
        let mut count: i32 = 1;

        for c in 1..n {
            let height = graph[r][c];
            if height == last_height {
                count += 1;
                continue;
            }

            if height == last_height + 1 {
                if count >= l as i32 {
                    count = 1;
                    last_height = height;
                } else {
                    count = -1;
                    break;
                }
                continue;
            }

            if height + 1 == last_height && count >= 0 {
                count = -(l as i32) + 1;
                last_height = height;
                continue;
            }

            count = -1;
            break;
        }

        if count >= 0 {
            answer += 1;
        }
    }

    for c in 0..n {
        let mut last_height = graph[0][c];
        let mut count: i32 = 1;

        for r in 1..n {
            let height = graph[r][c];
            if height == last_height {
                count += 1;
                continue;
            }
            if height == last_height + 1 {
                if count >= l as i32 {
                    count = 1;
                    last_height = height;
                } else {
                    count = -1;
                    break;
                }
                continue;
            }

            if height + 1 == last_height && count >= 0 {
                count = -(l as i32) + 1;
                last_height = height;
                continue;
            }

            count = -1;
            break;
        }

        if count >= 0 {
            answer += 1;
        }
    }

    println!("{}", answer)
}
