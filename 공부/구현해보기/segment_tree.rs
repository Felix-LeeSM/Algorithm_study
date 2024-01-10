const DEFAULT: isize = isize::MIN;

fn merge(left: isize, right: isize) -> isize {
    left.max(right)
}

fn init(nums: Vec<isize>) -> Vec<isize> {
    let n = nums.len();
    let mut points_segment = vec![0; 2 * n];

    for idx in 0..n {
        points_segment[idx + n] = nums[idx];
    }
    points_segment.push(DEFAULT);

    for idx in (0..n).rev() {
        points_segment[idx] = merge(points_segment[2 * idx + 1], points_segment[2 * idx + 2])
    }

    points_segment
}

fn query(tree: &Vec<isize>, left: usize, right: usize) -> isize {
    let data_length = tree.len() / 2;
    _query(tree, left + data_length, right + data_length, DEFAULT)
}
fn _query(tree: &Vec<isize>, mut left: usize, mut right: usize, mut val: isize) -> isize {
    if right % 2 == 1 {
        val = merge(val, tree[right]);
        right -= 1;
    }
    right = right / 2 - 1;

    if left % 2 == 0 {
        val = merge(val, tree[left]);
        left += 1;
    }
    left /= 2;

    if left <= right {
        _query(tree, left, right, val)
    } else {
        val
    }
}

fn update(tree: &mut Vec<isize>, idx: usize, val: isize) {
    let data_length = tree.len() / 2;
    let mut idx = idx + data_length;

    tree[idx] = val;
    idx = (idx - 1) / 2;

    while idx > 0 {
        tree[idx] = merge(tree[2 * idx + 1], tree[2 * idx + 2]);
        idx = (idx - 1) / 2;
    }

    tree[0] = merge(tree[1], tree[2])
}
