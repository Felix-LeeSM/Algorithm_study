use std::{
    collections::{HashSet, VecDeque},
    io::{self},
    ops::Range,
};

fn input() -> String {
    io::read_to_string(io::stdin()).expect("PARSE_ERROR")
    // .trim()
    // .split('\n')
    // .collect::<VecDeque<_>>();
}

const LINE: &str = "........";
const WALL: char = '#';
const BOARD_SIZE: usize = 8;
const DIRECTIONS: [(isize, isize); 9] = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
    (0, 0),
];

fn main() {
    let input = input();
    let mut board = input
        .trim()
        .split('\n')
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect::<VecDeque<_>>();

    let mut queue = VecDeque::from([VecDeque::from([(7_usize, 0_usize)]), VecDeque::new()]);
    let mut answer = 0;

    'solve: loop {
        let mut current_queue = queue.pop_front().unwrap();
        let mut next_queue = queue.pop_front().unwrap();
        let mut visited = vec![vec![false; 8]; 8];

        while !current_queue.is_empty() {
            let (r, c) = current_queue.pop_front().unwrap();
            if board[r][c] == WALL {
                continue;
            }

            for (dr, dc) in DIRECTIONS {
                let (nr, nc) = (r as isize + dr, c as isize + dc);
                if nr < 0 || nr >= BOARD_SIZE as isize || nc < 0 || nc >= BOARD_SIZE as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);

                if nr == 0 && nc == 7 {
                    answer = 1;
                    break 'solve;
                }
                if visited[nr][nc] || board[nr][nc] == WALL {
                    continue;
                }
                visited[nr][nc] = true;
                next_queue.push_back((nr, nc));
            }
        }

        if next_queue.is_empty() {
            break 'solve;
        }

        queue.push_back(next_queue);
        queue.push_back(current_queue);

        board.pop_back();
        board.push_front(LINE.chars().collect::<Vec<_>>());
    }

    println!("{}", answer);
}
