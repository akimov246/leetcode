from typing import Iterable

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.quantity = 1
        self.left = None
        self.right = None

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __repr__(self):
        return f'Значение: {self.value}, количество: {self.quantity}'

class Tree:

    def __init__(self, nums: Iterable):
        self.root = None
        nums = tuple(nums)
        self.__make_tree(nums)

    def __make_tree(self, nums: Iterable):
        for num in nums:
            if self.root is None:
                self.root = TreeNode(num)
            else:
                self.add_node(self.root, num)

    def add_node(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.add_node(node.left, value)
        elif value == node.value:
            node.quantity += 1
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.add_node(node.right, value)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        result = []
        tree = Tree(nums)

        def helper(node: TreeNode):
            if node:
                helper(node.left)
                result.extend([node.value] * node.quantity)
                helper(node.right)

        helper(tree.root)
        return result

#print(Solution().sortArray(nums = list(range(1, 500 + 1))))

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        pass

print(Solution().sortArray(nums = [5,1,1,2,0,0]))