from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_deep = self.minDepth(root.left)
        r_deep = self.minDepth(root.right)
        return min(l_deep, r_deep) + 1 if min(l_deep, r_deep) != 0 else max(l_deep, r_deep) + 1

