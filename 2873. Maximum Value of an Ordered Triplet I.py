class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    result = max(result, (nums[i] - nums[j]) * nums[k])
        return result

print(Solution().maximumTripletValue(nums = [12,6,1,2,7]))