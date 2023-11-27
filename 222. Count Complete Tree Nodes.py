from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        self.helper(root)
        return self.counter

    def helper(self, root):
        if root:
            self.counter += 1
            self.helper(root.left)
            self.helper(root.right)

# Решение с Leetcode
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)

print(Solution().countNodes(tree))