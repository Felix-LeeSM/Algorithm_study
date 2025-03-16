struct SORTracker {
    prev: std::collections::BinaryHeap<(std::cmp::Reverse<i32>, String)>,
    next: std::collections::BinaryHeap<(i32, std::cmp::Reverse<String>)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SORTracker {
    fn new() -> Self {
        SORTracker {
            prev: std::collections::BinaryHeap::new(),
            next: std::collections::BinaryHeap::new(),
        }
    }

    fn add(&mut self, name: String, score: i32) {
        if let Some((std::cmp::Reverse(prev_score), prev_name)) = self.prev.peek() {
            if score > *prev_score || score == *prev_score && name < *prev_name {
                let (std::cmp::Reverse(prev_score), prev_name) = self.prev.pop().unwrap();
                self.next.push((prev_score, std::cmp::Reverse(prev_name)));
                self.prev.push((std::cmp::Reverse(score), name));
            } else {
                self.next.push((score, std::cmp::Reverse(name)))
            }
        } else {
            self.next.push((score, std::cmp::Reverse(name)))
        }
    }

    fn get(&mut self) -> String {
        let (score, string) = self.next.pop().unwrap();

        let ret = string.0.clone();

        self.prev.push((std::cmp::Reverse(score), string.0));

        ret
    }
}
fn main() {
    let mut sortracker = SORTracker::new();

    sortracker.add(String::from("bradford"), 2);
    sortracker.add(String::from("branford"), 3);
    assert_eq!(String::from("branford"), sortracker.get());
    sortracker.add(String::from("alps"), 2);
    assert_eq!(String::from("alps"), sortracker.get());
    sortracker.add(String::from("orland"), 2);
    assert_eq!(String::from("bradford"), sortracker.get());
    sortracker.add(String::from("orland"), 3);
    assert_eq!(String::from("bradford"), sortracker.get());
    sortracker.add(String::from("alpine"), 2);
    assert_eq!(String::from("bradford"), sortracker.get());
    assert_eq!(String::from("orland"), sortracker.get());
}
