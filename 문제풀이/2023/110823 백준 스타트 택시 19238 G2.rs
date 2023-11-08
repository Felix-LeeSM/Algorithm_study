use core::panic;
use std::{
    collections::VecDeque,
    fmt::Debug,
    io::{self},
    str::FromStr,
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

const DIRECTIONS: [(isize, isize); 4] = [(-1, 0), (0, -1), (0, 1), (1, 0)];
const INFINITY: usize = 999_999;

#[derive(Debug)]
enum Cell {
    Empty,
    Wall,
    // (현재 x, 현재 y, 목적지 x, 목적지 y)
    Passenger(usize, usize, usize, usize),
}

fn in_board(dx: &isize, dy: &isize, x: usize, y: usize, n: usize) -> bool {
    let (nx, ny) = (x as isize + dx, y as isize + dy);

    if nx < 0 || ny < 0 || nx >= n as isize || ny >= n as isize {
        return false;
    }

    true
}

fn gas_usage(board: &Vec<Vec<Cell>>, fr: (usize, usize), to: (usize, usize)) -> usize {
    if fr.0 == to.0 && fr.1 == to.1 {
        return 0;
    }
    let length = board.len();
    let mut queue: VecDeque<(usize, usize, usize)> = VecDeque::new();
    let mut visited: Vec<Vec<bool>> = vec![vec![false; length]; length];

    queue.push_back((fr.0, fr.1, 0));
    visited[fr.0][fr.1] = true;

    while !queue.is_empty() {
        let (x, y, gas) = queue.pop_front().unwrap();

        for (dx, dy) in DIRECTIONS
            .iter()
            .filter(|(dx, dy)| in_board(dx, dy, x, y, length))
        {
            let (nx, ny) = ((x as isize + dx) as usize, (y as isize + dy) as usize);

            if visited[nx][ny] {
                continue;
            }
            visited[nx][ny] = true;

            if nx == to.0 && ny == to.1 {
                return gas + 1;
            }

            match board[nx][ny] {
                Cell::Wall => continue,
                _ => queue.push_back((nx, ny, gas + 1)),
            }
        }
    }

    INFINITY
}

fn close_passenger(board: &Vec<Vec<Cell>>, fr: (usize, usize)) -> (usize, Cell) {
    if let Cell::Passenger(_start_x, _start_y, x, y) = board[fr.0][fr.1] {
        return (0, Cell::Passenger(_start_x, _start_y, x, y));
    }

    let length = board.len();
    let mut queue: VecDeque<(usize, usize, usize)> = VecDeque::new();
    let mut visited: Vec<Vec<bool>> = vec![vec![false; length]; length];

    let mut closest = INFINITY;
    let mut closest_passenger = Cell::Passenger(INFINITY, INFINITY, INFINITY, INFINITY);

    queue.push_back((fr.0, fr.1, 0));
    visited[fr.0][fr.1] = true;

    while !queue.is_empty() {
        let (x, y, distance) = queue.pop_front().unwrap();

        if distance >= closest {
            break;
        }

        for (dx, dy) in DIRECTIONS
            .iter()
            .filter(|(dx, dy)| in_board(dx, dy, x, y, length))
        {
            let (nx, ny) = ((x as isize + dx) as usize, (y as isize + dy) as usize);

            if visited[nx][ny] {
                continue;
            }
            visited[nx][ny] = true;

            match board[nx][ny] {
                Cell::Wall => continue,
                Cell::Passenger(fr_x, fr_y, end_x, end_y) => {
                    if distance + 1 == closest {
                        if let Cell::Passenger(_fr_x, _fr_y, _end_x, _end_y) = closest_passenger {
                            if fr_x < _fr_x {
                                closest_passenger = Cell::Passenger(fr_x, fr_y, end_x, end_y);
                            } else if fr_x == _fr_x && fr_y < _fr_y {
                                closest_passenger = Cell::Passenger(fr_x, fr_y, end_x, end_y);
                            }
                        } else {
                            panic!("INVALID CLOSEST PASSENGER")
                        }
                    } else {
                        closest = distance + 1;
                        closest_passenger = Cell::Passenger(fr_x, fr_y, end_x, end_y);
                    }
                }
                _ => queue.push_back((nx, ny, distance + 1)),
            }
        }
    }

    (closest, closest_passenger)
}

fn main() {
    let mut input = input::<usize>();

    let nmg = input.pop_front().unwrap();
    let (n, m, gas) = (nmg[0], nmg[1], nmg[2]);
    let mut current_gas: isize = gas as isize;

    let mut board = input
        .drain(..n)
        .map(|line| {
            line.into_iter()
                .map(|cell| match cell {
                    0 => Cell::Empty,
                    1 => Cell::Wall,
                    _ => panic!("INVALID_CELL"),
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let position = input.pop_front().unwrap();
    let (mut x, mut y) = (position[0] - 1, position[1] - 1);

    input.into_iter().for_each(|line| {
        board[line[0] - 1][line[1] - 1] =
            Cell::Passenger(line[0] - 1, line[1] - 1, line[2] - 1, line[3] - 1);
    });

    for _case in 0..m {
        if let (to_passenger, Cell::Passenger(fr_x, fr_y, nx, ny)) = close_passenger(&board, (x, y))
        {
            if nx == INFINITY && ny == INFINITY {
                println!("-1");
                return;
            }
            board[fr_x][fr_y] = Cell::Empty;

            current_gas -= to_passenger as isize;

            if 0 > current_gas {
                println!("-1");
                return;
            }

            let consumption = gas_usage(&board, (fr_x, fr_y), (nx, ny));

            current_gas -= consumption as isize;

            if 0 > current_gas {
                println!("-1");
                return;
            }

            current_gas += 2 * consumption as isize;
            x = nx;
            y = ny;
        } else {
            panic!("INVALID_PASSENGER_LOGIC")
        }
    }

    println!("{}", current_gas);
}
