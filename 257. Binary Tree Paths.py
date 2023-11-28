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
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pass





tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.left.left = TreeNode(6)
tree.left.left.right = TreeNode(7)

print(Solution().binaryTreePaths(tree))
print(Solution().paths)
