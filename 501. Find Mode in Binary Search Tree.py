from typing import  Optional, List
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.traversal(root)
        c = Counter(self.values)
        number = tuple(c.values()).count(max(c.values()))
        ans = c.most_common(number)
        return [n for n, _ in ans]

    def traversal(self, root):
        if root:
            self.values.append(root.val)
            self.traversal(root.left)
            self.traversal(root.right)

root = TreeNode(1)
root.right = TreeNode(2)
#root.right.left = TreeNode(2)
#root.left = TreeNode(1)
#root = TreeNode(0)
print(Solution().findMode(root))