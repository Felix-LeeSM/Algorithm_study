// https://www.acmicpc.net/problem/1926
use std::collections::VecDeque;
use std::io::{self};

fn input() -> VecDeque<Vec<u16>> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|line| {
            line.split(' ')
                .map(|string| string.parse::<u16>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

const DIRECTIONS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn main() {
    let mut input = input();

    let line = input.pop_front().unwrap();
    let (r, c) = (line[0], line[1]);

    let board = input;
    let mut cnt = 0;
    let mut max = 0;
    let mut visited = vec![vec![false; c as usize]; r as usize];

    for (i, line) in board.iter().enumerate() {
        for (j, v) in line.iter().enumerate() {
            if *v == 1 && !visited[i][j] {
                visited[i][j] = true;
                let mut cur_area = 1;
                let mut stack = vec![(i, j)];

                while !stack.is_empty() {
                    let (x, y) = stack.pop().unwrap();
                    for (dx, dy) in DIRECTIONS {
                        let (nx, ny) = (x as i32 + dx, y as i32 + dy);
                        if nx < 0 || nx >= r as i32 || ny < 0 || ny >= c as i32 {
                            continue;
                        }
                        let (nx, ny) = (nx as usize, ny as usize);
                        if !visited[nx][ny] && board[nx][ny] == 1 {
                            visited[nx][ny] = true;
                            stack.push((nx, ny));
                            cur_area += 1;
                        }
                    }
                }
                max = max.max(cur_area);
                cnt += 1;
            }
        }
    }

    println!("{}\n{}", cnt, max);
}
