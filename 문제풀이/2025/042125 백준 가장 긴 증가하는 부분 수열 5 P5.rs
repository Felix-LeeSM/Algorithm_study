// https://www.acmicpc.net/problem/14003

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

fn solve(n: usize, nums: Vec<isize>) -> (usize, Vec<isize>) {
    fn bisect_right(nums: &Vec<isize>, num: isize) -> usize {
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
    let mut indexs = vec![];
    let mut prevs = vec![0; n];

    for (num_idx, &num) in nums.iter().enumerate() {
        let idx = bisect_right(&longest_increasing_subsequence, num);
        if idx == longest_increasing_subsequence.len() {
            longest_increasing_subsequence.push(num);
            indexs.push(num_idx);
            prevs[num_idx] = if idx == 0 { 0 } else { indexs[idx - 1] }
        } else {
            longest_increasing_subsequence[idx] = num;
            indexs[idx] = num_idx;
            prevs[num_idx] = if idx == 0 { 0 } else { indexs[idx - 1] }
        }
    }

    let mut index = *indexs.last().unwrap();
    let mut subsequence = vec![];

    for _ in 0..longest_increasing_subsequence.len() {
        subsequence.push(nums[index]);
        index = prevs[index];
    }

    (
        longest_increasing_subsequence.len(),
        subsequence.into_iter().rev().collect::<Vec<_>>(),
    )
}

fn main() {
    let mut input = input::<isize, Vec<_>, std::collections::VecDeque<_>>();
    let n = input.pop_front().unwrap().pop().unwrap() as usize;

    let nums = input.pop_front().unwrap();

    let (length, subsequence) = solve(n, nums);

    println!("{}", length);
    println!(
        "{}",
        subsequence
            .into_iter()
            .map(|num| num.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
