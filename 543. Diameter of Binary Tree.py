from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.getDeep(root)
        return self.d

    def getDeep(self, root: TreeNode):
        if root is None:
            return 0
        left = self.getDeep(root.left)
        right = self.getDeep(root.right)

        self.d = max(right + left, self.d)

        return max(left, right) + 1


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(14)

print(Solution().diameterOfBinaryTree(root))