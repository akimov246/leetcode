from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root: TreeNode, side: bool = False) -> None:
        if root:
            if side and root.left is None and root.right is None:
                self.ans += root.val
            self.helper(root.left, True)
            self.helper(root.right, False)


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
#tree = TreeNode(1)

print(Solution().sumOfLeftLeaves(tree))


