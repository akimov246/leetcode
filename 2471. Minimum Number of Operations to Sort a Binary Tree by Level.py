from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        swaps = 0

        def helper(node=root, level=0):
            if node:
                if level:
                    levels[level].append(node.val)
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        helper()
        print(levels)

        def count_swaps(arr):
            current_swaps = 0
            sorted_arr = sorted(arr)
            for i in range(len(arr)):
                if arr[i] != sorted_arr[i]:
                    idx = arr.index(sorted_arr[i])
                    arr[i], arr[idx] = arr[idx], arr[i]
                    current_swaps += 1
            return current_swaps

        for level in levels:
            swaps += count_swaps(levels[level])

        return swaps


root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(9)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(10)


print(Solution().minimumOperations(root))