use std::cmp::Reverse;
use std::collections::{BinaryHeap, VecDeque};

fn parse<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>>(line: &str) -> T2
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    line.trim()
        .split_ascii_whitespace()
        .map(|word| T1::from_str(word).unwrap())
        .collect()
}

fn input<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>, T3: std::iter::FromIterator<T2>>(
) -> T3
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(parse::<T1, T2>)
        .collect::<T3>()
}

const INF: usize = usize::MAX / 2;

fn solve(nodes: usize, start: usize, end: usize, edges: Vec<Vec<usize>>) -> isize {
    let mut graph = vec![vec![]; nodes];
    let mut rev_graph = vec![vec![]; nodes];

    edges
        .into_iter()
        .map(|line| (line[0], line[1], line[2]))
        .for_each(|(fr, to, dist)| {
            graph[fr].push((to, dist));
            rev_graph[to].push((fr, dist))
        });

    let mut dists = vec![INF; nodes];
    dists[start] = 0;
    let mut rev_dists = vec![INF; nodes];
    rev_dists[end] = 0;

    let mut queue: BinaryHeap<(std::cmp::Reverse<usize>, usize)> = BinaryHeap::new();

    queue.push((Reverse(0), start));

    while let Some((Reverse(curr_dist), node)) = queue.pop() {
        if dists[node] < curr_dist {
            continue;
        }

        for &(next, dist) in &graph[node] {
            let next_dist = curr_dist + dist;
            if next_dist < dists[next] {
                dists[next] = next_dist;
                queue.push((Reverse(next_dist), next));
            }
        }
    }

    queue.push((Reverse(0), end));

    while let Some((Reverse(curr_dist), node)) = queue.pop() {
        if rev_dists[node] < curr_dist {
            continue;
        }

        for &(next, dist) in &rev_graph[node] {
            let next_dist = curr_dist + dist;
            if next_dist < rev_dists[next] {
                rev_dists[next] = next_dist;
                queue.push((Reverse(next_dist), next));
            }
        }
    }

    let mut final_dists = vec![INF; nodes];
    final_dists[start] = 0;
    queue.push((Reverse(0), start));

    while let Some((Reverse(curr_dist), node)) = queue.pop() {
        if node == end {
            break;
        }

        if final_dists[node] < curr_dist {
            continue;
        }

        for &(next, dist) in &graph[node] {
            let next_dist = curr_dist + dist;

            if next_dist < final_dists[next] && dists[end] != dists[node] + dist + rev_dists[next] {
                final_dists[next] = next_dist;
                queue.push((Reverse(next_dist), next));
            }
        }
    }

    if final_dists[end] != INF {
        final_dists[end] as isize
    } else {
        -1
    }
}

fn main() {
    assert_eq!(
        5,
        solve(
            7,
            0,
            6,
            vec![
                vec![0, 1, 1],
                vec![0, 2, 1],
                vec![0, 3, 2],
                vec![0, 4, 3],
                vec![1, 5, 2],
                vec![2, 6, 4],
                vec![3, 6, 2],
                vec![4, 6, 4],
                vec![5, 6, 1]
            ]
        )
    );
    assert_eq!(
        -1,
        solve(
            4,
            0,
            2,
            vec![
                vec![0, 1, 1],
                vec![1, 2, 1],
                vec![1, 3, 1],
                vec![3, 2, 1],
                vec![2, 0, 3],
                vec![3, 0, 2],
            ]
        )
    );
    assert_eq!(
        6,
        solve(
            6,
            0,
            1,
            vec![
                vec![0, 1, 1],
                vec![0, 2, 2],
                vec![0, 3, 3],
                vec![2, 5, 3],
                vec![3, 4, 2],
                vec![4, 1, 1],
                vec![5, 1, 1],
                vec![3, 0, 1],
            ]
        )
    );

    assert_eq!(
        5,
        solve(
            6,
            0,
            5,
            vec![
                vec![0, 1, 2],
                vec![1, 2, 1],
                vec![0, 2, 2],
                vec![1, 3, 2],
                vec![2, 3, 2],
                vec![3, 5, 1],
                vec![2, 5, 2],
                vec![2, 4, 1],
                vec![4, 5, 2],
            ]
        )
    );

    let mut input = input::<usize, Vec<_>, VecDeque<_>>();

    let mut answer: Vec<isize> = vec![];

    loop {
        let line = input.pop_front().unwrap();
        let (n, m) = (line[0], line[1]);

        if n == 0 && m == 0 {
            break;
        }

        let line = input.pop_front().unwrap();
        let (start, end) = (line[0], line[1]);

        let edges = input.drain(0..m).collect::<Vec<_>>();

        answer.push(solve(n, start, end, edges));
    }

    println!(
        "{}",
        answer
            .into_iter()
            .map(|num| num.to_string())
            .collect::<Vec<_>>()
            .join("\n")
    )
}
