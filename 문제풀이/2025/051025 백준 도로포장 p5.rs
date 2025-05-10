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

type Edge = (usize, usize, usize);

fn solve(n: usize, k: usize, edges: Vec<Edge>) -> usize {
    let mut dp = vec![vec![INF; n + 1]; k + 1];

    let mut graph = vec![vec![]; n + 1];

    for (one, two, dist) in edges {
        graph[one].push((two, dist));
        graph[two].push((one, dist));
    }

    let mut queue = BinaryHeap::new();
    queue.push((Reverse(0), 1, k));
    dp[k][1] = 0;

    while let Some((Reverse(curr_dist), node, left)) = queue.pop() {
        if node == n {
            continue;
        }

        if dp[left][node] < curr_dist {
            continue;
        }

        for &(next_node, new_dist) in &graph[node] {
            if 0 < left {
                if curr_dist < dp[left - 1][next_node] {
                    dp[left - 1][next_node] = curr_dist;
                    queue.push((Reverse(curr_dist), next_node, left - 1));
                }
            }

            let next_dist = curr_dist + new_dist;
            if next_dist < dp[left][next_node] {
                dp[left][next_node] = next_dist;
                queue.push((Reverse(next_dist), next_node, left));
            }
        }
    }

    dp.into_iter().map(|dists| dists[n]).min().unwrap()
}

fn main() {
    assert_eq!(
        1,
        solve(4, 1, vec![(1, 2, 10), (2, 4, 10), (1, 3, 1), (3, 4, 100),])
    );

    let mut input = input::<usize, Vec<_>, VecDeque<_>>();

    let line = input.pop_front().unwrap();
    let (n, m, k) = (line[0], line[1], line[2]);

    let edges = input
        .drain(0..m)
        .map(|edge| (edge[0], edge[1], edge[2]))
        .collect::<Vec<_>>();

    let answer = solve(n, k, edges);

    println!("{}", answer)
}
