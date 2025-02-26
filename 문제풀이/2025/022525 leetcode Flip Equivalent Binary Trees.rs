#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
    pub right: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution;
impl Solution {
    pub fn flip_equiv(
        root1: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
        root2: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
    ) -> bool {
        Solution::_flip_equiv(&root1, &root2)
    }

    pub fn _flip_equiv(
        node1: &Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
        node2: &Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
    ) -> bool {
        match (node1, node2) {
            (Some(_), None) => false,
            (None, Some(_)) => false,
            (None, None) => true,
            (Some(node1), Some(node2)) => {
                let node1 = node1.borrow();
                let node2 = node2.borrow();

                node1.val == node2.val
                    && ((Solution::_flip_equiv(&node1.left, &node2.left)
                        && Solution::_flip_equiv(&node1.right, &node2.right))
                        || (Solution::_flip_equiv(&node1.left, &node2.right)
                            && Solution::_flip_equiv(&node1.right, &node2.left)))
            }
        }
    }
}
