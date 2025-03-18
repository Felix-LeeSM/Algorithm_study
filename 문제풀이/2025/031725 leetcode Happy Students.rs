struct Solution;

impl Solution {
    pub fn count_ways(nums: Vec<i32>) -> i32 {
        let mut reqs = nums;
        reqs.sort();
        reqs.push(i32::MAX);

        let (mut criteria, mut selected, mut answer) = (-1, 0, 0);

        for req in reqs {
            if criteria < req {
                if criteria < selected && selected < req {
                    answer += 1;
                }

                criteria = req;
            }

            selected += 1;
        }

        answer
    }
}

fn main() {
    assert_eq!(3, Solution::count_ways(vec![6, 0, 3, 3, 6, 7, 2, 7]));
    assert_eq!(2, Solution::count_ways(vec![1, 1]));
}
