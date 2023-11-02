use std::{collections::VecDeque, io};

fn input() -> VecDeque<Vec<i32>> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split("\n")
        .map(|line| {
            line.trim()
                .split(" ")
                .map(|string| string.parse::<i32>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

fn main() {
    let mut input = input();

    let test_cases = input.pop_front().unwrap().pop().unwrap();
    let mut dp = vec![(1, 0), (0, 1)];

    for _each_case in 0..test_cases {
        let n = input.pop_front().unwrap().pop().unwrap();

        loop {
            if dp.len() > n as usize {
                let (zero, one) = dp[n as usize];
                println!("{zero} {one}");
                break;
            }

            let (last_zero, last_one) = dp[dp.len() - 1];
            let (prev_zero, prev_one) = dp[dp.len() - 2];
            dp.push((last_zero + prev_zero, last_one + prev_one));
        }
    }
}
