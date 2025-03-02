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

fn build_tree(nodes: usize, root: usize, graph: Vec<Vec<usize>>) -> Vec<Vec<usize>> {
    let mut tree = vec![vec![]; nodes + 1];
    let mut stack = vec![root];
    let mut visited = vec![false; nodes + 1];
    visited[root] = true;

    while let Some(node) = stack.pop() {
        for &next in &graph[node] {
            if !visited[next] {
                visited[next] = true;
                tree[node].push(next);
                stack.push(next);
            }
        }
    }
    tree
}

fn max(tree: &Vec<Vec<usize>>, node: usize, values: &mut Vec<Option<usize>>) -> usize {
    let max = tree[node]
        .iter()
        .map(|&node| {
            if let Some(val) = values[node] {
                val
            } else {
                min(tree, node, values)
            }
        })
        .max()
        .unwrap_or(0);

    values[node] = Some(max);
    max
}

fn min(tree: &Vec<Vec<usize>>, node: usize, values: &mut Vec<Option<usize>>) -> usize {
    let min = tree[node]
        .iter()
        .map(|&node| {
            if let Some(val) = values[node] {
                val
            } else {
                max(tree, node, values)
            }
        })
        .min()
        .unwrap_or(0);

    values[node] = Some(min);
    min
}

fn main() {
    let mut input = input::<usize, Vec<_>, std::collections::VecDeque<_>>();

    let line = input.pop_front().unwrap();

    let (nodes, root) = (line[0], line[1]);
    let mut graph = vec![vec![]; nodes + 1];

    (0..(nodes - 1)).for_each(|_| {
        let line = input.pop_front().unwrap();
        let (u, v) = (line[0], line[1]);
        graph[u].push(v);
        graph[v].push(u);
    });

    let line = input.pop_front().unwrap();
    let l = line[0];

    let mut values = vec![None; nodes + 1];

    (0..l).for_each(|_| {
        let line = input.pop_front().unwrap();
        let (node, val) = (line[0], line[1]);
        values[node] = Some(val);
    });

    let tree = build_tree(nodes, root, graph);
    max(&tree, root, &mut values);

    let line = input.pop_front().unwrap();
    let q = line[0];

    let ret = (0..q)
        .map(|_| {
            let line = input.pop_front().unwrap();

            values[line[0]].unwrap().to_string()
        })
        .fold(String::new(), |mut acc, b| {
            acc.push_str(&b);
            acc.push('\n');

            acc
        });

    print!("{}", ret);
}
