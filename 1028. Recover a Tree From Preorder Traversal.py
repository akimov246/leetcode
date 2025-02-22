from typing import Optional
import re

#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return f'TreeNode({self.val})'


class Solution:

    def __init__(self):
        self.root = None
        self.traversal = None

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root_idx = traversal.find('-') if traversal.find('-') != -1 else int(traversal)
        self.root, self.traversal = TreeNode(int(traversal[:root_idx])), traversal[root_idx + 1:]
        self.root.level = 0

        print(self.root)
        print(self.traversal)

        def parser(node=self.root, subtree=self.traversal, level=1):
            if not subtree:
                return False
            result = re.split(fr'(?<!-){"-" * level}(?!-)', subtree)
            left = result[0]
            right = None
            if len(result) > 1:
                right = result[1]
            #print(left, right)
            if left:
                left_value = int(subtree[:left.find('-')]) if left.find('-') != -1 else int(left)
                node.left = TreeNode(left_value)
                dash = False
                cut_idx = 0
                if left.find('-') == -1:
                    return parser(node.left, '', level + 1)
                for i in range(len(left)):
                    if left[i] == '-':
                        dash = True
                    elif dash and left[i] != '-':
                        cut_idx = i
                        break
                return parser(node.left, left[cut_idx:], level + 1)
            if right:
                right_value = int(subtree[:right.find('-')]) if right.find('-') != -1 else int(right)
                node.left = TreeNode(right_value)
                dash = False
                cut_idx = 0
                if left.find('-') == -1:
                    return parser(node.right, '', level + 1)
                for i in range(len(right)):
                    if right[i] == '-':
                        dash = True
                    elif dash and right[i] != '-':
                        cut_idx = i
                        break
                return parser(node.right, right[cut_idx:], level + 1)


        parser()

        return self.root



print(Solution().recoverFromPreorder(traversal="1-2--3---4-5--6---7"))