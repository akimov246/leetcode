from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        self.helper(root)
        self.nodes.sort()
        left = 0
        right = 1
        minimum = max(self.nodes)
        while right != len(self.nodes) and left != len(self.nodes):
            minimum = min(self.nodes[right] - self.nodes[left], minimum)
            right += 1
            if right == len(self.nodes):
                left += 1
                right = left + 1
        return minimum

    def helper(self, root):
        if root:
            self.nodes.append(root.val)
            self.helper(root.left)
            self.helper(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)

print(Solution().getMinimumDifference(root))