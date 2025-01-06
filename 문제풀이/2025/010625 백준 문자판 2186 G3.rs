use std::collections::VecDeque;

const DIRECTION: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

fn main() {
    let input = std::io::read_to_string(std::io::stdin()).expect("PARSE_ERROR");
    let mut input: VecDeque<_> = input.trim().split('\n').collect();

    let line = input
        .pop_front()
        .unwrap()
        .split(' ')
        .map(|str| str.parse::<usize>().unwrap())
        .collect::<Vec<usize>>();

    let (n, m, k) = (line[0], line[1], line[2]);

    let board: Vec<Vec<_>> = input
        .drain(0..n)
        .map(|line| line.chars().collect())
        .collect();

    let word: Vec<_> = input.pop_front().unwrap().chars().collect();

    let mut dps = vec![vec![vec![0_usize; m]; n]; word.len()];

    for x in 0..n {
        for y in 0..m {
            if board[x][y] == word[0] {
                dps[0][x][y] = 1;
            }
        }
    }

    for turn in 1..word.len() {
        let prev = turn - 1;

        for x in 0..n {
            for y in 0..m {
                let curr_cases = dps[prev][x][y];
                if curr_cases == 0 {
                    continue;
                }

                for jump in 1..(k + 1) {
                    for &(dx, dy) in DIRECTION.iter() {
                        let nx = x as isize + dx * jump as isize;
                        let ny = y as isize + dy * jump as isize;

                        if nx < 0 || nx >= n as isize || ny < 0 || ny >= m as isize {
                            continue;
                        }

                        let (nx, ny) = (nx as usize, ny as usize);

                        if board[nx][ny] == word[turn] {
                            dps[turn][nx][ny] += curr_cases;
                        }
                    }
                }
            }
        }
    }

    let answer = dps
        .last()
        .unwrap()
        .into_iter()
        .map(|line| line.into_iter().sum::<usize>())
        .sum::<usize>();

    println!("{}", answer);
}
