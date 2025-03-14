struct Solution;
impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let (n, threshold) = (n as usize, threshold as usize + 1);

        let mut parents = (0..=n).collect::<Vec<_>>();

        for num in threshold..=n {
            if Self::get_parent(&mut parents, num) == num {
                for i in 2..=(n / num) {
                    Self::union_parent(&mut parents, num, num * i);
                }
            }
        }

        queries
            .into_iter()
            .map(|query| {
                Self::get_parent(&mut parents, query[0] as usize)
                    == Self::get_parent(&mut parents, query[1] as usize)
            })
            .collect::<Vec<_>>()
    }

    pub fn get_parent(parents: &mut Vec<usize>, node: usize) -> usize {
        let mut curr = node;
        while curr != parents[curr] {
            let parent = parents[curr];
            parents[curr] = parents[parent];
            curr = parent;
        }

        curr
    }

    pub fn union_parent(parents: &mut Vec<usize>, node1: usize, node2: usize) {
        let (parent1, parent2) = (
            Self::get_parent(parents, node1),
            Self::get_parent(parents, node2),
        );

        if parent1 < parent2 {
            parents[parent2] = parent1;
        } else {
            parents[parent1] = parent2;
        }
    }
}

fn main() {
    assert_eq!(
        vec![false, false, true],
        Solution::are_connected(6, 2, vec![vec![1, 4], vec![2, 5], vec![3, 6]])
    );

    assert_eq!(
        vec![true, true, true, true, true],
        Solution::are_connected(
            6,
            0,
            vec![vec![4, 5], vec![3, 4], vec![3, 2], vec![2, 6], vec![1, 3]]
        )
    );

    assert_eq!(
        vec![false, false, false, false, false],
        Solution::are_connected(
            5,
            1,
            vec![vec![4, 5], vec![4, 5], vec![3, 2], vec![2, 3], vec![3, 4]]
        )
    );
}
