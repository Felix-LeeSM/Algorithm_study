use std::{
    collections::VecDeque,
    io::{self},
};

fn main() {
    let input = io::read_to_string(io::stdin()).unwrap();

    let mut histograms = input
        .trim()
        .split_ascii_whitespace()
        .skip(1)
        .map(|str| str.parse::<isize>().unwrap())
        .collect::<VecDeque<_>>();

    histograms.push_back(0);
    histograms.push_front(0);

    let mut stack = vec![(0, -1)];

    let mut maximum = 0;

    for (cur, &height) in histograms.iter().enumerate().skip(1) {
        while let Some(&(_, prev_height)) = stack.last() {
            if prev_height < height {
                break;
            } else {
                let (_, prev_height) = stack.pop().unwrap();
                let &(prev, _) = stack.last().unwrap();

                let width = cur - prev - 1;
                let area = width * prev_height as usize;
                maximum = maximum.max(area);
            }
        }

        stack.push((cur, height));
    }

    println!("{}", maximum)
}
