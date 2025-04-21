// https://www.acmicpc.net/problem/12015

fn parse<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>>(line: &str) -> T2
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    line.trim()
        .split_ascii_whitespace()
        .map(|word| T1::from_str(word).unwrap())
        .collect()
}

fn input<T1: std::str::FromStr, T2: std::iter::FromIterator<T1>, T3: std::iter::FromIterator<T2>>(
) -> T3
where
    <T1 as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(parse::<T1, T2>)
        .collect::<T3>()
}

fn solve(nums: Vec<usize>) -> usize {
    fn bisect_right(nums: &Vec<usize>, num: usize) -> usize {
        let mut left = 0;
        let mut right = nums.len();

        while left < right {
            let mid = (left + right) / 2;

            if num <= nums[mid] {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left
    }

    let mut longest_increasing_subsequence = vec![];

    for &num in &nums {
        let idx = bisect_right(&longest_increasing_subsequence, num);
        if idx == longest_increasing_subsequence.len() {
            longest_increasing_subsequence.push(num);
        } else {
            longest_increasing_subsequence[idx] = num;
        }
    }

    longest_increasing_subsequence.len()
}

fn main() {
    let mut input = input::<usize, Vec<_>, std::collections::VecDeque<_>>();
    input.pop_front();

    let nums = input.pop_front().unwrap();

    let answer = solve(nums);

    println!("{}", answer);
}
