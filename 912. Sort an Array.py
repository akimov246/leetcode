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

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        pass


tree = TreeNode(1)
tree.quantity += 1
print(tree)

print(Solution().sortArray(nums = [5,2,3,1]))