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

        def select_node_idx(nodes: list[int]):
            if len(nodes) % 2:
                return len(nodes) // 2
            else:
                return len(nodes) // 2 - 1

        def add_new_node(node: TreeNode, value: int):
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
        def make_new_nodes(nodes):
            if len(nodes) > 1:
                index = select_node_idx(nodes)
                new_nodes.append(nodes[index])
                nodes[index] = 0
                make_new_nodes(nodes[nodes[]])



        def make_bst():
            new_root = select_node(nodes)
            new_nodes = []
            while len(new_nodes) != len(nodes):
                new_nodes.append(select_node(nodes))



        return make_bst()







root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

print(Solution().balanceBST(root))