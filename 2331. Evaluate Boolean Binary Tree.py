from typing import Optional
import operator

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        d = {0: False,
             1: True,
             2: operator.or_,
             3: operator.and_}

        def helper(node: Optional[TreeNode]):
            if node:
                if node.left is None and node.right is None:
                    return d[node.val]
                else:
                    left = helper(node.left)
                    right = helper(node.right)
                    return d[node.val](left, right)

        return helper(root)

tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(1)

print(Solution().evaluateTree(tree))