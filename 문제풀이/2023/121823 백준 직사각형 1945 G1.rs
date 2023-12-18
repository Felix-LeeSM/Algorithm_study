use std::collections::{BinaryHeap, VecDeque};

fn input<T: std::str::FromStr>() -> VecDeque<Vec<T>>
where
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| {
            line.trim()
                .split_ascii_whitespace()
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

#[derive(Eq, Debug)]
struct Coord(usize, usize, bool);

impl Ord for Coord {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        let self_inclination = self.1 as f64 / self.0 as f64;
        let other_inclination = other.1 as f64 / other.0 as f64;

        self_inclination.partial_cmp(&other_inclination).unwrap()
    }
}
impl PartialEq for Coord {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0 && self.1 == other.1
    }
}

impl PartialOrd for Coord {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Coord {
    fn incline(&self) -> f64 {
        self.1 as f64 / self.0 as f64
    }
    fn is_start(&self) -> bool {
        self.2
    }
}

fn main() {
    let mut input = input::<usize>();
    let n = input.pop_front().unwrap()[0];

    let mut coord_heap = BinaryHeap::new();

    input.into_iter().for_each(|line| {
        let (x_l, y_d, x_r, y_t) = (line[0], line[1], line[2], line[3]);
        coord_heap.push(Coord(x_l, y_t, true));
        coord_heap.push(Coord(x_r, y_d, false));
    });

    let mut maximum = 0_usize;
    let mut current = 0_usize;

    while let Some(coord) = coord_heap.pop() {
        let Coord(x, y, is_start) = coord;

        if is_start {
            current += 1;
            maximum = maximum.max(current);
        } else {
            current -= 1;
        }
    }

    println!("{}", maximum);
}
