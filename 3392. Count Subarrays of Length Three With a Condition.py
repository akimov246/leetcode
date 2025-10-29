class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        result = 0
        for i in range(1, len(nums) - 1):
            if nums[i] / 2 == nums[i - 1] + nums[i + 1]:
                result += 1

        return result


print(Solution().countSubarrays(nums = [1,2,1,4,1]))