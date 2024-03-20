from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #self.x = x
        #self.y = y
        self.cousins = []

        def helper(root: Optional[TreeNode], depth: int = 0, parent: Optional[TreeNode] = None):
            if root:
                #print(f'{root.val, depth}')
                if root.val == x or root.val == y:
                    self.cousins.append((depth, parent))
                helper(root.left, depth + 1, root)
                helper(root.right, depth + 1, root)

        helper(root)
        a_depth = self.cousins[0][0]
        a_parent = self.cousins[0][1]
        b_depth = self.cousins[1][0]
        b_parent = self.cousins[1][1]

        return True if a_depth == b_depth and a_parent != b_parent else False



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

print(Solution().isCousins(tree, x = 4, y = 3))