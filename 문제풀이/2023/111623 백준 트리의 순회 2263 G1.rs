use std::{
    collections::VecDeque,
    io::{self},
    str::FromStr,
};

fn input<T: FromStr>() -> VecDeque<Vec<T>>
where
    <T as FromStr>::Err: std::fmt::Debug,
{
    io::read_to_string(io::stdin())
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

fn main() {
    let mut input = input::<usize>();

    let n = input.pop_front().unwrap()[0];

    let in_order = input.pop_front().unwrap();
    let post_order = input.pop_front().unwrap();

    let mut output: Vec<usize> = vec![];

    search(&in_order, (0, n), &post_order, (0, n), &mut output);

    println!(
        "{}",
        output
            .into_iter()
            .map(|num| num.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}

fn search(
    in_order: &Vec<usize>,
    (in_start, in_end): (usize, usize),
    post_order: &Vec<usize>,
    (post_start, post_end): (usize, usize),
    output: &mut Vec<usize>,
) {
    if in_start >= in_end || post_start >= post_end {
        return;
    }

    let root = post_order[post_end - 1];
    output.push(root);

    let mut in_mid: usize = 0;
    for idx in in_start..in_end {
        if in_order[idx] == root {
            in_mid = idx;
            break;
        }
    }

    let left_length = in_mid - in_start;

    let left_in_start = in_start;
    let left_in_end = left_in_start + left_length;
    let left_post_start = post_start;
    let left_post_end = post_start + left_length;

    let right_in_start = in_mid + 1;
    let right_in_end = in_end;
    let right_post_start = left_post_end;
    let right_post_end = post_end - 1;

    search(
        in_order,
        (left_in_start, left_in_end),
        post_order,
        (left_post_start, left_post_end),
        output,
    );

    search(
        in_order,
        (right_in_start, right_in_end),
        post_order,
        (right_post_start, right_post_end),
        output,
    )
}
