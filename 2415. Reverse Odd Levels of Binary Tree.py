from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(list)

        def get_levels(node=root, level=0):
            if node:
                if level % 2:
                    levels[level].append(node.val)
                get_levels(node.left, level + 1)
                get_levels(node.right, level + 1)

        def reverse_levels(node=root, level=0):
            if node:
                if level % 2:
                    node.val = levels[level].pop()
                reverse_levels(node.left, level + 1)
                reverse_levels(node.right, level + 1)

        get_levels()
        print(levels)
        reverse_levels()

        return root


root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right = TreeNode(5)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

Solution().reverseOddLevels(root)
