from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        mins = [float('inf')] * 3001
        maxs = [-float('inf')] * 3001

        def dfs(node: TreeNode, depth, position) -> None:
            mins[depth] = min(mins[depth], position)
            maxs[depth] = max(maxs[depth], position)

            if node.left:
                dfs(node.left, depth+1, position*2)
            if node.right:
                dfs(node.right, depth+1, position*2 + 1)

        dfs(root, 0, 0)

        answer = 0
        for min_pos, max_pos in zip(mins, maxs):
            if min_pos != float('inf'):
                answer = max(max_pos - min_pos, answer)

        return answer
