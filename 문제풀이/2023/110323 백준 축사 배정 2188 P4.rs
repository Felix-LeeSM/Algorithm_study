use std::collections::VecDeque;
use std::io::{self};

fn input() -> VecDeque<Vec<usize>> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|line| {
            line.trim()
                .split(' ')
                .map(|string| string.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

fn main() {
    let mut input = input();
    let line = input.pop_front().unwrap();

    let (n, m) = (line[0], line[1]);
    let mut cows: Vec<Vec<usize>> = vec![];

    for _ in 0..n {
        cows.push(
            input
                .pop_front()
                .unwrap()
                .iter()
                .enumerate()
                .filter(|(idx, _)| *idx != 0)
                .map(|(_, cow)| *cow)
                .collect(),
        )
    }

    let mut barns_status: Vec<usize> = vec![usize::MAX; m + 1];

    fn dfs(
        cow: usize,
        cows: &Vec<Vec<usize>>,
        barns_status: &mut Vec<usize>,
        visited: &mut Vec<bool>,
    ) -> bool {
        if visited[cow] {
            return false;
        }
        visited[cow] = true;

        for barn in &cows[cow] {
            if barns_status[*barn] == usize::MAX
                || dfs(barns_status[*barn], cows, barns_status, visited)
            {
                barns_status[*barn] = cow;
                return true;
            }
        }
        return false;
    }

    let mut answer = 0;
    for cow in 0..n {
        let mut visited = vec![false; n + 1];
        if dfs(cow, &cows, &mut barns_status, &mut visited) {
            answer += 1;
        }
    }

    println!("{}", answer);
}
