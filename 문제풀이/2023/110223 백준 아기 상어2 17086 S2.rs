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
            line.trim()
                .split(' ')
                .map(|string| string.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

const DIR: [(i32, i32); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

fn main() {
    let mut input = input();
    let line = input.pop_front().unwrap();
    let (n, m) = (line[0], line[1]);

    let mut distances: [[usize; 51]; 51] = [[102; 51]; 51];
    let mut board: [[usize; 51]; 51] = [[0; 51]; 51];

    let mut queue: VecDeque<(usize, usize, i32)> = VecDeque::new();
    let mut answer = 0;

    for i in 0..input.len() {
        let line = input.pop_front().unwrap();
        for j in 0..line.len() {
            board[i][j] = line[j];

            if line[j] == 1 {
                distances[i][j] = 0;
                queue.push_back((i, j, 0));
            }
        }
    }

    while !queue.is_empty() {
        let (x, y, distance) = queue.pop_front().unwrap();
        for (dx, dy) in DIR {
            let (nx, ny) = (x as i32 + dx, y as i32 + dy);

            if nx < 0 || nx >= n as i32 || ny < 0 || ny >= m as i32 {
                continue;
            }

            if distances[nx as usize][ny as usize] <= distance as usize + 1 {
                continue;
            }

            distances[nx as usize][ny as usize] = distance as usize + 1;
            queue.push_back((nx as usize, ny as usize, distance + 1));
            answer = answer.max(distance as usize + 1);
        }
    }

    println!("{}", answer)
}
