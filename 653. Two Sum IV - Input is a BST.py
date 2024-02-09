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

    def __init__(self):
        self.nodes = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def helper(root: Optional[TreeNode]):
            if root:
                self.nodes.add(root.val)
                helper(root.left)
                helper(root.right)

        helper(root)
        if len(self.nodes) < 2:
            return False
        for val in self.nodes:
            if k - val in self.nodes - set((val, )):
                return True
        return False

# Решение с leetcode
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodes = set()

        def helper(root: TreeNode):
            if not root:
                return False

            if root.val in nodes:
                return True

            nodes.add(k - root.val)

            return helper(root.left) or helper(root.right)

        return helper(root)


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right = TreeNode(6)
tree.right.right = TreeNode(7)

print(Solution().findTarget(tree, k = 1))