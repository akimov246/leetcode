class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:

        nums.sort(reverse=True)
        i = 0
        summa = sum(nums)

        while i < len(nums):
            if nums[i] < summa - nums[i]:
                i += 1
            else:
                nums.remove(nums[i])
                summa = sum(nums)

        return sum(nums) if len(nums) > 2 else -1

# print(Solution().largestPerimeter([1,12,1,2,5,50,3]))
#print(Solution().largestPerimeter([5,5,5]))