# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        nodes = []

        def get_nodes(root: TreeNode):
            if root:
                nodes.append(root.val)
                get_nodes(root.left)
                get_nodes(root.right)

        get_nodes(root)
        nodes.sort()
        print(nodes)

        def get_middle_idx(nodes: list[int]) -> int:
            if len(nodes) % 2:
                return len(nodes) // 2
            else:
                return len(nodes) // 2 - 1

        def add_new_node(node: TreeNode, value: int) -> None:
            if value < node.val:
                if node.left:
                    add_new_node(node.left, value)
                else:
                    node.left = TreeNode(value)
            elif value > node.val:
                if node.right:
                    add_new_node(node.right, value)
                else:
                    node.right = TreeNode(value)

        new_nodes = []
        def make_new_nodes(nodes: list[int]):
            if nodes:
                index = get_middle_idx(nodes)
                new_nodes.append(nodes[index])
                make_new_nodes(nodes[:index])
                make_new_nodes(nodes[index + 1:])

        make_new_nodes(nodes)
        def make_new_tree():
            root = TreeNode(new_nodes.pop(0))
            for node in new_nodes:
                add_new_node(root, node)
            return root

        return make_new_tree()


root = TreeNode(1)
root.right = TreeNode(15)
root.right.right = TreeNode(17)
root.right.left = TreeNode(14)
root.right.left.left = TreeNode(7)
root.right.left.left.left = TreeNode(2)
root.right.left.left.right = TreeNode(12)
root.right.left.left.left.right = TreeNode(3)
root.right.left.left.right.left = TreeNode(9)
root.right.left.left.right.left.right = TreeNode(11)

print(Solution().balanceBST(root))