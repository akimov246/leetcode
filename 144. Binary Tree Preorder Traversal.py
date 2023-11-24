from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.result


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
print(Solution().preorderTraversal(tree))