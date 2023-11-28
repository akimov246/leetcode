from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def printTree(self, root: TreeNode):
        if root:
            print(root.val, end=" ")
            self.printTree(root.left)
            self.printTree(root.right)

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

Solution().printTree(tree)
print()
Solution().printTree(Solution().invertTree(tree))