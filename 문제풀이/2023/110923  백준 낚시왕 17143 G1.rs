use std::{
    collections::VecDeque,
    fmt::Debug,
    io::{self},
    str::FromStr,
    vec,
};

fn input<T: FromStr>() -> VecDeque<Vec<T>>
where
    <T as FromStr>::Err: Debug,
{
    io::read_to_string(io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| {
            line.split(' ')
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

const DIRECTIONS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, 1), (0, -1)];

#[derive(Debug, Clone, Copy)]
enum Cell {
    Shark {
        direction: isize,
        speed: isize,
        size: isize,
    },
    Empty,
}

impl Cell {
    fn is_empty(&self) -> bool {
        match self {
            Cell::Empty => true,
            _ => false,
        }
    }

    fn size(&self) -> isize {
        match self {
            Cell::Shark { size, .. } => *size,
            _ => panic!("Not a Shark"),
        }
    }
}

fn turn(dir: isize) -> isize {
    match dir {
        0 => 1,
        1 => 0,
        2 => 3,
        3 => 2,
        _ => panic!("Invalid Direction"),
    }
}

fn move_shark(
    r: isize,
    c: isize,
    board: &mut Vec<Vec<Cell>>,
    next_board: &mut Vec<Vec<Cell>>,
) -> () {
    for row in 0..r {
        for col in 0..c {
            if let Cell::Shark {
                direction,
                speed,
                size,
            } = board[row as usize][col as usize]
            {
                board[row as usize][col as usize] = Cell::Empty;
                let (mut cr, mut cc) = (row, col);
                let mut dir = direction;
                for _ in 0..speed {
                    let (dr, dc) = DIRECTIONS[dir as usize];
                    let (mut nr, mut nc) = (cr + dr, cc + dc);

                    if nr < 0 || nr >= r || nc < 0 || nc >= c {
                        dir = turn(dir);
                        let (dr, dc) = DIRECTIONS[dir as usize];
                        (nr, nc) = (cr + dr, cc + dc);
                    }

                    cr = nr;
                    cc = nc;
                }

                match next_board[cr as usize][cc as usize] {
                    Cell::Empty => {
                        next_board[cr as usize][cc as usize] = Cell::Shark {
                            direction: dir,
                            speed,
                            size,
                        }
                    }

                    Cell::Shark { size: s, .. } => {
                        if s < size {
                            next_board[cr as usize][cc as usize] = Cell::Shark {
                                direction: dir,
                                speed,
                                size,
                            }
                        }
                    }
                }
            }
        }
    }
}

fn main() {
    let mut input = input::<isize>();

    let rcm = input.pop_front().unwrap();
    let (r, c, m) = (rcm[0], rcm[1], rcm[2]);

    let mut board = vec![vec![Cell::Empty; c as usize]; r as usize];
    let next_board = vec![vec![Cell::Empty; c as usize]; r as usize];

    for _shark in 0..m {
        let shark = input.pop_front().unwrap();
        let (r_, c_, s, d, z) = (shark[0], shark[1], shark[2], shark[3], shark[4]);
        if d == 1 || d == 2 {
            board[(r_ - 1) as usize][(c_ - 1) as usize] = Cell::Shark {
                direction: d - 1,
                speed: s % (2 * (r - 1)),
                size: z,
            };
        } else if d == 3 || d == 4 {
            board[(r_ - 1) as usize][(c_ - 1) as usize] = Cell::Shark {
                direction: d - 1,
                speed: s % (2 * (c - 1)),
                size: z,
            };
        } else {
            panic!("Invalid Direction")
        }
    }

    let mut boards = VecDeque::new();
    boards.push_back(board);
    boards.push_back(next_board);

    let mut caught = 0;

    for fisherman in 0..c {
        let mut board = boards.pop_front().unwrap();
        let mut next_board = boards.pop_front().unwrap();
        for row in 0..r {
            let cell = board[row as usize][fisherman as usize];
            if !cell.is_empty() {
                caught += cell.size();
                board[row as usize][fisherman as usize] = Cell::Empty;
                break;
            }
        }

        move_shark(r, c, &mut board, &mut next_board);
        boards.push_back(next_board);
        boards.push_back(board);
    }

    println!("{}", caught);
}
