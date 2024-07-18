from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.nodes = []

        def get_all_nodes(node: TreeNode):
            if node:
                if node.left or node.right:
                    self.nodes.append(node)
                get_all_nodes(node.left)
                get_all_nodes(node.right)

        get_all_nodes(root)
        print(self.nodes)

        dist_to_leaves_map = defaultdict(list)

        def get_dist_to_leaves(root: TreeNode, node: TreeNode, dist: int = 0):
            if node:
                if node.left is None and node.right is None:
                    dist_to_leaves_map[root.val].append(dist)
                else:
                    dist += 1
                    get_dist_to_leaves(root, node.left, dist)
                    get_dist_to_leaves(root, node.right, dist)

        for node in self.nodes:
            get_dist_to_leaves(node, node)
        print(dist_to_leaves_map)

        counter = 0
        for node in dist_to_leaves_map:
            if len(dist_to_leaves_map[node]) > 1:
                for i in range(len(dist_to_leaves_map[node])):
                    for j in range(i + 1, len(dist_to_leaves_map[node])):
                        if dist_to_leaves_map[node][i] + dist_to_leaves_map[node][j] <= distance:
                            counter += 1
        return counter

root = TreeNode(15)
root.left = TreeNode(66)
root.left.left = TreeNode(97)
root.left.right = TreeNode(60)
root.left.left.right = TreeNode(54)
root.left.right.right = TreeNode(49)
root.left.right.right.right = TreeNode(90)
root.right = TreeNode(55)
root.right.left = TreeNode(12)
root.right.left.right = TreeNode(9)
root.right.right = TreeNode(56)

print(Solution().countPairs(root, distance=5))