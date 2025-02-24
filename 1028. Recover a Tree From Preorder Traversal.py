from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:

    def __init__(self):
        self.root = None
        self.traversal = None

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        self.traversal = traversal

        def helper(node, t: str):
            if not t:
                return False
            if not self.root and t[0] != '-':
                idx = t.find('-')
                if idx == -1:
                    self.root = TreeNode(int(traversal))
                else:
                    self.root = TreeNode(int(traversal[:idx]))
                return helper(self.root, t[idx:])
            if t[0] == '-':
                dash_target = None
                for i, char in enumerate(t):
                    if char != '-':
                        dash_target = t[:i]
                        break
                idx = 0
                leaves = []
                while True:
                    idx = t.find(dash_target, idx)
                    if idx == -1 or len(leaves) == 2:
                        break
                    if t[idx + len(dash_target)] != '-' and t[idx - 1] != '-':
                        for i in range(idx + len(dash_target), len(t)):
                            if i == len(t) - 1:
                                value = int(t[idx + len(dash_target):len(t)])
                                leaves.append((value, len(t)))
                                break
                            if t[i] == '-':
                                dbg = t[idx + len(dash_target): i]
                                value = int(t[idx + len(dash_target): i])
                                leaves.append((value, i))
                                break
                    idx += 1
                #print(leaves)
                if len(leaves) == 2:
                    val1, slice1 = leaves[0]
                    val2, slice2 = leaves[1]
                    node.left = TreeNode(val1)
                    node.right = TreeNode(val2)
                    helper(node.left, t[slice1: slice2 - len(str(val2)) - len(dash_target)])
                    helper(node.right, t[slice2:])
                elif len(leaves) == 1:
                    val, slice = leaves[0]
                    node.left = TreeNode(val)
                    helper(node.left, t[slice:])

        helper(self.root, self.traversal)

        return self.root



print(Solution().recoverFromPreorder(traversal = "1-2--3--4-5--6--7"))