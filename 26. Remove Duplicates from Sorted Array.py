class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unic_nums = list(dict.fromkeys(nums).keys())
        for i in range(len(unic_nums)):
            nums[i] = unic_nums[i]
        return len(unic_nums)

print(Solution().removeDuplicates([1, 1, 2]))