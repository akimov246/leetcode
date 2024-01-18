from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def getTilt(root: TreeNode):
            if root is None:
                return 0

            left = getTilt(root.left)
            right = getTilt(root.right)
            self.tilt += abs(left - right)

            return root.val + left + right

        getTilt(root)
        return self.tilt



root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right = TreeNode(9)
root.right.right = TreeNode(7)

print(Solution().findTilt(root))