from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    __slots__ = ('val', 'left', 'right')

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.range = range(low, high + 1)
        self.sum = 0
        self.helper(root)
        return self.sum

    def helper(self, root):
        if root:
            if root.val in self.range:
                self.sum += root.val
                self.helper(root.left)
                self.helper(root.right)
            elif root.val < self.low:
                self.helper(root.right)
            else:
                self.helper(root.left)