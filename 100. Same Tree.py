from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        travel_p = Traversal()
        travel_p.inorder(p)

        travel_q = Traversal()
        travel_q.inorder(q)

        return travel_p.ans == travel_q.ans

class Traversal:

    def __init__(self):
        self.ans = []

    def inorder(self, tree: TreeNode):
        node = tree
        if node:
            self.ans.append(node.val)
            self.inorder(node.left)
            self.inorder(node.right)
        else:
            self.ans.append(None)


p = TreeNode(1)
p.left = TreeNode(1)
q = TreeNode(1)
q.right = TreeNode(1)

# travel_p = Traversal()
# travel_p.inorder(p)
# print(travel_p.ans)
#
# travel_q = Traversal()
# travel_q.inorder(q)
# print(travel_q.ans)

print(Solution().isSameTree(p, q))