struct Solution;
impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        let n = coins.len();
        let m = coins[0].len();

        let mut dp = vec![vec![[None, None, None]; m]; n];

        let mut queue = std::collections::VecDeque::new();
        dp[0][0][0] = Some(coins[0][0]);
        dp[0][0][1] = Some(coins[0][0].max(0));
        queue.push_back((0, 0, 0));
        queue.push_back((0, 0, 1));

        let vec = [(0, 1), (1, 0)];

        while let Some((x, y, used)) = queue.pop_front() {
            vec.iter().for_each(|&(dx, dy)| {
                let nx = x + dx;
                let ny = y + dy;
                if nx < n && ny < m {
                    if dp[nx][ny][used].is_none()
                        || dp[nx][ny][used].unwrap() < dp[x][y][used].unwrap() + coins[nx][ny]
                    {
                        dp[nx][ny][used] = Some(dp[x][y][used].unwrap() + coins[nx][ny]);
                        queue.push_back((nx, ny, used));
                    }
                    if coins[nx][ny] < 0
                        && used < 2
                        && (dp[nx][ny][used + 1].is_none()
                            || dp[nx][ny][used + 1].unwrap() < dp[x][y][used].unwrap())
                    {
                        dp[nx][ny][used + 1] = dp[x][y][used];
                        queue.push_back((nx, ny, used + 1));
                    }
                }
            });
        }

        dp[n - 1][m - 1]
            .iter()
            .filter(|one| one.is_some())
            .map(|one| one.unwrap())
            .max()
            .unwrap()
            .to_owned()
    }
}
fn main() {
    assert_eq!(
        Solution::maximum_amount(vec![vec![0, 1, -1], vec![1, -2, 3], vec![2, -3, 4]]),
        8
    );

    assert_eq!(
        Solution::maximum_amount(vec![
            vec![-6, -15, -16, -8],
            vec![-10, 11, 6, 16],
            vec![1, 2, 18, 12],
            vec![15, 19, 4, 17]
        ]),
        64
    )
}
