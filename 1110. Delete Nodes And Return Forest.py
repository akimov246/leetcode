from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        self.forest = []

        def helper(node: Optional[TreeNode]):
            if node:
                if node.val in to_delete:
                    if node.left and node.left.val not in to_delete:
                        self.forest.append(node.left)
                    if node.right and node.right.val not in to_delete:
                        self.forest.append(node.right)
                elif not self.forest:
                    self.forest.append(node)
                helper(node.left)
                helper(node.right)

        helper(root)

        def make_forest(node: Optional[TreeNode]):
            if node:
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None
                make_forest(node.left)
                make_forest(node.right)

        for root in self.forest:
            make_forest(root)

        return self.forest

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().delNodes(root, [3, 5]))