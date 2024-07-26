import random
from typing import Iterable
from functools import cache

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
        random.shuffle(nums)
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
        i = 0
        j = 1
        while j != len(nums):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j = i + 1
                continue
            j += 1
            if j == len(nums):
                i += 1
                j = i + 1

        return nums

#print(Solution().sortArray(nums=list(range(1, 50001))))

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.minrun = self.__get_minrun(len(nums))
        print(self.minrun)
        self.runs = self.__split_array(nums)
        print(self.runs)
        result = self.__merge()
        return result

    def __get_minrun(self, N):
        bin_N = bin(N)[2:].zfill(7)
        most = bin_N[:6]
        least = bin_N[6:]
        if '1' in least:
            return int(most, 2) + 1
        return int(most, 2)

    def __split_array(self, array):
        runs = []
        while array:
            run = []
            for i in range(len(array)):
                if i in (0, 1):
                    run.append(array[i])
                else:
                    if run[-1] < run[-2]:
                        if array[i] < run[-1]:
                            run.append(array[i])
                    else:
                        if array[i] >= run[-1]:
                            run.append(array[i])
            if run[0] > run[-1]:
                run = run[::-1]
            runs.append(run)
            for element in run:
                array.remove(element)
            if len(run) < self.minrun:
                add_to_run = []
                for _ in range(self.minrun - len(run)):
                    if array:
                        add_to_run.append(array.pop())
                runs[-1].extend(add_to_run)
                self.__insertion_sort(runs[-1])

        return runs

    def __insertion_sort(self, run):
        for i in range(1, len(run)):
            j = i
            while j > 0 and run[j - 1] > run[j]:
                run[j - 1], run[j] = run[j], run[j - 1]
                j -= 1

    def __merge(self):
        result = self.runs.pop()
        for run in self.runs:
            tmp = []
            i = 0
            j = 0
            while i != len(result) and j != len(run):
                if result[i] < run[j]:
                    tmp.append(result[i])
                    i += 1
                else:
                    tmp.append(run[j])
                    j += 1
            if i != len(result):
                tmp.extend(result[i:])
            if j != len(run):
                tmp.extend(run[j:])
            result = tmp
        return result

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def quicksort(array, low, high):
            if low < high:
                p = partition(array, low, high)
                quicksort(array, low, p)
                quicksort(array, p + 1, high)

        def partition(array, low, high):
            pivot = array[(low + high) // 2]
            #pivot = array[random.randint(low, high)]
            i = low
            j = high
            while i <= j:
                while array[i] < pivot:
                    i += 1
                while array[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                i += 1
                j -= 1
                array[i], array[j] = array[j], array[i]
            return j

        quicksort(nums, 0, len(nums) - 1)
        return nums

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        return nums

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i != len(left) and j != len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                if i == len(left):
                    result.extend(right[j:])
                if j == len(right):
                    result.extend(left[i:])
            return result

        def merge_sort(array):
            if len(array) == 1:
                return array
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            return merge(merge_sort(left), merge_sort(right))

        return merge_sort(nums)


print(Solution().sortArray(nums = [5,1,1,2,0,0]))