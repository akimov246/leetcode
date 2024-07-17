from itertools import zip_longest

class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even_idx_elements = []
        odd_idx_elements = []
        new_nums = []
        for i in range(len(nums)):
            if i % 2:
                odd_idx_elements.append(nums[i])
            else:
                even_idx_elements.append(nums[i])
        even_idx_elements.sort()
        odd_idx_elements.sort(reverse=True)
        for e, o in zip_longest(even_idx_elements, odd_idx_elements):
            if e:
                new_nums.append(e)
            if o:
                new_nums.append(o)
        return new_nums


print(Solution().sortEvenOdd(nums = [4,1,2,3]))