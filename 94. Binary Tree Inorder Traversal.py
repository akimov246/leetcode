from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        if node:
            self.inorderTraversal(node.left)
            self.ans.append(node.val)
            self.inorderTraversal(node.right)
        return self.ans





tree = TreeNode(1)
# tree.right = TreeNode(2)
# tree.right.left = TreeNode(3)
# tree = None
print(Solution().inorderTraversal(tree))