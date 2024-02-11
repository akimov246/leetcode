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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minimals = set()

        def helper(root: Optional[TreeNode]):
            if root:
                minimals.add(root.val)
                helper(root.left)
                helper(root.right)

        helper(root)
        return sorted(minimals)[1] if len(minimals) > 1 else -1


tree = TreeNode(2)
tree.left = TreeNode(2)
tree.right = TreeNode(5)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)

print(Solution().findSecondMinimumValue(tree))