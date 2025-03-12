struct Query(usize, usize);

struct Solution;
impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let (n, threshold) = (n as usize, threshold as usize + 1);
        let pseduo_primes = Self::get_pseudo_primes(n, threshold);

        let mut parents = (0..=n).collect::<Vec<_>>();

        for num in pseduo_primes {
            for i in 2..=(n / num) {
                Self::union_parent(&mut parents, num, num * i);
            }
        }

        queries
            .into_iter()
            .map(|query| Query(query[0] as usize, query[1] as usize))
            .map(|Query(one, another)| {
                Self::get_parent(&mut parents, one) == Self::get_parent(&mut parents, another)
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

    pub fn get_pseudo_primes(num: usize, threshold: usize) -> Vec<usize> {
        let mut seive = vec![true; num + 1];

        for i in threshold..=num {
            if seive[i] {
                for not_prime in ((2 * i)..=num).step_by(i) {
                    seive[not_prime] = false;
                }
            }
        }

        for i in 1..threshold {
            seive[i] = false;
        }

        seive
            .into_iter()
            .enumerate()
            .skip(1)
            .filter(|&(_num, is_prime)| is_prime)
            .map(|(num, _is_prime)| num)
            .collect::<Vec<_>>()
    }
}

// [0, 1, 1, 2, 3, 4]
// [0, 1, 1, 2, 3, 3]
// [0, 1, 1, 2, 2, 3]
// [0, 1, 1, 1, 2, 3]
// [0, 1, 1, 1, 2, 3]
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
