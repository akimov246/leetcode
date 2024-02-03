from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.levels = {}
        self.helper(root)
        return [sum(values) / len(values) for values in self.levels.values()]

    def helper(self, root: TreeNode, level: int = 0):
        if root:
            self.levels.setdefault(level, []).append(root.val)
            self.helper(root.left, level + 1)
            self.helper(root.right, level + 1)


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().averageOfLevels(tree))

