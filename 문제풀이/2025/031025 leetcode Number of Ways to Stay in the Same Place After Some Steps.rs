const MODULO: usize = 1_000_000_007;

struct Solution;
impl Solution {
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        let steps = steps as usize;
        let arr_len = (arr_len as usize).min(steps);

        let mut curr = vec![0; arr_len];
        let mut next = vec![0; arr_len];
        curr[0] = 1;

        let vector: [isize; 3] = [0, 1, -1];

        for _step in 0..steps {
            for position in 0..arr_len {
                vector
                    .iter()
                    .map(|&v| v + position as isize)
                    .filter(|&position| 0 <= position && position < arr_len as isize)
                    .map(|position| position as usize)
                    .for_each(|nxt_position| {
                        next[nxt_position] = (next[nxt_position] + curr[position]) % MODULO
                    });
            }

            std::mem::swap(&mut curr, &mut next);
            next.fill(0);
        }

        curr[0] as i32
    }
}
fn main() {
    assert_eq!(4, Solution::num_ways(3, 2));
    assert_eq!(2, Solution::num_ways(2, 4));
    assert_eq!(8, Solution::num_ways(4, 2));
    assert_eq!(374847123, Solution::num_ways(500, 969997));
}
