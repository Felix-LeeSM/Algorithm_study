use std::collections::VecDeque;

impl Solution {
    pub fn min_flips(mat: Vec<Vec<i32>>) -> i32 {
        let mat = mat
            .into_iter()
            .map(|line| {
                line.into_iter()
                    .map(|cell| match cell {
                        0 => false,
                        1 => true,
                        _ => panic!("improper cell"),
                    })
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();

        let n = mat.len();
        let m = mat[0].len();
        let bit = Solution::mat_to_bit(&mat, n, m);

        let mut dp = [usize::MAX; 1 << 10];
        dp[0] = 0;

        let mut queue = VecDeque::new();
        queue.push_back([0, 0]);

        while let Some([curr_bit, time]) = queue.pop_front() {
            for x in 0..n {
                for y in 0..m {
                    let flipped = Solution::flip(curr_bit, n, m, x, y);

                    if dp[flipped] > time + 1 {
                        dp[flipped] = time + 1;
                        queue.push_back([flipped, time + 1]);
                    }
                }
            }
        }

        if dp[bit] != usize::MAX {
            dp[bit] as i32
        } else {
            -1
        }
    }

    pub fn pos_to_bit(x: usize, y: usize) -> usize {
        1 << (8 - 3 * x - y)
    }

    pub fn mat_to_bit(mat: &Vec<Vec<bool>>, n: usize, m: usize) -> usize {
        let mut bit = 0;
        for x in 0..n {
            for y in 0..m {
                if mat[x][y] {
                    bit |= Solution::pos_to_bit(x, y);
                }
            }
        }
        bit
    }

    pub fn bit_to_mat(bit: usize, n: usize, m: usize) -> Vec<Vec<bool>> {
        let mut mat = vec![vec![false; m]; n];

        for x in 0..n {
            for y in 0..m {
                mat[x][y] = Solution::pos_to_bit(x, y) & bit != 0;
            }
        }

        mat
    }

    pub fn flip(bit: usize, n: usize, m: usize, x: usize, y: usize) -> usize {
        let mut mat = Solution::bit_to_mat(bit, n, m);
        for [i, j] in Solution::to_flip(n, m, x, y).into_iter() {
            mat[i][j] = !mat[i][j]
        }

        Solution::mat_to_bit(&mat, n, m)
    }

    fn to_flip(n: usize, m: usize, x: usize, y: usize) -> Vec<[usize; 2]> {
        let mut ret = vec![];
        for [i, j] in [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1]].into_iter() {
            let (nx, ny) = (x as isize + i, y as isize + j);
            if 0 <= nx && nx < n as isize && 0 <= ny && ny < m as isize {
                ret.push([nx as usize, ny as usize])
            }
        }

        ret
    }
}
