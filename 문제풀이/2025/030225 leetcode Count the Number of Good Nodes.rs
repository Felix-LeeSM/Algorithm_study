struct Solution;
impl Solution {
    pub fn count_good_nodes(edges: Vec<Vec<i32>>) -> i32 {
        let edges: Vec<Vec<usize>> = edges
            .into_iter()
            .map(|edge| edge.into_iter().map(|num| num as usize).collect())
            .collect();
        let mut children_count = vec![0; edges.len() + 1];
        let mut tree = vec![vec![]; edges.len() + 1];
        let mut graph = vec![vec![]; edges.len() + 1];
        let mut visited = vec![false; edges.len() + 1];
        let mut stack = vec![0];

        visited[0] = true;

        for edge in edges {
            graph[edge[0]].push(edge[1]);
            graph[edge[1]].push(edge[0]);
        }

        while let Some(node) = stack.pop() {
            for &next in &graph[node] {
                if !visited[next] {
                    visited[next] = true;
                    tree[node].push(next);
                    stack.push(next);
                }
            }
        }

        fn dfs_children_count(
            node: usize,
            tree: &Vec<Vec<usize>>,
            children_count: &mut Vec<usize>,
        ) -> usize {
            let mut children = 1;
            for node in tree[node as usize].iter() {
                children += dfs_children_count(*node, tree, children_count);
            }
            children_count[node] = children - 1;
            children
        }
        dfs_children_count(0, &tree, &mut children_count);

        fn dfs_good_node(
            node: usize,
            tree: &Vec<Vec<usize>>,
            children_count: &Vec<usize>,
        ) -> usize {
            if tree[node].is_empty() {
                1
            } else {
                tree[node]
                    .iter()
                    .map(|&node| dfs_good_node(node, tree, children_count))
                    .sum::<usize>()
                    + if tree[node]
                        .iter()
                        .map(|&node| children_count[node])
                        .collect::<std::collections::HashSet<_>>()
                        .iter()
                        .len()
                        == 1
                    {
                        1
                    } else {
                        0
                    }
            }
        }
        dfs_good_node(0, &tree, &children_count) as i32
    }
}

fn main() {
    Solution::count_good_nodes(vec![
        vec![0, 1],
        vec![0, 2],
        vec![1, 3],
        vec![1, 4],
        vec![2, 5],
        vec![2, 6],
    ]);
}
