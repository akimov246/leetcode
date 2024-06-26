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

        # def select_node_idx(nodes: list[int]) -> int:
        #     if len(nodes) % 2:
        #         return len(nodes) // 2
        #     else:
        #         return len(nodes) // 2 - 1

        def get_node_idx(left: int, right: int) -> int:
            sum_ = left + right
            if sum_ % 2:
                return sum_ // 2
            else:
                return sum_ // 2 - 1

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
        stack_rights = []
        def make_new_nodes(left: int = None, right: int = None):
            index = None
            if left is None and right is None:
                index = get_node_idx(0, len(nodes))
            elif left != right:
                index = get_node_idx(left, right)

            if index is not None and nodes[index]:
                new_nodes.append(nodes[index])
                nodes[index] = 0
                right = index
                stack_rights.reverse()
                stack_rights.append(right)
                stack_rights.reverse()
                index -= 1
                while index > -1:
                    if nodes[index] == 0:
                        left = index
                        break
                    index -= 1
                else:
                    left = 0
                make_new_nodes(left, right)

                left = stack_rights.pop()
                index = left + 1

                while index < len(nodes):
                    if nodes[index] == 0:
                        right = index
                        break
                    index += 1
                else:
                    right = len(nodes)
                make_new_nodes(left + 1, right)

        def make_bst():
            make_new_nodes()
            print(new_nodes)
            new_root = TreeNode(new_nodes.pop(0))
            for node in new_nodes:
                add_new_node(new_root, node)
            return new_root

        return make_bst()




# Попробовать написать генераторную функцию !

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