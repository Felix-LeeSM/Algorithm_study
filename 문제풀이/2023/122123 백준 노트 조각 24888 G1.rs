use std::{
    cmp::Reverse,
    collections::{BinaryHeap, VecDeque},
    iter::FromIterator,
    str::FromStr,
};

fn parse<T1: FromStr, T2: FromIterator<T1>>(line: &str) -> T2
where
    <T1 as FromStr>::Err: std::fmt::Debug,
{
    line.trim()
        .split_ascii_whitespace()
        .map(|word| T1::from_str(word).unwrap())
        .collect()
}

fn input<T1: FromStr, T2: FromIterator<T1>>() -> VecDeque<T2>
where
    <T1 as FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(parse::<T1, T2>)
        .collect::<VecDeque<_>>()
}

const INF: usize = usize::MAX;

fn main() {
    let mut input = input::<usize, Vec<_>>();

    let n_m = input.pop_front().unwrap();
    let (n, m) = (n_m[0], n_m[1]);
    drop(n_m);

    let mut graph = vec![vec![]; n + 1];
    input.drain(0..m).for_each(|edge| {
        let (u, v, w) = (edge[0], edge[1], edge[2]);
        graph[u].push((v, w));
        graph[v].push((u, w));
    });

    let notes = input.pop_back().unwrap();
    let notes = vec![vec![0], notes].concat();
    drop(input);

    let (start, end) = (1, n);

    let mut from = vec![0; n + 1];
    let mut retrieved_at = notes.clone();

    let mut queue = BinaryHeap::new();
    let mut distances = vec![std::usize::MAX; n + 1];
    distances[start] = 0;

    queue.push(Reverse((0, start)));

    while let Some(Reverse((dist, node))) = queue.pop() {
        if distances[node] < dist {
            continue;
        }

        for &(next, weight) in graph[node].iter() {
            let next_dist = dist + weight;
            let next_retrieved = retrieved_at[node] + notes[next];

            if next_dist < distances[next] {
                distances[next] = next_dist;
                queue.push(Reverse((next_dist, next)));

                retrieved_at[next] = next_retrieved;
                from[next] = node;
            } else if next_dist == distances[next] && next_retrieved > retrieved_at[next] {
                queue.push(Reverse((next_dist, next)));

                retrieved_at[next] = next_retrieved;
                from[next] = node;
            }
        }
    }

    let to_retrieve: usize = notes.into_iter().sum();

    if distances[end] == INF || to_retrieve != retrieved_at[end] {
        println!("-1");
    } else {
        let mut path = vec![];
        let mut node = end;
        while node != start {
            path.push(node);
            node = from[node];
        }
        path.push(start);
        path.reverse();

        println!("{}", path.len());
        println!(
            "{}",
            path.iter()
                .map(|node| node.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        );
    }
}
