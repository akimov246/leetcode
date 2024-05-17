from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.root = root
        self.target = target

        def helper(node: Optional[TreeNode] = self.root, parent: Optional[TreeNode] = None):
            if node == self.root and node.left is None and node.right is None and node.val == target:
                self.root = None
            elif node.left is None and node.right is None and node.val == self.target:
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None
                helper()
            if node:
                if node.left:
                    helper(node.left, node)
                if node.right:
                    helper(node.right, node)

        helper()
        return self.root



root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

print(Solution().removeLeafNodes(root, 1))