# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):

        __slots__ = ('val', 'left', 'right')

        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helper(node: TreeNode):
            if node:
                if node.val == target.val:
                    return node
                return helper(node.left) or helper(node.right)

        return helper(cloned)

cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)

print(Solution().getTargetCopy(cloned, cloned, cloned.right))