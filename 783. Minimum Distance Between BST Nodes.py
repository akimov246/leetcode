from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = set()

        def helper(root: Optional[TreeNode]):
            if root:
                nodes.add(root.val)
                helper(root.left)
                helper(root.right)

        helper(root)

        nodes = sorted(nodes)
        min_diff = nodes[-1]
        for i in range(len(nodes) - 1):
            min_diff = min(min_diff, abs(nodes[i] - nodes[i + 1]))
        return min_diff




tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(6)

print(Solution().minDiffInBST(tree))