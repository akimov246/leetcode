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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaves1 = []
        self.leaves2 = []
        self.helper(root1, self.leaves1)
        self.helper(root2, self.leaves2)
        return self.leaves1 == self.leaves2

    def helper(self, root: Optional[TreeNode], leaves: list):
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.val)
            self.helper(root.left, leaves)
            self.helper(root.right, leaves)



tree = TreeNode(3)
tree.left = TreeNode(5)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right = TreeNode(1)
tree.right.left = TreeNode(9)
tree.right.right = TreeNode(8)

print(Solution().leafSimilar(tree, tree))