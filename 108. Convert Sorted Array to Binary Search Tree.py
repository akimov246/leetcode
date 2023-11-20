from typing import Optional, List
from itertools import zip_longest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: TreeNode|None = None):
        self.root = root

    def add(self, value: int):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.__add_helper(self.root, value)

    def __add_helper(self, node: TreeNode, value: int):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.__add_helper(node.left, value)
        elif value > node.val:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.__add_helper(node.right, value)

class Solution:

    def __init__(self):
        self.tree = Tree()

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            middle = len(nums) // 2
            self.tree.add(nums[middle])

            left = nums[:middle]
            right = nums[middle + 1:]
            self.sortedArrayToBST(left)
            self.sortedArrayToBST(right)

        return self.tree.root


nums = [0, 1, 2, 3, 4, 5]
nums = [-1, 0, 1, 2]
print(Solution().sortedArrayToBST(nums))

# Решение с Leetcode
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        if not n:
            return None

        mid = (n - 1) // 2
        root = TreeNode(nums[mid])

        root.left = (self.sortedArrayToBST(nums[:mid]))
        root.right = (self.sortedArrayToBST(nums[mid + 1:]))

        return root