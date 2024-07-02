// implementation of segment_tree for max.
// index of nodes with four numbers.
// kept 0 empty to calculate child and parent indexes easily
//     1
//   2   3
//  4 5 6 7

const DEFAULT: isize = isize::MIN;

fn merge(left: isize, right: isize) -> isize {
    left.max(right)
}

fn init(nums: Vec<isize>) -> Vec<isize> {
    let n = nums.len();
    let mut points_segment = vec![0; n];

    points_segment.extend(nums);

    (1..n).for_each(|idx| {
        points_segment[idx] = merge(points_segment[2 * idx], points_segment[2 * idx + 1])
    });

    points_segment
}

// contains both end.
fn query(tree: &Vec<isize>, left: usize, right: usize) -> isize {
    let (mut left, mut right) = (tree.len() / 2 + left, tree.len() / 2 + right);
    let mut val = DEFAULT;
    while left <= right {
        if right % 2 == 0 {
            val = merge(val, tree[right]);
            right -= 1;
        }
        right /= 2;

        if left % 2 == 1 {
            val = merge(val, tree[left]);
            left += 1;
        }
        left /= 2;
    }
    val
}

fn update(tree: &mut Vec<isize>, idx: usize, val: isize) {
    let mut idx = idx + tree.len() / 2;

    tree[idx] = val;
    idx = (idx - 1) / 2;

    while idx > 0 {
        tree[idx] = merge(tree[2 * idx + 1], tree[2 * idx + 2]);
        idx = (idx - 1) / 2;
    }

    tree[0] = merge(tree[1], tree[2])
}

fn main() {
    let nums = vec![1, 3, 5, 2, 6];
    let mut tree = init(nums);

    assert_eq!(1, query(&tree, 0, 0));
    assert_eq!(5, query(&tree, 1, 2));
    assert_eq!(3, query(&tree, 1, 1));
    assert_eq!(6, query(&tree, 2, 4));

    update(&mut tree, 0, 100);
    assert_eq!(100, query(&tree, 0, 0));
    assert_eq!(5, query(&tree, 1, 2));
    assert_eq!(3, query(&tree, 1, 1));
    assert_eq!(100, query(&tree, 0, 4));
}
