# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return str(self.val)

class Solution:
    def postorder(self, root: Node) -> list[int]:

        traversal = []

        def helper(root: Node):
            if not root:
                return

            if root.children:
                for child in root.children:
                    helper(child)

            traversal.append(root.val)

        helper(root)

        return traversal

tree = Node(1)
tree.children = [Node(3), Node(2), Node(4)]
tree.children[0].children = [Node(5), Node(6)]

print(Solution().postorder(tree))