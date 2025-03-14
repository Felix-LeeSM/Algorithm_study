struct Solution;
impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        if let None = nums.iter().find(|&&x| x == 1) {
            let mut parents = (0..100_001).collect::<Vec<_>>();
            let nums = nums.into_iter().map(|num| num as usize).collect::<Vec<_>>();
            let primes = Self::primes_up_to_good(100_001);

            let mut total_used_primes = std::collections::HashSet::new();

            let mut visited = vec![false; 100_001];

            for &num in nums.iter() {
                let mut num = num;
                if visited[num] {
                    continue;
                } else {
                    visited[num] = true
                }

                let mut used_primes = vec![];
                for &prime in primes.iter() {
                    if prime > num {
                        break;
                    }
                    if num % prime == 0 {
                        while num % prime == 0 {
                            num /= prime;
                        }
                        used_primes.push(prime);

                        total_used_primes.insert(prime);
                    }
                }

                if used_primes.len() >= 2 {
                    for idx in 0..(used_primes.len() - 1) {
                        Self::union_parent(&mut parents, used_primes[idx], used_primes[idx + 1]);
                    }
                }
            }

            if total_used_primes.len() == 1 {
                true
            } else {
                let mut total_used_primes = total_used_primes.into_iter();

                let one = total_used_primes.next().unwrap();
                let parent = Self::get_parent(&mut parents, one);

                for another in total_used_primes {
                    if parent != Self::get_parent(&mut parents, another) {
                        return false;
                    }
                }

                true
            }
        } else {
            false
        }
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

    pub fn primes_up_to_good(number: usize) -> Vec<usize> {
        let mut is_prime = vec![true; number + 1];
        is_prime[0] = false;
        is_prime[1] = false;

        for num in 2..=number {
            if is_prime[num] {
                for not_prime in ((2 * num)..=number).step_by(num) {
                    is_prime[not_prime] = false;
                }
            }
        }

        is_prime
            .into_iter()
            .enumerate()
            .filter_map(|(num, is_prime)| if is_prime { Some(num) } else { None })
            .collect::<Vec<_>>()
    }
}
fn main() {
    assert_eq!(true, Solution::can_traverse_all_pairs(vec![2, 3, 6]));
    assert_eq!(false, Solution::can_traverse_all_pairs(vec![3, 9, 5]));
    assert_eq!(true, Solution::can_traverse_all_pairs(vec![4, 3, 12, 8]));
}
