from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root_nodes = []
        self.subRoot_structure = []

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self._getNodes(root)
        self._getStructure(subRoot, self.subRoot_structure)
        for node in self.root_nodes:
            node_structure = []
            self._getStructure(node, node_structure)
            if node_structure == self.subRoot_structure:
                return True
        return False

    def _getNodes(self, root):
        if root:
            self.root_nodes.append(root)
            self._getNodes(root.left)
            self._getNodes(root.right)

    def _getStructure(self, node: TreeNode, structure: list):
        if node:
            structure.append(node.val)
            self._getStructure(node.left, structure)
            self._getStructure(node.right, structure)
        else:
            structure.append(None)



root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot))