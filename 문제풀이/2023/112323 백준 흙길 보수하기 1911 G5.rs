use std::collections::VecDeque;

fn input<T: std::str::FromStr>() -> VecDeque<Vec<T>>
where
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    std::io::read_to_string(std::io::stdin())
        .expect("PARSE_ERROR")
        .trim()
        .split('\n')
        .map(|line| {
            line.trim()
                .split_ascii_whitespace()
                .map(|x| x.parse::<T>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<VecDeque<_>>()
}

fn main() {
    let mut input = input::<usize>();

    let line = input.pop_front().unwrap();
    let (n, l) = (line[0] as usize, line[1] as usize);

    let mut ponds = input
        .into_iter()
        .map(|line| (line[0], line[1]))
        .collect::<Vec<_>>();

    ponds.sort_by_cached_key(|pond| pond.0);

    let mut needed = 0;

    // last_end는 판자가 없음.
    let mut last_end = 0_usize;

    for (start, end) in ponds {
        if last_end >= end {
            continue;
        }

        let start = if last_end > start { last_end } else { start };

        let wood_needed = (end - start) / l + if (end - start) % l == 0 { 0 } else { 1 };

        needed += wood_needed;
        last_end = start + wood_needed * l;
    }

    println!("{}", needed);
}
