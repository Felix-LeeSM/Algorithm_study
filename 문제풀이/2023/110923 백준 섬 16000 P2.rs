use std::{
    collections::{HashSet, VecDeque},
    io::{self},
    vec,
};

fn input() -> VecDeque<String> {
    io::read_to_string(io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| line.trim().to_string())
        .collect::<VecDeque<_>>()
}

const DIRECTIONS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, 1), (0, -1)];

#[derive(Clone, Copy, Debug)]
enum Cell {
    Land(usize),
    Ocean(usize),
    Unknown,
}

#[derive(Clone, Copy, Debug)]
enum State {
    Safe,
    Dangerous,
    Unknown(usize),
}

fn conjugate(
    n: usize,
    m: usize,
    x: usize,
    y: usize,
    curr_ocean: &mut usize,
    curr_land: &mut usize,
    raw_board: &Vec<Vec<char>>,
    board: &mut Vec<Vec<Cell>>,
    ocean_to_land: &mut Vec<HashSet<usize>>,
    land_to_ocean: &mut Vec<HashSet<usize>>,
) {
    if raw_board[x][y] == '.' {
        board[x][y] = Cell::Ocean(*curr_ocean);
        ocean_to_land.push(HashSet::new());
        *curr_ocean += 1;
    } else {
        board[x][y] = Cell::Land(*curr_land);
        land_to_ocean.push(HashSet::new());
        *curr_land += 1;
    };

    let mut queue = VecDeque::new();
    queue.push_back((x, y));

    while let Some((i, j)) = queue.pop_front() {
        for (di, dj) in DIRECTIONS {
            let (ni, nj) = (i as isize + di, j as isize + dj);

            if ni < 0 || nj < 0 {
                continue;
            }
            let (ni, nj) = (ni as usize, nj as usize);
            if ni >= n || nj >= m {
                continue;
            }
            match (board[i][j], board[ni][nj], raw_board[ni][nj]) {
                (Cell::Ocean(ocean_id), Cell::Unknown, '.') => {
                    board[ni][nj] = Cell::Ocean(ocean_id);
                    queue.push_back((ni, nj));
                }
                (Cell::Land(land_id), Cell::Unknown, '#') => {
                    board[ni][nj] = Cell::Land(land_id);
                    queue.push_back((ni, nj));
                }
                (Cell::Ocean(ocean_id), Cell::Land(land_id), _)
                | (Cell::Land(land_id), Cell::Ocean(ocean_id), _) => {
                    ocean_to_land[ocean_id].insert(land_id);
                    land_to_ocean[land_id].insert(ocean_id);
                }
                _ => (),
            };
        }
    }
}

fn main() {
    let mut input = input();

    let nm = input
        .pop_front()
        .expect("NO FIRST LINE")
        .split(' ')
        .map(|x| x.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    let raw_board: Vec<Vec<char>> = input
        .into_iter()
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let (n, m) = (nm[0], nm[1]);

    let mut board: Vec<Vec<Cell>> = vec![vec![Cell::Unknown; m]; n];
    let mut curr_ocean: usize = 0_usize;
    let mut curr_land: usize = 0_usize;

    let mut ocean_to_land: Vec<HashSet<usize>> = vec![];
    let mut land_to_ocean: Vec<HashSet<usize>> = vec![];

    for i in 0..n {
        for j in 0..m {
            match board[i][j] {
                Cell::Unknown => conjugate(
                    n,
                    m,
                    i,
                    j,
                    &mut curr_ocean,
                    &mut curr_land,
                    &raw_board,
                    &mut board,
                    &mut ocean_to_land,
                    &mut land_to_ocean,
                ),
                _ => (),
            }
        }
    }

    let mut ocean_states = vec![State::Dangerous; curr_ocean];
    let mut land_states = vec![State::Dangerous; curr_land];

    let mut queue = VecDeque::new();
    ocean_states[0] = State::Safe;
    queue.push_back(Cell::Ocean(0));

    while let Some(element) = queue.pop_front() {
        match element {
            Cell::Ocean(ocean_id) => {
                for &land_id in ocean_to_land[ocean_id].iter() {
                    match (ocean_states[ocean_id], land_states[land_id]) {
                        (State::Safe, State::Dangerous) => {
                            land_states[land_id] = State::Safe;
                            queue.push_back(Cell::Land(land_id));
                        }
                        (State::Safe, State::Unknown(_)) => {
                            land_states[land_id] = State::Safe;
                            queue.push_back(Cell::Land(land_id));
                        }
                        _ => (),
                    }
                }
                ()
            }
            Cell::Land(land_id) => {
                for &ocean_id in land_to_ocean[land_id].iter() {
                    match (land_states[land_id], ocean_states[ocean_id]) {
                        (State::Safe, State::Dangerous) => {
                            ocean_states[ocean_id] = State::Unknown(land_id)
                        }
                        (State::Safe, State::Unknown(l_id)) if l_id != land_id => {
                            ocean_states[ocean_id] = State::Safe;
                            queue.push_back(Cell::Ocean(ocean_id));
                        }
                        _ => (),
                    }
                }
            }
            _ => panic!("Cell::Unknown in queue"),
        }
    }

    let output = board
        .into_iter()
        .map(|line| {
            line.into_iter()
                .map(|cell| match cell {
                    Cell::Land(land_id) => match land_states[land_id] {
                        State::Safe => 'O',
                        _ => 'X',
                    },
                    Cell::Ocean(_) => '.',
                    _ => panic!("Cell::Unknown in board"),
                })
                .collect::<String>()
        })
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", output);
}
