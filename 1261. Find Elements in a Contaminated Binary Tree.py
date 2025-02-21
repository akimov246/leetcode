from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.values = set()

        def get_values(node=self.root):
            if node:
                self.values.add(node.val)
                if node.left:
                    node.left.val = 2 * node.val + 1
                    get_values(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    get_values(node.right)
        get_values()

    @cache
    def find(self, target: int) -> bool:
        return target in self.values


root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.right = TreeNode(-1)
root.right.right.right = TreeNode(-1)

print(FindElements(root).find(6))