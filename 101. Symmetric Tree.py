from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        try:
            if root.left == root.right == None:
                return True
            if root.left.val != root.right.val:
                return False
        except:
            return False

        left_halt = Traversal()
        left_halt.travel_left(root.left)
        right_half = Traversal()
        right_half.travel_right(root.right)

        return left_halt.ans == right_half.ans

class Traversal:

    def __init__(self):
        self.ans = []

    def travel_left(self, tree: TreeNode):
        node = tree
        if node:
            self.ans.append(node.val)
            self.travel_left(node.left)
            self.travel_left(node.right)
        else:
            self.ans.append(None)

    def travel_right(self, tree: TreeNode):
        node = tree
        if node:
            self.ans.append(node.val)
            self.travel_right(node.right)
            self.travel_right(node.left)
        else:
            self.ans.append(None)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

# l = Traversal()
# l.travel_left(tree.left)
# print(l.ans)
# r = Traversal()
# r.travel_right(tree.right)
# print(r.ans)

print(Solution().isSymmetric(tree))

# Решение с Leetcode
class Solution(object):
    def isSymmetric(self, root):
        # Special case...
        if not root:
            return True
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)