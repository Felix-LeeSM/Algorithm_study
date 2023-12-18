fn parse(line: &str) -> usize {
    let parsed = line
        .chars()
        .map(|char| char.to_string().parse::<usize>())
        .filter_map(|parsed| match parsed {
            Ok(x) => Some(x),
            Err(_) => None,
        })
        .collect::<Vec<_>>();

    if parsed.is_empty() {
        0
    } else {
        parsed.first().unwrap() * 10 + parsed.last().unwrap()
    }
}
fn main() {
    let ret = std::io::read_to_string(std::io::stdin())
        .expect("REQUIRES STDIN")
        .split('\n')
        .map(parse)
        .fold(0, |acc, x| acc + x);

    println!("{}", ret);
}
