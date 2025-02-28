struct FrequencyTracker {
    num_freq: std::collections::HashMap<i32, usize>,
    freq_num: std::collections::HashMap<usize, std::collections::HashSet<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FrequencyTracker {
    fn new() -> Self {
        Self {
            num_freq: std::collections::HashMap::new(),
            freq_num: std::collections::HashMap::new(),
        }
    }

    fn add(&mut self, number: i32) {
        let freq = self.num_freq.entry(number).or_insert(0);
        self.freq_num
            .entry(*freq)
            .or_insert(std::collections::HashSet::new())
            .remove(&number);

        *freq += 1;
        self.freq_num
            .entry(*freq)
            .or_insert(std::collections::HashSet::new())
            .insert(number);
    }

    fn delete_one(&mut self, number: i32) {
        if let Some(freq) = self.num_freq.get_mut(&number) {
            self.freq_num
                .entry(*freq)
                .or_insert(std::collections::HashSet::new())
                .remove(&number);

            if *freq >= 1 {
                *freq -= 1;
                self.freq_num
                    .entry(*freq)
                    .or_insert(std::collections::HashSet::new())
                    .insert(number);
            }
        }
    }

    fn has_frequency(&self, frequency: i32) -> bool {
        self.freq_num
            .get(&(frequency as usize))
            .filter(|x| x.len() > 0)
            .is_some()
    }
}

// 배열을 사용하는 풀이
// struct FrequencyTracker {
//     num_freq: [usize; 100000],
//     freq_num: [usize; 100000],
// }

// /**
//  * `&self` means the method takes an immutable reference.
//  * If you need a mutable reference, change it to `&mut self` instead.
//  */
// impl FrequencyTracker {
//     fn new() -> Self {
//         Self {
//             num_freq: [0; 100_000],
//             freq_num: [0; 100_000],
//         }
//     }

//     fn add(&mut self, number: i32) {
//         match self.num_freq[number as usize] {
//             0 => {
//                 self.num_freq[number as usize] += 1;
//                 self.freq_num[1] += 1;
//             }
//             freq => {
//                 self.num_freq[number as usize] += 1;
//                 self.freq_num[freq + 1] += 1;
//                 self.freq_num[freq] -= 1;
//             }
//         }
//     }

//     fn delete_one(&mut self, number: i32) {
//         match self.num_freq[number as usize] {
//             0 => {}
//             freq => {
//                 self.num_freq[number as usize] -= 1;
//                 self.freq_num[freq] -= 1;
//                 self.freq_num[freq - 1] += 1;
//             }
//         }
//     }

//     fn has_frequency(&self, frequency: i32) -> bool {
//         self.freq_num[frequency as usize] > 0
//     }
// }

fn main() {
    let mut tracker = FrequencyTracker::new();

    assert_eq!((), tracker.delete_one(9));
    assert_eq!((), tracker.delete_one(8));
    assert_eq!((), tracker.delete_one(1));
    assert_eq!((), tracker.delete_one(4));
    assert_eq!(false, tracker.has_frequency(1));
    assert_eq!((), tracker.add(10));
    assert_eq!((), tracker.delete_one(5));
    assert_eq!(true, tracker.has_frequency(1));
    assert_eq!((), tracker.delete_one(10));
    assert_eq!((), tracker.delete_one(9));
    assert_eq!((), tracker.delete_one(10));
    assert_eq!(false, tracker.has_frequency(1));
    assert_eq!((), tracker.add(4));
    assert_eq!(true, tracker.has_frequency(1));
    assert_eq!((), tracker.delete_one(4));
    assert_eq!(false, tracker.has_frequency(1));
    assert_eq!(false, tracker.has_frequency(1));
    assert_eq!((), tracker.add(10));
    assert_eq!(true, tracker.has_frequency(1));
    assert_eq!((), tracker.add(2));
    assert_eq!((), tracker.delete_one(1));
    assert_eq!(false, tracker.has_frequency(2));
    assert_eq!((), tracker.add(7));
    assert_eq!(true, tracker.has_frequency(1));
    assert_eq!(true, tracker.has_frequency(1));
    assert_eq!((), tracker.add(6));
}
