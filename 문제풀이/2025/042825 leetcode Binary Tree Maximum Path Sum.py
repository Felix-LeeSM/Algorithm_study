from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = -1001

        def solve(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            # 날 포함해 양쪽을 연결한 최대값, 날 포함해 한 쪽만 연결한 최대값, 날 포함하지 않을 때의 최대값
            if node is None:
                return (0, 0, 0)

            nonlocal max_val
            max_val = max(max_val, node.val)

            left = solve(node.left)
            right = solve(node.right)

            return (
                node.val + max(left[1], 0) + max(right[1], 0),
                node.val + max(left[1], right[1], 0),
                max(*left, *right)
            )

        ret = max(solve(root))
        return ret if max_val >= 0 else max_val


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    assert 6 == Solution().maxPathSum(root)

    root = TreeNode(
        -10,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )

    assert 42 == Solution().maxPathSum(root)

    root = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                None,
                TreeNode(1)
            )
        )
    )

    assert 48 == Solution().maxPathSum(root)
