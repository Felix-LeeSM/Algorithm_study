struct Solution;

// 0 ~ 100_000
static LEN: usize = 100_001;
static DEFAULT: usize = 0;

fn update(
    seg_tree: &mut Vec<usize>,
    number: usize,
    value: usize,
    merge: &dyn Fn(usize, usize) -> usize,
) {
    let mut idx = number + LEN;

    seg_tree[idx] = merge(value, seg_tree[idx]);

    while idx > 1 {
        idx /= 2;

        seg_tree[idx] = merge(seg_tree[2 * idx], seg_tree[2 * idx + 1])
    }
}

fn query(
    seg_tree: &Vec<usize>,
    start: usize,
    end: usize,
    merge: &dyn Fn(usize, usize) -> usize,
) -> usize {
    let mut val = DEFAULT;
    let (mut left, mut right) = (start + LEN, end + LEN);

    while left <= right {
        if left % 2 == 1 {
            val = merge(val, seg_tree[left]);
            left += 1;
        }
        if right % 2 == 0 {
            val = merge(val, seg_tree[right]);
            right -= 1;
        }

        left /= 2;
        right /= 2;
    }

    val
}

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>, k: i32) -> i32 {
        let nums = nums.into_iter().map(|num| num as usize).collect::<Vec<_>>();
        let k = k as usize;

        let mut seg_tree = vec![0_usize; LEN * 2];

        let max = |num1: usize, num2: usize| num1.max(num2);

        for num in nums {
            let start = if num >= k { num - k } else { 0 };
            let end = num - 1;

            let longest = query(&seg_tree, start, end, &max);
            update(&mut seg_tree, num, longest + 1, &max);
        }

        query(&seg_tree, 1, 100_000, &max) as i32
    }
}

fn main() {
    assert_eq!(
        5,
        Solution::length_of_lis(vec![4, 2, 1, 4, 3, 4, 5, 8, 15], 3)
    );

    assert_eq!(4, Solution::length_of_lis(vec![7, 4, 5, 1, 8, 12, 4, 7], 5));
    assert_eq!(1, Solution::length_of_lis(vec![1, 5], 1));
    assert_eq!(
        100_000,
        Solution::length_of_lis(Vec::from_iter(1..100_001), 100_000)
    )
}
