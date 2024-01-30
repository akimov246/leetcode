from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

# Моё решение. Урод, ублюдок на костылях, настоящая мразь, но работает.
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1, root2)

    def merge(self, node1: Optional[TreeNode], node2: Optional[TreeNode]):
        if node1 and node2:
            mergeRoot = TreeNode(node1.val + node2.val)
            if node1.left and node2.left:
                mergeRoot.left = self.merge(node1.left, node2.left)
            elif node1.left:
                mergeRoot.left = self.merge(node1.left, None)
            elif node2.left:
                mergeRoot.left = self.merge(None, node2.left)

            if node1.right and node2.right:
                mergeRoot.right = self.merge(node1.right, node2.right)
            elif node1.right:
                mergeRoot.right = self.merge(node1.right, None)
            elif node2.right:
                mergeRoot.right = self.merge(None, node2.right)
        elif node1:
            mergeRoot = TreeNode(node1.val)
            if node1.left:
                mergeRoot.left = self.merge(node1.left, None)
            if node1.right:
                mergeRoot.right = self.merge(node1.right, None)
        elif node2:
            mergeRoot = TreeNode(node2.val)
            if node2.left:
                mergeRoot.left = self.merge(None, node2.left)
            if node2.right:
                mergeRoot.right = self.merge(None, node2.right)

        return mergeRoot

# Решение с leetcode
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res

# root1 = TreeNode(1)
# root1.left = TreeNode(3)
# root1.right = TreeNode(2)
# root1.left.left = TreeNode(5)
#
# root2 = TreeNode(2)
# root2.left = TreeNode(1)
# root2.left.right = TreeNode(4)
# root2.right = TreeNode(3)
# root2.right.right = TreeNode(7)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(3)

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

Solution().mergeTrees(root1, root2)