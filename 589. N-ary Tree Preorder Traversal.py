# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> list[int]:
        traversal = []

        def helper(root: Node):
            if root:
                traversal.append(root.val)
                if root.children:
                    for child in root.children:
                        helper(child)

        helper(root)

        return traversal

