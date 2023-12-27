use std::{collections::VecDeque, iter::FromIterator, str::FromStr};

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

// 서로 다른 노선은 같은 도로를 공유할 수 있다.
// 그러므로 노선을 잘 조율한다면, leaf 노드의 절반만큼의 노선으로 모든 도로를 커버할 수 있다.
// 무지성으로 가장 가까운 곳으로 간다면 물론 안되겠지만, 적절히 먼 노드를 잘 선택하면 가능하다.
fn main() {
    let mut input = input::<usize, Vec<_>>();

    let n = input.pop_front().unwrap()[0];

    let mut graph = vec![0; n];

    for _ in 0..(n - 1) {
        let line = input.pop_front().unwrap();
        let (s, e) = (line[0], line[1]);
        graph[s] += 1;
        graph[e] += 1;
    }

    let answer = (graph.into_iter().filter(|&x| x == 1).count() + 1) / 2;

    println!("{}", answer);
}
