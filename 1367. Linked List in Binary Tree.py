from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:

    init_head = None

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def get_tree_nodes(root: Optional[TreeNode], tree_nodes: Optional[set] = None):
            if tree_nodes is None:
                tree_nodes = set()
            if root:
                if root.val == head.val:
                    tree_nodes.add(root)
                get_tree_nodes(root.left, tree_nodes)
                get_tree_nodes(root.right, tree_nodes)
            return tree_nodes

        tree_nodes = get_tree_nodes(root)

        def helper(head: Optional[ListNode], root: Optional[TreeNode]):
            if head is None:
                return True
            if root:
                if root.val == head.val:
                    return helper(head.next, root.left) or helper(head.next, root.right)
                else:
                    return False
            else:
                return False

        for node in tree_nodes:
            if helper(head, node):
                return True
        return False

root = TreeNode(1)
root.left = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(8)

print(Solution().isSubPath(head, root))