class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        ans = 0
        self.nodes = []
        self.getAllNodes(root)
        for node in self.nodes:
            self.v = []
            self.getV(node)
            ans = max(max([abs(self.v[0] - value) for value in self.v]), ans)
        return ans

    def getAllNodes(self, root):
        if root:
            self.nodes.append(root)
            self.getAllNodes(root.left)
            self.getAllNodes(root.right)

    def getV(self, root):
        if root:
            self.v.append(root.val)
            self.getV(root.left)
            self.getV(root.right)

# Это решение еще хуже предыдущего
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        self.nodes = []
        self.getAllNodes(root)
        v = (self.helper(node, node) for node in self.nodes)
        return max(v)

    def helper(self, root: TreeNode, node: TreeNode):
        if node:
            if node.left and node.right:
                return max(self.helper(root, node.left), self.helper(root, node.right), abs(root.val - node.val))
            elif node.left:
                return max(self.helper(root, node.left), abs(root.val - node.val))
            elif node.right:
                return max(self.helper(root, node.right), abs(root.val - node.val))
            return abs(root.val - node.val)

    def getAllNodes(self, root):
        if root:
            self.nodes.append(root)
            self.getAllNodes(root.left)
            self.getAllNodes(root.right)

root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(0)
root.right.right.left = TreeNode(3)

print(Solution().maxAncestorDiff(root))
