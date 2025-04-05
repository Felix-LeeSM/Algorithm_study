struct Solution;

const NO_CLUE: usize = 10_000_007;

impl Solution {
    pub fn loud_and_rich(richer: Vec<Vec<i32>>, quiet: Vec<i32>) -> Vec<i32> {
        let n = quiet.len();
        let mut distances = vec![vec![NO_CLUE; n]; n];

        richer
            .iter()
            .map(|line| (line[0] as usize, line[1] as usize))
            .for_each(|(rich, poor)| distances[poor][rich] = 1);

        for i in 0..n {
            distances[i][i] = 0;
        }

        for k in 0..n {
            for i in 0..n {
                for j in 0..n {
                    distances[i][j] = distances[i][j].min(distances[i][k] + distances[k][j]);
                }
            }
        }

        let mut ret = vec![];

        for node in 0..n {
            let ans = (0..n)
                .filter(|&another| distances[node][another] != NO_CLUE)
                .map(|node| (node, quiet[node]))
                .min_by_key(|&(_node, quiet)| quiet)
                .map(|(node, _quiet)| node)
                .unwrap();

            ret.push(ans as i32)
        }

        ret
    }
}
fn main() {
    assert_eq!(
        vec![5, 5, 2, 5, 4, 5, 6, 7],
        Solution::loud_and_rich(
            vec![
                vec![1, 0],
                vec![2, 1],
                vec![3, 1],
                vec![3, 7],
                vec![4, 3],
                vec![5, 3],
                vec![6, 3]
            ],
            vec![3, 2, 5, 4, 6, 1, 7, 0]
        )
    );

    assert_eq!(vec![0], Solution::loud_and_rich(vec![], vec![0]));
}
