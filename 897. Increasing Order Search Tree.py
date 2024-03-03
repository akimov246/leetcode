# Definition for a binary tree node.
class TreeNode:

    __slots__ = ('val', 'left', 'right')

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    __slots__ = ('nodes')

    def __init__(self):
        self.nodes = set()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.get_nodes(root)
        self.nodes = sorted(list(self.nodes), reverse=True)
        new_root = TreeNode(self.nodes[-1])
        self.nodes.pop()
        self.make_new_tree(new_root)
        return new_root

    def make_new_tree(self, root: TreeNode):
        if self.nodes:
            root.right = TreeNode(self.nodes[-1])
            self.nodes.pop()
            self.make_new_tree(root.right)

    def get_nodes(self, root: TreeNode):
        if root:
            self.nodes.add(root.val)
            self.get_nodes(root.left)
            self.get_nodes(root.right)

tree = TreeNode(5)
tree.left = TreeNode(1)
tree.right = TreeNode(7)

#print(Solution().__dict__)

#print(Solution().increasingBST(tree))
