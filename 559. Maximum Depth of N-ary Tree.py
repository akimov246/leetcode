# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return str(self.val)

class Solution:
    def maxDepth(self, root: Node) -> int:

        def helper(root: Node, deep: int):
            if not root:
                return 0

            if root.children:
                return deep + max(helper(root.children[i], deep) for i in range(len(root.children)))

            return deep

        return helper(root, 1)


tree = Node(1)
tree.children = [Node(3), Node(2), Node(4)]
tree.children[0].children = [Node(5), Node(6)]

print(Solution().maxDepth(tree))