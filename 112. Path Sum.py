from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # Является ли наша нода листом, если да, то проверяем равняется ли value остатку targetSum
        if root.left is None and root.right is None:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        # Возвращаем левую или левую ноду, так как хотя бы одна из них не словила False
        return left_sum or right_sum




tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.right = TreeNode(1)
#tree.right.left = TreeNode(5)
print(Solution().hasPathSum(tree, 5))
