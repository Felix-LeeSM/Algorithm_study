use std::collections::VecDeque;
use std::io::{self};

fn input() -> VecDeque<String> {
    io::read_to_string(io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|line| String::from(line))
        .collect()
}

const DELTA_ROWS: [i32; 3] = [-1, 0, 1];

fn main() {
    let mut input = input();
    let line = input
        .pop_front()
        .unwrap()
        .split(' ')
        .map(|string| string.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    let (row, col) = (line[0], line[1]);

    let board = input
        .iter()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<_>>();

    let mut visited: Vec<Vec<bool>> = vec![vec![false; col]; row];

    fn dfs(
        r: usize,
        c: usize,
        goal: usize,
        visited: &mut Vec<Vec<bool>>,
        board: &Vec<Vec<char>>,
    ) -> usize {
        visited[r][c] = true;
        if c == goal {
            return 1;
        }

        for delta_row in DELTA_ROWS.iter() {
            let next_r = r as i32 + delta_row;
            if next_r < board.len() as i32 && next_r >= 0 {
                let next_r = next_r as usize;
                if !visited[next_r][c + 1] && board[next_r][c + 1] == '.' {
                    visited[next_r][c + 1] = true;
                    if dfs(next_r, c + 1, goal, visited, board) == 1 {
                        return 1;
                    }
                }
            }
        }

        0
    }

    let answer: usize = (0..row)
        .map(|r| dfs(r, 0, col - 1, &mut visited, &board))
        .sum();

    println!("{:?}", answer)
}
