class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for num in nums:
            if num == 0:
                nums.append(0)
                nums.remove(num)
        print(nums)

# Решение с Leetcode (Техника двух указателей)
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

Solution().moveZeroes([0, 1, 0, 3, 12])