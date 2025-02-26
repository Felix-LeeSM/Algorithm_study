struct Solution;
impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let mut hash = std::collections::HashMap::new();

        arr.iter()
            .enumerate()
            .for_each(|(idx, &num)| hash.entry(num).or_insert_with(Vec::new).push(idx));

        let mut distances = vec![usize::MAX; arr.len()];

        let mut queue = std::collections::BinaryHeap::new();
        queue.push((usize::MAX, 0));

        while let Some((neg_distnace, idx)) = queue.pop() {
            let distance = usize::MAX - neg_distnace;

            if idx == arr.len() - 1 {
                return distance as i32;
            }

            hash.remove(&arr[idx])
                .unwrap_or(vec![])
                .into_iter()
                .chain(if idx > 0 {
                    vec![idx - 1, idx + 1]
                } else {
                    vec![idx + 1]
                })
                .for_each(|next| {
                    if next < arr.len() && distances[next] > distance + 1 {
                        distances[next] = distance + 1;
                        queue.push((usize::MAX - (distance + 1), next));
                    }
                });
        }

        unreachable!()
    }
}
fn main() {
    assert_eq!(
        Solution::min_jumps(vec![100, -23, -23, 404, 100, 23, 23, 23, 3, 404]),
        3
    );
    assert_eq!(Solution::min_jumps(vec![7]), 0);
    assert_eq!(Solution::min_jumps(vec![7, 6, 9, 6, 9, 6, 9, 7]), 1);
    assert_eq!(Solution::min_jumps(vec![6, 1, 9]), 2);
    assert_eq!(
        Solution::min_jumps(vec![11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]),
        3
    );
}
