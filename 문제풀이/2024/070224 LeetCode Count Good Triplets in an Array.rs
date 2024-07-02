struct Solution;

impl Solution {
    pub fn good_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();

        let mut nums1 = nums1
            .into_iter()
            .map(|num| num as usize)
            .collect::<Vec<_>>();
        let nums2 = nums2
            .into_iter()
            .map(|num| num as usize)
            .collect::<Vec<_>>();

        let mut indexes = vec![0; n];

        nums2
            .into_iter()
            .enumerate()
            .for_each(|(idx, num)| indexes[num] = idx);

        nums1
            .clone()
            .into_iter()
            .enumerate()
            .for_each(|(idx, num)| nums1[idx] = indexes[num]);

        let mut answer = 0;
        let mut segment_tree = vec![0; 2 * n];
        let mut couplets = vec![0; n];

        for idx in (0..n).rev() {
            let num = nums1[idx];
            couplets[num] = Solution::seg_get(&mut segment_tree, num, n - 1, n);
            Solution::seg_set(&mut segment_tree, num, 1, n);
        }

        segment_tree.fill(0);

        for idx in (0..n).rev() {
            let num = nums1[idx];
            let couples = couplets[num];
            answer += Solution::seg_get(&mut segment_tree, num, n - 1, n);
            Solution::seg_set(&mut segment_tree, num, couples, n);
        }

        answer as i64
    }

    fn seg_idx(n: usize, index: usize) -> usize {
        n + index
    }

    fn seg_merge(val1: usize, val2: usize) -> usize {
        val1 + val2
    }

    fn seg_set(segment_tree: &mut Vec<usize>, index: usize, value: usize, n: usize) {
        let mut index = Solution::seg_idx(n, index);
        segment_tree[index] = value;
        index /= 2;

        while index > 0 {
            let (left, right) = (index * 2, index * 2 + 1);

            match (segment_tree.get(left), segment_tree.get(right)) {
                (Some(&val1), Some(&val2)) => segment_tree[index] = Solution::seg_merge(val1, val2),
                (Some(&val), None) => segment_tree[index] = val,
                _ => panic!("invalid child!"),
            };

            index /= 2;
        }
    }

    fn seg_get(segment_tree: &mut Vec<usize>, start: usize, end: usize, n: usize) -> usize {
        let mut val = 0;
        let (mut left, mut right) = (start + n, end + n);

        while left <= right {
            if right % 2 == 0 {
                val = Solution::seg_merge(val, segment_tree[right]);
                right -= 1;
            }

            if left % 2 == 1 {
                val = Solution::seg_merge(val, segment_tree[left]);
                left += 1;
            }

            left /= 2;
            right /= 2;
        }

        val
    }
}

fn main() {
    assert_eq!(
        Solution::good_triplets(vec![2, 0, 1, 3], vec![0, 1, 2, 3]),
        1,
    );
    assert_eq!(
        Solution::good_triplets(vec![4, 0, 1, 3, 2], vec![4, 1, 0, 2, 3]),
        4,
    );
}
