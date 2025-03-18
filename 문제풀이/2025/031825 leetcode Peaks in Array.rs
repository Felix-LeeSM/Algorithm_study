struct Solution;

enum Query {
    Update(usize, i32),
    Determine(usize, usize),
}

impl Solution {
    pub fn count_of_peaks(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut tree = vec![0; nums.len() * 2];

        for idx in 1..(nums.len() - 1) {
            if nums[idx - 1] < nums[idx] && nums[idx + 1] < nums[idx] {
                tree[idx + nums.len()] = 1;
            }
        }

        for parent in (1..nums.len()).rev() {
            let (left, right) = (parent * 2, parent * 2 + 1);
            tree[parent] = tree[left] + tree[right];
        }

        let mut answers = vec![];

        queries
            .into_iter()
            .map(|query| {
                if query[0] == 1 {
                    Query::Determine(query[1] as usize, query[2] as usize)
                } else {
                    Query::Update(query[1] as usize, query[2])
                }
            })
            .for_each(|query| match query {
                Query::Determine(from, to) => {
                    let (mut left, mut right) = (from + 1 + nums.len(), to - 1 + nums.len());
                    let mut answer = 0;

                    while left <= right {
                        if left % 2 == 1 {
                            answer += tree[left];
                            left += 1;
                        }

                        if right % 2 == 0 {
                            answer += tree[right];
                            right -= 1;
                        }

                        left /= 2;
                        right /= 2;
                    }

                    answers.push(answer);
                }
                Query::Update(idx, number) => {
                    nums[idx] = number;
                    let affected_idx = (((idx.max(1) - 1).max(1))
                        ..=((idx + 1).min(nums.len() - 2)))
                        .collect::<Vec<_>>();

                    for &idx in &affected_idx {
                        tree[idx + nums.len()] =
                            if nums[idx - 1] < nums[idx] && nums[idx + 1] < nums[idx] {
                                1
                            } else {
                                0
                            };

                        let mut parent = (idx + nums.len()) / 2;
                        while parent >= 1 {
                            let (left, right) = (parent * 2, parent * 2 + 1);
                            tree[parent] = tree[left] + tree[right];

                            parent /= 2;
                        }
                    }
                }
            });

        answers
    }
}

fn main() {
    assert_eq!(
        vec![1, 0],
        Solution::count_of_peaks(
            vec![9, 7, 5, 8, 9],
            vec![vec![2, 0, 2], vec![1, 0, 3], vec![1, 3, 3], vec![2, 3, 5]]
        )
    );
    assert_eq!(
        vec![0],
        Solution::count_of_peaks(vec![3, 1, 4, 2, 5], vec![vec![2, 3, 4], vec![1, 0, 4]])
    );
    assert_eq!(
        vec![0, 1],
        Solution::count_of_peaks(
            vec![4, 1, 4, 2, 1, 5],
            vec![vec![2, 2, 4], vec![1, 0, 2], vec![1, 0, 4]]
        )
    );
}
