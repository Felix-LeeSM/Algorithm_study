const INF: usize = 100_000_001;

impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let (n, k) = (n as usize, k as usize - 1);

        let mut map = vec![vec![INF; n]; n];

        times
            .into_iter()
            .map(|vec| (vec[0], vec[1], vec[2]))
            .map(|(u, v, w)| ((u - 1) as usize, (v - 1) as usize, w as usize))
            .for_each(|(u, v, w)| map[u][v] = w);

        for k in 0..n {
            for i in 0..n {
                for j in 0..n {
                    map[i][j] = map[i][j].min(map[i][k] + map[k][j]);
                }
            }
        }

        (0..n).for_each(|i| map[i][i] = 0);

        let answer = map[k].clone().into_iter().fold(0, |a, b| a.max(b));

        if answer == INF {
            -1
        } else {
            answer as i32
        }
    }
}
