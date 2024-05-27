use std::collections::VecDeque;

fn input() -> VecDeque<Vec<usize>> {
    std::io::read_to_string(std::io::stdin())
        .unwrap()
        .trim()
        .split('\n')
        .map(|str| {
            str.trim()
                .split_ascii_whitespace()
                .map(|st| st.parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
        })
        .collect::<VecDeque<Vec<usize>>>()
}

fn solution(airports: usize, budget: usize, flights: Vec<Vec<usize>>) -> String {
    let mut graph = vec![vec![]; airports + 1];

    for line in flights {
        let (from, to, cost, distance) = (line[0], line[1], line[2], line[3]);
        graph[from].push((to, cost, distance));
    }

    // dp[airport][cost] = [distance]
    let mut dp = vec![vec![usize::MAX; budget + 1]; airports + 1];
    dp[1][0] = 0;

    for cost in 0..=budget {
        for airport in 1..=airports {
            if dp[airport][cost] == usize::MAX {
                continue;
            }

            for line in &graph[airport] {
                let (to, flight_cost, flight_distance) = *line;
                let next_cost = cost + flight_cost;
                if next_cost > budget {
                    continue;
                }

                dp[to][next_cost] = dp[to][next_cost].min(dp[airport][cost] + flight_distance);
            }
        }
    }

    match dp[airports]
        .iter()
        .fold(usize::MAX, |curr_min, new| curr_min.min(*new))
    {
        usize::MAX => "Poor KCM".to_string(),
        ret => ret.to_string(),
    }
}

fn main() {
    let mut input = input();

    let test_cases = input.pop_front().unwrap().pop().unwrap();

    let answer = (0..test_cases)
        .map(|_| {
            let line = input.pop_front().unwrap();
            let (airports, budget, flights) = (line[0], line[1], line[2]);

            solution(airports, budget, input.drain(..flights).collect())
        })
        .fold(String::new(), |mut acc, answer| {
            acc.push_str(&answer);
            acc.push('\n');
            acc
        });

    println!("{}", answer);
}
