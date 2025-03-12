# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cnt = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root:
            self.dfs(root)

        return self.cnt

    def dfs(self, node: TreeNode, digits: List[int] = []):
        digits.append(node.val)

        if node.left:
            self.dfs(node.left, digits)
        if node.right:
            self.dfs(node.right, digits)

        if not node.left and not node.right:
            for expo, digit in enumerate(reversed(digits)):
                self.cnt += digit * (10 ** expo)

        digits.pop()
