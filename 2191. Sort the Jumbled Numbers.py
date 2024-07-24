from functools import cache

class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:

        @cache
        def my_sort(num):
            num = str(num)
            new_num = ''
            for n in num:
                new_num += str(mapping[int(n)])
            return int(new_num)

        return sorted(nums, key=my_sort)

print(Solution().sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))