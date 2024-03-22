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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = []

        def helper(root: Optional[TreeNode], v: str = ''):
            if root:
                if root.left is None and root.right is None:
                    self.total.append(int(v + str(root.val), 2))

                helper(root.left, v + str(root.val))
                helper(root.right, v + str(root.val))

        helper(root)
        return sum(self.total)

tree = TreeNode(1)
tree.left = TreeNode(0)
tree.right = TreeNode(1)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(1)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(1)

print(Solution().sumRootToLeaf(tree))

