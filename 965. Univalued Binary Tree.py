from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        self.nodes = set()

        def helper(root: Optional[TreeNode]):
            if root:
                self.nodes.add(root.val)
                if len(self.nodes) <= 1:
                    helper(root.left)
                    helper(root.right)

        helper(root)

        return True if len(self.nodes) == 1 else False



