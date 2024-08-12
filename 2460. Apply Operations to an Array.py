class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = []
        zero_counter = 0
        for n in nums:
            if n:
                result.append(n)
            else:
                zero_counter += 1
        return result + [0] * zero_counter

print(Solution().applyOperations(nums = [1,2,2,1,1,0]))