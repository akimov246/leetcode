from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getMaxDeep(root) >= 0

    def getMaxDeep(self, node: TreeNode) -> int:
        if node is None:
            return 0
        l_deep = self.getMaxDeep(node.left)
        r_deep = self.getMaxDeep(node.right)
        if abs(l_deep - r_deep) > 1 or l_deep < 0 or r_deep < 0:
            return -1
        return max(l_deep, r_deep) + 1


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.right = TreeNode(8)

print(Solution().isBalanced(tree))
