from typing import Optional
from collections import defaultdict

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.left.val if self.left else None}← {self.val} →{self.right.val if self.right else None}'

# class Solution:
#     def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#
#         def helper(root: Optional[TreeNode], depth: int = 0, result: dict = None):
#             if result is None:
#                 result = defaultdict(dict)
#             if root:
#                 # result[depth + 1].append({root.left: (root.left.val, root)}) if root.left else ...
#                 # result[depth + 1].append({root.right: (root.right.val, root)}) if root.right else ...
#                 result[depth + 1].update({id(root.left): (root.left.val, root)}) if root.left else ...
#                 result[depth + 1].update({id(root.right): (root.right.val, root)}) if root.right else ...
#                 helper(root.left, depth + 1, result)
#                 helper(root.right, depth + 1, result)
#             return result
#
#         print(helper(root))
#         structure = helper(root)
#
#         def modify_tree(root: Optional[TreeNode], structure, depth: int = 0):
#             if root:
#                 if depth == 0:
#                     root.val = 0
#                 else:
#                     sum = 0
#                     parent = structure[depth][id(root)][1]
#                     for node in tuple(structure[depth].keys()):
#                         if structure[depth][node][1] != parent:
#                             sum += structure[depth][node][0]
#
#                     root.val = sum
#
#                 modify_tree(root.left, structure, depth + 1)
#                 modify_tree(root.right, structure, depth + 1)
#
#         modify_tree(root, structure)
#         return root

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def get_levels_sum(root: Optional[TreeNode], level: int = 0, result: dict = None):
            if result is None:
                result = {}
            if root:
                l = root.left.val if root.left else 0
                r = root.right.val if root.right else 0
                result[id(root)] = l + r
                result[level + 1] = result.get(level + 1, 0) + result[id(root)]

                get_levels_sum(root.left, level + 1, result)
                get_levels_sum(root.right, level + 1, result)

            return result

        levels = get_levels_sum(root)

        def modify_tree(root: Optional[TreeNode], level: int = 0, parent = None):
            if root:
                if level == 0:
                    root.val = 0
                else:
                    root.val = levels[level] - levels[id(parent)]
                modify_tree(root.left, level + 1, root)
                modify_tree(root.right, level + 1, root)

        modify_tree(root)
        return root


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right = TreeNode(9)
root.right.right = TreeNode(7)

Solution().replaceValueInTree(root)

