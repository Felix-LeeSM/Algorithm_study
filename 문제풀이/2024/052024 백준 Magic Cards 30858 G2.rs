use std::collections::{HashMap, VecDeque};
use std::io::{self};

fn input() -> VecDeque<Vec<String>> {
    let input = io::read_to_string(io::stdin()).unwrap();
    input
        .trim()
        .split('\n')
        .map(|str| {
            str.split_ascii_whitespace()
                .map(|st| st.to_string())
                .collect::<Vec<String>>()
        })
        .collect()
}

fn main() {
    let mut input = input();

    let line = input
        .pop_front()
        .unwrap()
        .into_iter()
        .map(|st| st.parse::<usize>().unwrap())
        .collect::<Vec<usize>>();
    let (n, k, m, f) = (line[0], line[1], line[2], line[3]);

    let mut cards_str = vec![vec!['N'; k]; n + 1];

    for (card_no, card) in input.drain(..k).enumerate() {
        for num in card {
            cards_str[num.parse::<usize>().unwrap()][card_no] = 'Y';
        }
    }

    let mut memo: HashMap<String, usize> = HashMap::new();

    for num in 1..(n + 1) {
        let s = (0..k)
            .map(|card_no| cards_str[num][card_no])
            .collect::<String>();

        if memo.contains_key(&s) {
            memo.insert(s, 0);
        } else {
            memo.insert(s, num);
        }
    }

    let ret = input
        .drain(..f)
        .map(|query| memo.get(&query.join("")).unwrap())
        .map(|&num| num.to_string())
        .collect::<Vec<String>>();

    println!("{}", ret.join("\n"));
}
